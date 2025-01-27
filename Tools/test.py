import tkinter as tk
from tkinter import ttk

def ajustar_escala(event):
    # Ajusta el escalado según el ancho de la ventana principal
    escala = event.width / 800  # Ajusta 800 según el diseño inicial
    root.tk.call('tk', 'scaling', escala)  # Escalado global en Tkinter

# Crear ventana principal
root = tk.Tk()
root.geometry("800x600")  # Tamaño inicial de referencia

# Crear algunos widgets
label = tk.Label(root, text="Texto dinámico", font=("Helvetica", 20))
label.pack(pady=20)

boton = ttk.Button(root, text="Soy un botón dinámico")
boton.pack(pady=10)

# Vincular evento de redimensionamiento
root.bind("<Configure>", ajustar_escala)

# Iniciar el bucle principal
root.mainloop()