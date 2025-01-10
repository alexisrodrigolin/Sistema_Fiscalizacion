import ttkbootstrap as ttk

def mostrar_seleccion():
    print(f"Opción seleccionada: {selected_option.get()}")

# Crear la aplicación
root = ttk.Window(themename="cosmo")

# Crear una variable para rastrear la opción seleccionada
selected_option = ttk.StringVar(value="Opción 1")

# Crear el Menubutton
menubutton = ttk.Menubutton(root, text="Menú", width=15)
menubutton.grid(row=0, column=0)

# Crear un menú para el Menubutton
menu = ttk.Menu(menubutton)
menu.add_radiobutton(label="Opción 1", variable=selected_option, value="Opción 1")
menu.add_radiobutton(label="Opción 2", variable=selected_option, value="Opción 2")
menu.add_radiobutton(label="Opción 3", variable=selected_option, value="Opción 3")
menubutton["menu"] = menu

# Botón para mostrar la opción seleccionada
btn_mostrar = ttk.Button(root, text="Mostrar selección", command=mostrar_seleccion)
btn_mostrar.grid(row=1, column=0)

# Iniciar la aplicación
root.mainloop()