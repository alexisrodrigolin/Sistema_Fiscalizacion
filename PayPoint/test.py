import mysql.connector
from mysql.connector import Error
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Configuración de la base de datos
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Taytay-0307",
    "database": "test"
}

def crear_tabla_e_indices():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        cursor = conexion.cursor()
        
        # Corregido tipo de dato VARCHAR
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                marca VARCHAR(255),
                descripcion TEXT,
                tipo_sabor VARCHAR(255),
                cantidad INT
            )
        """)
        
        # Verificar índices
        indices = [
            ('idx_marca', 'marca'),
            ('idx_descripcion', 'descripcion(255)'),
            ('idx_tipo_sabor', 'tipo_sabor'),
            ('idx_cantidad', 'cantidad')
        ]
        
        for nombre, columna in indices:
            cursor.execute(f"SHOW INDEX FROM productos WHERE Key_name = '{nombre}'")
            if not cursor.fetchone():
                cursor.execute(f"CREATE INDEX {nombre} ON productos ({columna})")
                
    except Error as e:
        messagebox.showerror("Error", f"Error en base de datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def buscar_productos(general_terms, cantidad):
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        cursor = conexion.cursor(dictionary=True)
        
        condiciones = []
        parametros = []
        
        # Búsqueda general
        terminos_limpios = [t.strip() for t in general_terms.split() if t.strip()]
        for termino in terminos_limpios:
            busqueda = f"%{termino}%"
            condiciones.append("(marca LIKE %s OR descripcion LIKE %s OR tipo_sabor LIKE %s)")
            parametros.extend([busqueda, busqueda, busqueda])
        
        # Búsqueda por cantidad
        if cantidad.strip():
            try:
                cantidad_int = int(cantidad)
                condiciones.append("cantidad = %s")
                parametros.append(cantidad_int)
            except ValueError:
                messagebox.showwarning("Error", "La cantidad debe ser un número entero")
                return []
        
        # Construir consulta
        query = "SELECT * FROM productos"
        if condiciones:
            query += " WHERE " + " AND ".join(condiciones)
        query += " LIMIT 100"
        
        cursor.execute(query, parametros)
        return cursor.fetchall()
        
    except Error as e:
        messagebox.showerror("Error", f"Error de búsqueda: {e}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

class BuscadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscador de Productos")
        self.root.geometry("800x600")
        
        self.style = ttk.Style(theme="cosmo")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Campo de búsqueda general
        ttk.Label(self.frame, text="Búsqueda General (marca, descripción, sabor):").pack(pady=5)
        self.entry_busqueda = ttk.Entry(self.frame, width=50)
        self.entry_busqueda.pack(pady=5)
        self.entry_busqueda.bind("<Return>", self.realizar_busqueda)
        
        # Campo para cantidad
        ttk.Label(self.frame, text="Cantidad exacta (Sin unidad):").pack(pady=5)
        self.entry_cantidad = ttk.Entry(self.frame, width=20)
        self.entry_cantidad.pack(pady=5)
        self.entry_cantidad.bind("<Return>", self.realizar_busqueda)
        
        # Botón de búsqueda
        self.btn_buscar = ttk.Button(
            self.frame, text="Buscar", command=self.realizar_busqueda, bootstyle=PRIMARY
        )
        self.btn_buscar.pack(pady=10)
        
        # Tabla de resultados
        self.tree = ttk.Treeview(
            self.frame, 
            columns=("Marca", "Descripción", "Tipo/Sabor", "Cantidad"), 
            show="headings",
            height=15
        )
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Tipo/Sabor", text="Tipo/Sabor")
        self.tree.heading("Cantidad", text="Cantidad (ml/gr)")
        self.tree.pack(fill=BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        crear_tabla_e_indices()
    
    def realizar_busqueda(self, event=None):
        terminos_general = self.entry_busqueda.get().strip()
        cantidad = self.entry_cantidad.get().strip()
        
        # Limpiar resultados
        self.tree.delete(*self.tree.get_children())
        
        resultados = buscar_productos(terminos_general, cantidad)
        
        if not resultados:
            messagebox.showinfo("Información", "No se encontraron coincidencias")
            return
        
        for producto in resultados:
            self.tree.insert("", END, values=(
                producto["marca"],
                producto["descripcion"],
                producto["tipo_sabor"],
                producto["cantidad"]
            ))

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")
    app = BuscadorApp(root)
    root.mainloop()