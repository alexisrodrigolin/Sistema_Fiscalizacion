import tkinter as tk

def verificar_y_agregar_simbolo(event):
    entry = event.widget  # Obtener el widget que generó el evento
    contenido = entry.get().strip()  # Obtener el contenido y eliminar espacios extra

    # Verificar si el contenido ya tiene el símbolo "$"
    if contenido.startswith("$ "):
        # Validar que lo que sigue después del "$ " sea un número válido
        numero = contenido[2:]  # Quitar "$ "
        if numero.isdigit() or (numero.replace(".", "", 1).isdigit() and numero.count(".") < 2):
            return  # Todo está correcto, no se hace nada
        else:
            entry.delete(0, tk.END)  # Si no es un número válido, limpiar
            return

    # Verificar si es un número válido (sin "$ ")
    if contenido.isdigit() or (contenido.replace(".", "", 1).isdigit() and contenido.count(".") < 2):
        # Agregar el "$ " al inicio
        entry.delete(0, tk.END)
        entry.insert(0, f"$ {contenido}")
    else:
        # Si no es un número válido, limpiar el Entry
        entry.delete(0, tk.END)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Validación de Entrada")

# Crear el Entry y vincular el evento <FocusOut>
entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack(padx=20, pady=20)
entry.bind("<FocusOut>", verificar_y_agregar_simbolo)

# Iniciar el bucle principal de la aplicación
root.mainloop()