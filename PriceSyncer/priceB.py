import mysql.connector as sql
import json
from mysql.connector import Error
class connection():
    def __init__(self):
        with open("PriceConfiguration.json", "r") as archivo:
            self.datos = json.load(archivo)
        self.font= float(self.datos['Font'])
    def Connection(self):
        self.mydb = sql.connect( 
        host=f"{self.datos['Db']}",
        user=f"{self.datos['User']}",
        password=f"{self.datos['Password']}",
        database= "TEST"
        )
        if not self.mydb.is_connected(): exit()
        self.cursor= self.mydb.cursor()   
        self.valid_users = {
            "1": "1",  }
  
    def search(self, codigo):
        instructionId= f"SELECT * FROM Art WHERE ID={codigo}"
        instructionPlu= f"SELECT * FROM Art WHERE PLU= {codigo}"
        instructionPlu2= f"SELECT * FROM Art WHERE PLU2= {codigo}"
        self.cursor.execute(instructionPlu)
        resultPlu= self.cursor.fetchall()
        self.cursor.execute(instructionId)       
        resultId= self.cursor.fetchall()
        self.cursor.execute(instructionPlu2)
        resultPlu2= self.cursor.fetchall()
        if resultId:
            return resultId
        elif resultPlu:
            return resultPlu
        elif resultPlu2:
            return resultPlu2
        else:
            instruction= f"INSERT INTO Art (PLU) VALUES('{codigo}')"
            self.cursor.execute(instruction)
            self.mydb.commit()

    def guardar(self, dic,id):
        net=''
        for clave, valor in dic.items():
            if valor =='NULL':
                net+= f"{clave} = {valor}, "
            else:
                net+= f"{clave} = '{valor}', "
        instruction = f'UPDATE Art SET {net[:-2]} WHERE id = {id}'
        self.cursor.execute(instruction)
        self.mydb.commit()
    def validate_user(self, username, password):
        return self.valid_users.get(username) == password

    def writeCfg(self):
        with open("PriceConfiguration.json","w") as archivo:
            json.dump(self.datos,archivo, indent=4)
    def buscar_productos(self,general_terms, cantidad):
        try:
           
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
                    # messagebox.showwarning("Error", "La cantidad debe ser un número entero")
                    return []
            
            # Construir consulta
            query = "SELECT * FROM art"
            if condiciones:
                query += " WHERE " + " AND ".join(condiciones)
            query += " LIMIT 100"
            
            self.cursor.execute(query, parametros)
            return self.cursor.fetchall()
            
        except Error as e:
            # messagebox.showerror("Error", f"Error de búsqueda: {e}")
            return []
        # finally:
        #     if conexion.is_connected():
        #         cursor.close()
        #         conexion.close()
