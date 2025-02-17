import tkinter as tk
import ttkbootstrap as tb

root = tb.Window(themename="darkly")

# Frame principal
main_frame = tb.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Canvas para permitir desplazamiento
canvas = tk.Canvas(main_frame)
scrollbar = tb.Scrollbar(main_frame, orient="vertical", command=canvas.yview)

# Frame interno dentro del canvas
scrollable_frame = tb.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Frame para organizar Checkbuttons y Treeview
content_frame = tb.Frame(scrollable_frame)
content_frame.pack(fill="both", expand=True)

# Frame para Checkbuttons (lado izquierdo)
check_frame = tb.Frame(content_frame)
check_frame.grid(row=0, column=0, sticky="nw", padx=5)

# Treeview (lado derecho)
tree =tb.Treeview(content_frame, columns=("data",), show="tree", height=0)
tree.heading("data", text="Datos")
tree.column("data", width=150, anchor="center")
tree.grid(row=0, column=1, sticky="nw", padx=5)

# Diccionario para almacenar Checkbuttons vinculados con filas del Treeview
check_dict = {}

# Función para actualizar selección en el Treeview
def actualizar_treeview():
    for item_id, vars_list in check_dict.items():
        if any(var.get() for var in vars_list):  # Si al menos un Checkbutton está activado
            tree.item(item_id, tags=("seleccionado",))
        else:
            tree.item(item_id, tags=())

# Configurar color de filas seleccionadas
tree.tag_configure("seleccionado", background="lightblue")

# Función para agregar filas dinámicamente
def agregar_fila():
    fila_id = len(check_dict)  # Número de fila actual

    # Insertar fila en Treeview y guardar su ID
    item_id = tree.insert("", "end", values=(f"Dato fila {fila_id+1}",))
    tree["height"] = fila_id + 1  # Ajustar la altura del Treeview

    # Crear un Frame para la nueva fila de Checkbuttons y ubicarlo en una fila nueva
    row_frame = tb.Frame(check_frame)
    row_frame.grid(row=fila_id, column=0, sticky="w")  # Cada grupo de Checkbuttons en una fila nueva

    # Crear 4 Checkbuttons dentro de la fila
    row_vars = []
    for j in range(4):
        var = tk.BooleanVar()
        row_vars.append(var)
        chk = tb.Checkbutton(row_frame, text=f"Opción {j+1}", variable=var, command=actualizar_treeview)
        chk.pack(side="left", padx=5)

    # Asociar Checkbuttons con la fila en el Treeview
    check_dict[item_id] = row_vars

    # Actualizar scrollbar
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

# Botón para agregar filas dinámicamente
btn_agregar = tb.Button(root, text="Agregar Fila", command=agregar_fila)
btn_agregar.pack(pady=5)

# Empaquetar el canvas y el scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
