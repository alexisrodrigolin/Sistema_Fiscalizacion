import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",       # Cambia por tu host si es necesario
    user="root",      # Cambia por tu usuario de MySQL
    password="", # Cambia por tu contraseña
    database="TEST" # Cambia por tu base de datos
)
cursor = conn.cursor()
# Crear tabla con 100 columnas VARCHAR(40)
# Nombre de la tabla: productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Facturado (
    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Subtotal` VARCHAR(10), `Hora` TIME, `Continue` TINYINT,
    """ + ", ".join([f"item_{i} VARCHAR(40)" for i in range(1, 101)]) + """)""")


conn.commit()

print("Se crearon las 1000 filas con 100 columnas, todas con valores NULL.")

# Cerrar conexión
cursor.close()
conn.close()