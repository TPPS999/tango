Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)

' Try different Python commands silently
On Error Resume Next

' Try py -3.11 first
WshShell.Run "py -3.11 dual_modbus_gui_prod.py", 0, False
If Err.Number = 0 Then
    WScript.Quit
End If

Err.Clear

' Try python
WshShell.Run "python dual_modbus_gui_prod.py", 0, False
If Err.Number = 0 Then
    WScript.Quit
End If

Err.Clear

' Try py
WshShell.Run "py dual_modbus_gui_prod.py", 0, False
If Err.Number = 0 Then
    WScript.Quit
End If

' If all failed, show error
MsgBox "ERROR: Cannot launch e2tango GUI. Python not found or application failed to start.", vbCritical, "e2tango Modbus GUI"