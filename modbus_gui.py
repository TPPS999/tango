import tkinter as tk
from tkinter import ttk, messagebox
from pymodbus.client import ModbusTcpClient
import struct
import threading
import time

class ModbusGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Modbus Reader")
        self.root.geometry("800x600")

        self.client = None
        self.is_connected = False
        self.reading_thread = None
        self.stop_reading = False

        self.setup_gui()
        self.setup_modbus_registers()

    def setup_gui(self):
        # Connection frame
        conn_frame = ttk.LabelFrame(self.root, text="Connection Settings", padding="10")
        conn_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(conn_frame, text="IP Address:").grid(row=0, column=0, sticky="w", padx=5)
        self.ip_entry = ttk.Entry(conn_frame, width=15)
        self.ip_entry.insert(0, "192.168.41.99")
        self.ip_entry.grid(row=0, column=1, padx=5)

        ttk.Label(conn_frame, text="Port:").grid(row=0, column=2, sticky="w", padx=5)
        self.port_entry = ttk.Entry(conn_frame, width=8)
        self.port_entry.insert(0, "502")
        self.port_entry.grid(row=0, column=3, padx=5)

        self.connect_btn = ttk.Button(conn_frame, text="Connect", command=self.toggle_connection)
        self.connect_btn.grid(row=0, column=4, padx=10)

        self.status_label = ttk.Label(conn_frame, text="Disconnected", foreground="red")
        self.status_label.grid(row=0, column=5, padx=10)

        # Data frame
        data_frame = ttk.LabelFrame(self.root, text="Current Measurements", padding="10")
        data_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Treeview for data display
        self.columns = ("Address", "Name", "Description", "Value", "Unit")
        self.tree = ttk.Treeview(data_frame, columns=self.columns, show="headings", height=20)

        # Column widths
        column_widths = {
            "Address": 80,
            "Name": 80,
            "Description": 300,
            "Value": 100,
            "Unit": 60
        }

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths[col])

        # Column visibility state
        self.column_visible = {col: True for col in self.columns}

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
        self.refresh_entry.insert(0, "1000")
        self.refresh_entry.pack(side="left", padx=5)

        # Column visibility controls
        ttk.Label(control_frame, text="Show Columns:").pack(side="left", padx=(20, 5))
        self.column_vars = {}
        for col in self.columns:
            var = tk.BooleanVar(value=True)
            self.column_vars[col] = var
            cb = ttk.Checkbutton(control_frame, text=col, variable=var,
                               command=lambda c=col: self.toggle_column(c))
            cb.pack(side="left", padx=2)

    def setup_modbus_registers(self):
        self.registers = [
            (0x000, "I1", "Wartosc pradu I1", "A"),
            (0x002, "I2", "Wartosc pradu I2", "A"),
            (0x004, "I3", "Wartosc pradu I3", "A"),
            (0x006, "U12", "Wartosc napiecia U12", "V"),
            (0x008, "U23", "Wartosc napiecia U23", "V"),
            (0x00A, "U31", "Wartosc napiecia U31", "V"),
            (0x00C, "f", "Wartosc czestotliwosci", "Hz"),
            (0x00E, "P", "Wartosc mocy czynnej", "W"),
            (0x010, "Q", "Wartosc mocy biernej", "var"),
            (0x012, "S", "Wartosc mocy pozornej", "VA"),
            (0x014, "cos(fi)", "Wartosc cos(fi)", ""),
            (0x016, "tg(fi)", "Wartosc tg(fi)", ""),
            (0x018, "Ec+", "Licznik energii czynnej dodatniej", "Wh"),
            (0x01A, "Ec-", "Licznik energii czynnej ujemnej", "Wh"),
            (0x01C, "Eb+", "Licznik energii biernej dodatniej", "varh"),
            (0x01E, "Eb-", "Licznik energii biernej ujemnej", "varh"),
            (0x020, "I0", "Wartosc pradu I0", "A"),
            (0x022, "U0", "Wartosc napiecia U0", "V"),
            (0x024, "Y0", "Wartosc admitancji Y0", "S"),
            (0x026, "fi0", "Kat miedzy U0 a I0", "°"),
            (0x028, "Ig", "Wartosc pradu wew. baterii kondensatorow Ig", "A"),
            (0x02A, "I1_1h", "Wartosc I harmonicznej pradu I1", "A"),
            (0x02C, "I2_1h", "Wartosc I harmonicznej pradu I2", "A"),
            (0x02E, "I3_1h", "Wartosc I harmonicznej pradu I3", "A"),
            (0x030, "U1", "Wartosc napiecia U1", "V"),
            (0x032, "U2", "Wartosc napiecia U2", "V"),
            (0x034, "U3", "Wartosc napiecia U3", "V"),
            (0x036, "P1", "Wartosc mocy czynnej P1", "W"),
            (0x038, "P2", "Wartosc mocy czynnej P2", "W"),
            (0x03A, "P3", "Wartosc mocy czynnej P3", "W"),
            (0x03C, "Q1", "Wartosc mocy biernej Q1", "var"),
            (0x03E, "Q2", "Wartosc mocy biernej Q2", "var"),
            (0x040, "Q3", "Wartosc mocy biernej Q3", "var"),
            (0x042, "fi1", "Kat miedzy U1 a I1", "°"),
            (0x044, "fi2", "Kat miedzy U2 a I2", "°"),
            (0x046, "fi3", "Kat miedzy U3 a I3", "°"),
            (0x048, "fiU1_2", "Kat miedzy U1 a U2", "°"),
            (0x04A, "fiU1_3", "Kat miedzy U1 a U3", "°"),
            (0x04C, "I_s1", "Skladowa zgodna pradu", "A"),
            (0x04E, "I_s2", "Skladowa przeciwna pradu", "A"),
            (0x050, "U_s1", "Skladowa zgodna napiecia", "V"),
            (0x052, "U_s2", "Skladowa przeciwna napiecia", "V"),
        ]

        # Populate tree with register info
        for addr, name, desc, unit in self.registers:
            self.tree.insert("", "end", values=(f"0x{addr:03X}", name, desc, "---", unit))

    def toggle_column(self, column):
        """Toggle visibility of a column"""
        is_visible = self.column_vars[column].get()
        self.column_visible[column] = is_visible

        # Update displayed columns list
        visible_columns = [col for col in self.columns if self.column_visible[col]]
        self.tree.configure(displaycolumns=visible_columns)

    def get_column_width(self, column):
        """Get default width for a column"""
        widths = {
            "Address": 80,
            "Name": 80,
            "Description": 300,
            "Value": 100,
            "Unit": 60
        }
        return widths.get(column, 150)

    def toggle_connection(self):
        if not self.is_connected:
            self.connect_to_device()
        else:
            self.disconnect_from_device()

    def connect_to_device(self):
        try:
            ip = self.ip_entry.get().strip()
            port = int(self.port_entry.get().strip())

            self.client = ModbusTcpClient(ip, port=port)
            result = self.client.connect()

            if result:
                self.is_connected = True
                self.status_label.config(text="Connected", foreground="green")
                self.connect_btn.config(text="Disconnect")
                self.read_btn.config(state="normal")
                self.ip_entry.config(state="disabled")
                self.port_entry.config(state="disabled")
            else:
                messagebox.showerror("Error", "Failed to connect to device")

        except Exception as e:
            messagebox.showerror("Error", f"Connection error: {str(e)}")

    def disconnect_from_device(self):
        if self.reading_thread and self.reading_thread.is_alive():
            self.stop_reading = True
            self.reading_thread.join()

        if self.client:
            self.client.close()

        self.is_connected = False
        self.status_label.config(text="Disconnected", foreground="red")
        self.connect_btn.config(text="Connect")
        self.read_btn.config(text="Start Reading", state="disabled")
        self.ip_entry.config(state="normal")
        self.port_entry.config(state="normal")

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
            refresh_rate = 1.0

        while not self.stop_reading and self.is_connected:
            try:
                self.read_all_registers()
                time.sleep(refresh_rate)
            except Exception as e:
                error_msg = f"Reading error: {str(e)}"
                self.root.after(0, lambda msg=error_msg: messagebox.showerror("Error", msg))
                break

    def read_all_registers(self):
        if not self.client or not self.is_connected:
            return

        # Read all registers in one go (each float value uses 2 registers)
        total_registers = len(self.registers) * 2
        result = self.client.read_input_registers(address=0x0000, count=total_registers)

        if not hasattr(result, 'registers') or result.registers is None:
            raise Exception("Failed to read registers - no data received")
        if len(result.registers) < total_registers:
            raise Exception(f"Expected {total_registers} registers, got {len(result.registers)}")

        # Update GUI in main thread
        self.root.after(0, lambda: self.update_display(result.registers))

    def update_display(self, registers):
        for i, (addr, name, desc, unit) in enumerate(self.registers):
            try:
                # Each float value uses 2 registers
                reg_index = i * 2
                if reg_index + 1 < len(registers):
                    # Convert two 16-bit registers to IEEE-754 float
                    # Using Little Endian format as determined from testing
                    reg1 = registers[reg_index]
                    reg2 = registers[reg_index + 1]

                    # Pack as little endian and unpack as little endian float
                    raw_bytes = struct.pack('<HH', reg1, reg2)
                    float_value = struct.unpack('<f', raw_bytes)[0]

                    # Update tree item
                    item_id = self.tree.get_children()[i]
                    current_values = self.tree.item(item_id)['values']
                    new_values = (current_values[0], current_values[1], current_values[2], f"{float_value:.3f}", current_values[4])
                    self.tree.item(item_id, values=new_values)

            except Exception as e:
                print(f"Error updating register {name}: {e}")

    def on_closing(self):
        if self.is_connected:
            self.disconnect_from_device()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModbusGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()