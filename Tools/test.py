import tkinter as tk

class MiAplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry("800x600")

        # Botón para abrir el "widget modal"
        tk.Button(self.root, text="Abrir Modal", command=self.mostrar_modal).pack(pady=20)

    def mostrar_modal(self):
        # Crear un Frame que cubra toda la ventana principal
        overlay = tk.Frame(self.root, bg="black")
        overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Desactivar la interacción con los widgets debajo del overlay
        overlay.grab_set()

        # Crear el "contenido" de la ventana modal en el centro del overlay
        modal = tk.Frame(overlay, bg="white", padx=20, pady=20)
        modal.place(relx=0.5, rely=0.5, anchor="center")

        # Contenido del modal
        tk.Label(modal, text="Este es un modal", bg="white").pack(pady=10)
        tk.Button(modal, text="Cerrar", command=overlay.destroy).pack()

root = tk.Tk()
app = MiAplicacion(root)
root.mainloop()