import tkinter as tk
from tkinter import ttk, messagebox
from pymodbus.client import ModbusTcpClient
import struct
import threading
import time
import sys
import os

# Hide console window on Windows
if sys.platform == "win32":
    try:
        import win32gui
        import win32con
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    except ImportError:
        pass

class DualModbusGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dual Modbus Reader - e2tango & PQI-DA v1.0")
        self.root.geometry("1200x700")

        self.client_e2tango = None
        self.client_pqi = None
        self.is_connected_e2tango = False
        self.is_connected_pqi = False
        self.reading_thread = None
        self.stop_reading = False

        # Power monitoring from energy counters
        self.energy_history = {"e2tango": {}, "pqi": {}}
        self.power_averages = {"e2tango": {}, "pqi": {}}

        # Scaling options
        self.use_kwh_scaling = tk.BooleanVar(value=False)
        self.use_kw_scaling = tk.BooleanVar(value=False)

        self.setup_gui()
        self.setup_register_mapping()

    def setup_gui(self):
        # Connection frame
        conn_frame = ttk.LabelFrame(self.root, text="Connection Settings", padding="10")
        conn_frame.pack(fill="x", padx=10, pady=5)

        # e2tango connection
        ttk.Label(conn_frame, text="e2tango IP:").grid(row=0, column=0, sticky="w", padx=5)
        self.ip_e2tango_entry = ttk.Entry(conn_frame, width=15)
        self.ip_e2tango_entry.insert(0, "192.168.41.99")
        self.ip_e2tango_entry.grid(row=0, column=1, padx=5)

        ttk.Label(conn_frame, text="Port:").grid(row=0, column=2, sticky="w", padx=5)
        self.port_e2tango_entry = ttk.Entry(conn_frame, width=8)
        self.port_e2tango_entry.insert(0, "502")
        self.port_e2tango_entry.grid(row=0, column=3, padx=5)

        self.connect_e2tango_btn = ttk.Button(conn_frame, text="Connect e2tango", command=self.toggle_e2tango_connection)
        self.connect_e2tango_btn.grid(row=0, column=4, padx=10)

        self.status_e2tango_label = ttk.Label(conn_frame, text="Disconnected", foreground="red")
        self.status_e2tango_label.grid(row=0, column=5, padx=10)

        # PQI connection
        ttk.Label(conn_frame, text="PQI IP:").grid(row=1, column=0, sticky="w", padx=5)
        self.ip_pqi_entry = ttk.Entry(conn_frame, width=15)
        self.ip_pqi_entry.insert(0, "192.168.41.95")
        self.ip_pqi_entry.grid(row=1, column=1, padx=5)

        ttk.Label(conn_frame, text="Port:").grid(row=1, column=2, sticky="w", padx=5)
        self.port_pqi_entry = ttk.Entry(conn_frame, width=8)
        self.port_pqi_entry.insert(0, "502")
        self.port_pqi_entry.grid(row=1, column=3, padx=5)

        self.connect_pqi_btn = ttk.Button(conn_frame, text="Connect PQI", command=self.toggle_pqi_connection)
        self.connect_pqi_btn.grid(row=1, column=4, padx=10)

        self.status_pqi_label = ttk.Label(conn_frame, text="Disconnected", foreground="red")
        self.status_pqi_label.grid(row=1, column=5, padx=10)

        # Data frame
        data_frame = ttk.LabelFrame(self.root, text="Measurement Comparison", padding="10")
        data_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Treeview for data display
        self.columns = ("Description", "e2tango_Name", "e2tango_Value", "PQI_Name", "PQI_Value", "Unit")
        self.tree = ttk.Treeview(data_frame, columns=self.columns, show="headings", height=20)

        # Column widths
        column_widths = {
            "Description": 250,
            "e2tango_Name": 80,
            "e2tango_Value": 100,
            "PQI_Name": 80,
            "PQI_Value": 100,
            "Unit": 60
        }

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths[col])

        # Column visibility state
        self.column_visible = {col: True for col in self.columns}
        self.column_vars = {}

        scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Control frame
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill="x", padx=10, pady=5)

        self.read_btn = ttk.Button(control_frame, text="Start Reading", command=self.toggle_reading, state="disabled")
        self.read_btn.pack(side="left", padx=5)

        ttk.Label(control_frame, text="Refresh Rate (ms):").pack(side="left", padx=10)
        self.refresh_entry = ttk.Entry(control_frame, width=8)
        self.refresh_entry.insert(0, "2000")
        self.refresh_entry.pack(side="left", padx=5)

        # Scaling controls
        ttk.Label(control_frame, text="Scaling:").pack(side="left", padx=(20, 5))
        kwh_cb = ttk.Checkbutton(control_frame, text="kWh/kvarh", variable=self.use_kwh_scaling)
        kwh_cb.pack(side="left", padx=2)
        kw_cb = ttk.Checkbutton(control_frame, text="kW/kVA/kvar", variable=self.use_kw_scaling)
        kw_cb.pack(side="left", padx=2)

        # Column visibility controls
        ttk.Label(control_frame, text="Show Columns:").pack(side="left", padx=(20, 5))
        for col in self.columns:
            var = tk.BooleanVar(value=True)
            self.column_vars[col] = var
            cb = ttk.Checkbutton(control_frame, text=col, variable=var,
                               command=lambda c=col: self.toggle_column(c))
            cb.pack(side="left", padx=2)

    def setup_register_mapping(self):
        # Register mapping: (e2tango_addr, e2tango_name, description, pqi_addr, pqi_name, unit, pqi_conversion)
        self.register_mapping = [
            (0x000, "I1", "Wartosc pradu I1", 41016, "i1", "A", 1.0),
            (0x002, "I2", "Wartosc pradu I2", 41018, "i2", "A", 1.0),
            (0x004, "I3", "Wartosc pradu I3", 41020, "i3", "A", 1.0),
            (0x006, "U12", "Wartosc napiecia U12", 41010, "u12", "V", 1.0),
            (0x008, "U23", "Wartosc napiecia U23", 41012, "u23", "V", 1.0),
            (0x00A, "U31", "Wartosc napiecia U31", 41014, "u31", "V", 1.0),
            (0x00C, "f", "Wartosc czestotliwosci", 41000, "f", "Hz", 1.0),
            (0x00E, "P", "Wartosc mocy czynnej", 1964, "p", "W", 1.0),
            (0x010, "Q", "Wartosc mocy biernej", 1996, "q1", "var", 1.0),
            (0x012, "S", "Wartosc mocy pozornej", 1968, "s", "VA", 1.0),
            (0x014, "cos(fi)", "Wartosc cos(fi)", 2048, "cosphid", "", 1.0),
            (0x016, "tg(fi)", "Wartosc tg(fi)", 2040, "sinphi", "", 1.0),
            (0x018, "Ec+", "Licznik energii czynnej dodatniej", 2184, "wi", "Wh", 1000.0),
            (0x01A, "Ec-", "Licznik energii czynnej ujemnej", 2168, "wt", "Wh", 1000.0),
            (0x01C, "Eb+", "Licznik energii biernej dodatniej", 2208, "wri", "varh", 1000.0),
            (0x01E, "Eb-", "Licznik energii biernej ujemnej", 2200, "wro", "varh", 1000.0),
        ]

        # Additional power monitoring from energy counters (calculated)
        self.power_monitoring = [
            ("P_avg_Ec+", "Moc srednia 1min z Ec+", "P_avg_wi", "W"),
            ("P_avg_Ec-", "Moc srednia 1min z Ec-", "P_avg_wt", "W"),
            ("Q_avg_Eb+", "Moc bierna srednia 1min z Eb+", "Q_avg_wri", "var"),
            ("Q_avg_Eb-", "Moc bierna srednia 1min z Eb-", "Q_avg_wro", "var"),
        ]

        # Populate tree with register info
        for e2t_addr, e2t_name, desc, pqi_addr, pqi_name, unit, conv in self.register_mapping:
            self.tree.insert("", "end", values=(desc, e2t_name, "---", pqi_name, "---", unit))

        # Add power monitoring entries
        for calc_name, desc, pqi_calc_name, unit in self.power_monitoring:
            self.tree.insert("", "end", values=(desc, calc_name, "---", pqi_calc_name, "---", unit))

    def toggle_column(self, column):
        """Toggle visibility of a column"""
        is_visible = self.column_vars[column].get()
        self.column_visible[column] = is_visible

        # Update displayed columns list
        visible_columns = [col for col in self.columns if self.column_visible[col]]
        self.tree.configure(displaycolumns=visible_columns)

    def toggle_e2tango_connection(self):
        if not self.is_connected_e2tango:
            self.connect_e2tango()
        else:
            self.disconnect_e2tango()

    def toggle_pqi_connection(self):
        if not self.is_connected_pqi:
            self.connect_pqi()
        else:
            self.disconnect_pqi()

    def connect_e2tango(self):
        try:
            ip = self.ip_e2tango_entry.get().strip()
            port = int(self.port_e2tango_entry.get().strip())

            self.client_e2tango = ModbusTcpClient(ip, port=port)
            result = self.client_e2tango.connect()

            if result:
                self.is_connected_e2tango = True
                self.status_e2tango_label.config(text="Connected", foreground="green")
                self.connect_e2tango_btn.config(text="Disconnect e2tango")
                self.ip_e2tango_entry.config(state="disabled")
                self.port_e2tango_entry.config(state="disabled")
                self.update_read_button_state()
            else:
                messagebox.showerror("Error", "Failed to connect to e2tango device")

        except Exception as e:
            messagebox.showerror("Error", f"e2tango connection error: {str(e)}")

    def connect_pqi(self):
        try:
            ip = self.ip_pqi_entry.get().strip()
            port = int(self.port_pqi_entry.get().strip())

            self.client_pqi = ModbusTcpClient(ip, port=port)
            result = self.client_pqi.connect()

            if result:
                self.is_connected_pqi = True
                self.status_pqi_label.config(text="Connected", foreground="green")
                self.connect_pqi_btn.config(text="Disconnect PQI")
                self.ip_pqi_entry.config(state="disabled")
                self.port_pqi_entry.config(state="disabled")
                self.update_read_button_state()
            else:
                messagebox.showerror("Error", "Failed to connect to PQI device")

        except Exception as e:
            messagebox.showerror("Error", f"PQI connection error: {str(e)}")

    def disconnect_e2tango(self):
        if self.reading_thread and self.reading_thread.is_alive():
            self.stop_reading = True
            self.reading_thread.join()

        if self.client_e2tango:
            self.client_e2tango.close()

        self.is_connected_e2tango = False
        self.status_e2tango_label.config(text="Disconnected", foreground="red")
        self.connect_e2tango_btn.config(text="Connect e2tango")
        self.ip_e2tango_entry.config(state="normal")
        self.port_e2tango_entry.config(state="normal")
        self.update_read_button_state()

    def disconnect_pqi(self):
        if self.reading_thread and self.reading_thread.is_alive():
            self.stop_reading = True
            self.reading_thread.join()

        if self.client_pqi:
            self.client_pqi.close()

        self.is_connected_pqi = False
        self.status_pqi_label.config(text="Disconnected", foreground="red")
        self.connect_pqi_btn.config(text="Connect PQI")
        self.ip_pqi_entry.config(state="normal")
        self.port_pqi_entry.config(state="normal")
        self.update_read_button_state()

    def update_read_button_state(self):
        if self.is_connected_e2tango and self.is_connected_pqi:
            self.read_btn.config(state="normal")
        else:
            self.read_btn.config(state="disabled")

    def toggle_reading(self):
        if not self.reading_thread or not self.reading_thread.is_alive():
            self.start_reading()
        else:
            self.stop_reading_data()

    def start_reading(self):
        self.stop_reading = False
        self.reading_thread = threading.Thread(target=self.read_data_loop, daemon=True)
        self.reading_thread.start()
        self.read_btn.config(text="Stop Reading")
        self.refresh_entry.config(state="disabled")

    def stop_reading_data(self):
        self.stop_reading = True
        if self.reading_thread:
            self.reading_thread.join()
        self.read_btn.config(text="Start Reading")
        self.refresh_entry.config(state="normal")

    def read_data_loop(self):
        try:
            refresh_rate = int(self.refresh_entry.get()) / 1000.0
        except:
            refresh_rate = 2.0

        while not self.stop_reading and self.is_connected_e2tango and self.is_connected_pqi:
            try:
                e2tango_data = self.read_e2tango_registers()
                pqi_data = self.read_pqi_registers()
                self.root.after(0, lambda: self.update_display(e2tango_data, pqi_data))
                time.sleep(refresh_rate)
            except Exception as e:
                error_msg = f"Reading error: {str(e)}"
                self.root.after(0, lambda msg=error_msg: messagebox.showerror("Error", msg))
                break

    def read_e2tango_registers(self):
        """Read e2tango registers using Input Registers with IEEE-754 Little Endian"""
        if not self.client_e2tango or not self.is_connected_e2tango:
            return {}

        # Read all registers (each float uses 2 registers)
        total_registers = len(self.register_mapping) * 2
        result = self.client_e2tango.read_input_registers(address=0x0000, count=total_registers)

        if not hasattr(result, 'registers') or result.registers is None:
            raise Exception("e2tango: Failed to read registers")

        data = {}
        for i, (e2t_addr, e2t_name, desc, pqi_addr, pqi_name, unit, conv) in enumerate(self.register_mapping):
            reg_index = i * 2
            if reg_index + 1 < len(result.registers):
                reg1 = result.registers[reg_index]
                reg2 = result.registers[reg_index + 1]

                # IEEE-754 Little Endian conversion
                raw_bytes = struct.pack('<HH', reg1, reg2)
                float_value = struct.unpack('<f', raw_bytes)[0]
                data[e2t_name] = float_value

        return data

    def read_pqi_registers(self):
        """Read PQI registers using Holding Registers with IEEE-754 float32"""
        if not self.client_pqi or not self.is_connected_pqi:
            return {}

        data = {}
        for e2t_addr, e2t_name, desc, pqi_addr, pqi_name, unit, conv in self.register_mapping:
            try:
                # Read 2 registers for each float32 value
                result = self.client_pqi.read_holding_registers(address=pqi_addr, count=2)

                if hasattr(result, 'registers') and len(result.registers) >= 2:
                    reg1 = result.registers[0]
                    reg2 = result.registers[1]

                    # IEEE-754 Little Endian conversion (as determined from testing)
                    raw_bytes = struct.pack('<HH', reg1, reg2)
                    float_value = struct.unpack('<f', raw_bytes)[0]

                    # Apply conversion factor (kWh->Wh, kvarh->varh)
                    converted_value = float_value * conv
                    data[pqi_name] = converted_value

            except Exception:
                # Silent error handling in production
                data[pqi_name] = None

        return data

    def update_display(self, e2tango_data, pqi_data):
        """Update the display with data from both devices"""
        for i, (e2t_addr, e2t_name, desc, pqi_addr, pqi_name, unit, conv) in enumerate(self.register_mapping):
            try:
                item_id = self.tree.get_children()[i]

                # Get values
                e2t_value = e2tango_data.get(e2t_name, None)
                pqi_value = pqi_data.get(pqi_name, None)

                # Format values with scaling support
                if unit in ["Wh", "varh"]:
                    e2t_str = self.format_energy_value(e2t_value, unit)
                    pqi_str = self.format_energy_value(pqi_value, unit)
                    display_unit = ("k" + unit) if self.use_kwh_scaling.get() else unit
                elif unit in ["W", "var", "VA"]:
                    e2t_str = self.format_power_value(e2t_value, unit)
                    pqi_str = self.format_power_value(pqi_value, unit)
                    display_unit = ("k" + unit) if self.use_kw_scaling.get() else unit
                else:
                    e2t_str = f"{e2t_value:.3f}" if e2t_value is not None else "---"
                    pqi_str = f"{pqi_value:.3f}" if pqi_value is not None else "---"
                    display_unit = unit

                # Update tree item
                new_values = (desc, e2t_name, e2t_str, pqi_name, pqi_str, display_unit)
                self.tree.item(item_id, values=new_values)

            except Exception:
                # Silent error handling in production
                pass

        # Update power monitoring (calculated from energy counters)
        self.update_power_monitoring(e2tango_data, pqi_data)

    def update_power_monitoring(self, e2tango_data, pqi_data):
        """Calculate average power from energy counter differences"""
        current_time = time.time()

        # Update energy history for e2tango (all energy counters)
        energy_registers_e2t = ["Ec+", "Ec-", "Eb+", "Eb-"]
        for reg in energy_registers_e2t:
            if reg in e2tango_data and e2tango_data[reg] is not None:
                self.update_energy_history("e2tango", reg, e2tango_data[reg], current_time)

        # Update energy history for PQI (all energy counters)
        energy_registers_pqi = ["wi", "wt", "wro", "wri"]
        for reg in energy_registers_pqi:
            if reg in pqi_data and pqi_data[reg] is not None:
                self.update_energy_history("pqi", reg, pqi_data[reg], current_time)

        # Calculate average powers for all energy counters
        power_calculations = [
            ("e2tango", "Ec+", "pqi", "wi"),  # Active power consumption
            ("e2tango", "Ec-", "pqi", "wt"),  # Active power total
            ("e2tango", "Eb+", "pqi", "wri"), # Reactive power supply
            ("e2tango", "Eb-", "pqi", "wro"), # Reactive power consumption
        ]

        calculated_powers = []
        for e2t_dev, e2t_reg, pqi_dev, pqi_reg in power_calculations:
            e2t_power = self.calculate_average_power(e2t_dev, e2t_reg, 60.0, min_time=30.0)
            pqi_power = self.calculate_average_power(pqi_dev, pqi_reg, 60.0, min_time=30.0)
            calculated_powers.append((e2t_power, pqi_power))

        # Update power monitoring display for all calculated powers
        start_idx = len(self.register_mapping)
        children = self.tree.get_children()

        for i, (calc_name, desc, pqi_calc_name, unit) in enumerate(self.power_monitoring):
            if start_idx + i < len(children):
                item_id = children[start_idx + i]
                e2t_power, pqi_power = calculated_powers[i]

                # Format with power scaling
                if unit in ["W", "var", "VA"]:
                    e2t_str = self.format_power_value(e2t_power, unit)
                    pqi_str = self.format_power_value(pqi_power, unit)
                    display_unit = ("k" + unit) if self.use_kw_scaling.get() else unit
                else:
                    e2t_str = f"{e2t_power:.3f}" if e2t_power is not None else "---"
                    pqi_str = f"{pqi_power:.3f}" if pqi_power is not None else "---"
                    display_unit = unit

                self.tree.item(item_id, values=(desc, calc_name, e2t_str, pqi_calc_name, pqi_str, display_unit))

    def update_energy_history(self, device, register, value, timestamp):
        """Store energy value with timestamp for power calculation"""
        if device not in self.energy_history:
            self.energy_history[device] = {}
        if register not in self.energy_history[device]:
            self.energy_history[device][register] = []

        # Add new reading
        self.energy_history[device][register].append((timestamp, value))

        # Keep only last 3 minutes of data
        cutoff_time = timestamp - 180.0
        self.energy_history[device][register] = [
            (t, v) for t, v in self.energy_history[device][register] if t > cutoff_time
        ]

    def calculate_average_power(self, device, register, time_window, min_time=60.0):
        """Calculate average power over time window from energy differences"""
        if (device not in self.energy_history or
            register not in self.energy_history[device] or
            len(self.energy_history[device][register]) < 2):
            return None

        history = self.energy_history[device][register]
        current_time = history[-1][0]
        start_time = current_time - time_window

        # Find readings within time window
        readings_in_window = [(t, v) for t, v in history if t >= start_time]

        if len(readings_in_window) < 2:
            return None

        # Calculate power as energy difference / time difference
        first_reading = readings_in_window[0]
        last_reading = readings_in_window[-1]

        time_diff = last_reading[0] - first_reading[0]
        energy_diff = last_reading[1] - first_reading[1]

        # Require minimum time span for reliable average
        if time_diff < min_time:
            return None

        # Convert Wh to W (energy/time), varh to var
        power_avg = (energy_diff / time_diff) * 3600.0  # Wh/s -> W

        return power_avg

    def format_energy_value(self, value, unit):
        """Format energy value according to scaling preference"""
        if value is None:
            return "---"

        if self.use_kwh_scaling.get() and unit in ["Wh", "varh"]:
            # Convert to kWh/kvarh
            scaled_value = value / 1000.0
            return f"{scaled_value:.3f}"
        else:
            return f"{value:.3f}"

    def format_power_value(self, value, unit):
        """Format power value according to scaling preference"""
        if value is None:
            return "---"

        if self.use_kw_scaling.get() and unit in ["W", "var", "VA"]:
            # Convert to kW/kvar/kVA
            scaled_value = value / 1000.0
            return f"{scaled_value:.3f}"
        else:
            return f"{value:.3f}"

    def on_closing(self):
        if self.is_connected_e2tango or self.is_connected_pqi:
            self.disconnect_e2tango()
            self.disconnect_pqi()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DualModbusGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()