import tkinter as tk
from tkinter import ttk

def submit():
    # Recolectar los datos de los campos
    data = {param: entries[param].get() for param in params}
    print("Datos ingresados:", data)
    # Aquí podrías agregar lógica para procesar o guardar los datos

# Lista de parámetros de la imagen
params = [
    "ID", "Marca", "Descripcion", "Tipo_Sabor", "PLU", "IVA", "Costo", "Precio", 
    "Departamento", "Pasillo", "Fecha_de_modificacion", "Cantidad", "Tipo_de_cantidad"
]

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Parámetros")
root.geometry("500x600")  # Ajustar el tamaño de la ventana
root.configure(bg="#f5f5f5")

# Crear un frame para los campos de entrada
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

entries = {}

# Crear un título
title_label = tk.Label(root, text="Formulario de Parámetros", font=("Arial", 16), bg="#f5f5f5", fg="#333")
title_label.grid(row=0, column=0, pady=10)

# Crear etiquetas y campos de entrada dinámicamente
for idx, param in enumerate(params):
    label = tk.Label(frame, text=param, font=("Arial", 12), bg="#f5f5f5", fg="#555")
    label.grid(row=idx, column=0, sticky=tk.W, pady=5, padx=5)
    
    entry = ttk.Entry(frame, width=40)
    entry.grid(row=idx, column=1, pady=5, padx=5)
    entries[param] = entry

# Botón para enviar los datos
submit_button = tk.Button(root, text="Enviar", command=submit, bg="#007BFF", fg="white", font=("Arial", 12), padx=10, pady=5, borderwidth=0, activebackground="#0056b3")
submit_button.grid(row=2, column=0, pady=20)

# Iniciar el loop de la aplicación
root.mainloop()