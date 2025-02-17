import tkinter as tk
import ttkbootstrap as ttk

root = ttk.Window(themename="darkly")

# Frame principal
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Canvas para el scrollbar
canvas = tk.Canvas(main_frame)
scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)

# Frame interno dentro del canvas
scrollable_frame = ttk.Frame(canvas)

# Configurar el frame interno dentro del canvas
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Crear un window dentro del canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Frame para organizar Checkbuttons y Treeview
content_frame = ttk.Frame(scrollable_frame)
content_frame.pack(fill="both", expand=True)

# Frame para Checkbuttons (lado izquierdo)
check_frame = ttk.Frame(content_frame)
check_frame.pack(side="left", fill="y", padx=5)

# Crear Checkbuttons en filas de 4 columnas
check_vars = []  # Lista para almacenar variables de Checkbuttons
num_filas = 5  # 5 filas de Checkbuttons (total 5x4 = 20 opciones)
num_columnas = 4  # 4 Checkbuttons por fila

for i in range(num_filas):
    row_frame = ttk.Frame(check_frame)
    row_frame.pack(fill="x", pady=2)
    row_vars = []
    for j in range(num_columnas):
        var = tk.BooleanVar()
        row_vars.append(var)
        chk = ttk.Checkbutton(row_frame, text=f"Opción {i*num_columnas + j + 1}", variable=var)
        chk.pack(side="left", padx=5)
    check_vars.append(row_vars)

# Treeview (lado derecho)
tree = ttk.Treeview(content_frame, columns=("data",), show="headings", height=num_filas)
tree.heading("data", text="Datos")
tree.column("data", width=150, anchor="center")
tree.pack(side="left", padx=5, fill="y")

# Insertar filas en el Treeview (una por cada fila de Checkbuttons)
for i in range(num_filas):
    tree.insert("", "end", values=(f"Dato fila {i+1}",))

# Empaquetar el canvas y el scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
