import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.geometry("300x200")

# Crear el DateEntry
cal = DateEntry(root, date_pattern="yyyy-mm-dd")
cal.pack(pady=50)

# Cambiar el fondo del Entry interno y del calendario
#cal._entry.configure(background="lightblue")  # Fondo del campo de entrada
cal._top_cal.configure(background="lightblue")  # Fondo del calendario

root.mainloop()