import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

def mostrar_error():
    Messagebox.show_error(
        title="Error",
        message="¡Ocurrió un error crítico!",
        
    )

# Ventana principal
raiz = ttk.Window(themename="superhero")
boton = ttk.Button(raiz, text="Mostrar Error", command=mostrar_error)
boton.pack(pady=50, padx=50)

raiz.geometry("400x200")
raiz.mainloop()