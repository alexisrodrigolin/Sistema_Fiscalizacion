import mysql.connector as sql
from datetime import date
import json
from mysql.connector import Error
import os
import sys

class connection():
    def __init__(self):
        # Get the base path for configuration files
        local_dir = os.path.join(os.getenv("LOCALAPPDATA"), "RSystems")
        os.makedirs(local_dir, exist_ok=True)  # Crear la carpeta si no existe

        # Ruta del archivo de configuración
        config_path = os.path.join(local_dir, "Configuration.json")

        # Si no existe el archivo, crearlo con valores por defecto
        if not os.path.exists(config_path):
            default_config = {
                "Db": "localhost",
                "User": "root",
                "Password": "",
                "Font": "0.8",
                "Com": "3",
                "Baudrate": "9600",
                "AdminPass": "888888",
                "EntryPass": "1",
                "SuperPass": "0",
                "Printer": "",
                "Supabase_url": "",
                "Supabase_key": ""
            }
            with open(config_path, "w") as f:
                json.dump(default_config, f, indent=4)
            print(f"Archivo de configuración creado en: {config_path}")
        else:
            print(f"Archivo de configuración encontrado en: {config_path}")

        # Cargar la configuración
        with open(config_path, "r") as archivo:
            self.datos = json.load(archivo)
        self.font = float(self.datos['Font'])
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
        self.etiR=[]
        self.etiO=[]
        self.bridge="PLU, PLU2, Precio, Marca, Descripcion, Tipo_Sabor, Cantidad, Unidad,Pasillo,Costo,IVA,Ganancia, Cant1, Precio1, Cant2, Precio2, Cant3, Precio3, Fecha_de_Modificacion"
    def search(self, codigo,status=0):
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
        elif status==0:
            instruction= f"INSERT INTO Art (PLU, Precio,Fecha_de_modificacion) VALUES('{codigo}','0','{date.today()}')"
            self.cursor.execute(instruction)
            self.mydb.commit()
    def delete(self, id):
            self.cursor.execute(f"DELETE FROM art WHERE id={id}")
            self.mydb.commit()
    def guardar(self, dic,id, status=0):

        net=''
        for clave, valor in dic.items():
            if valor =='NULL':
                net+= f"{clave} = {valor}, "
            else:
                net+= f"{clave} = '{valor}', "
        instruction = f'UPDATE Art SET {net[:-2]} WHERE id = {id}'
        self.cursor.execute(instruction)
        self.mydb.commit()
        if status==1:
            instructionEti=f"REPLACE INTO etiq({self.bridge}) Select {self.bridge} From Art Where id={id}"
            instructionSEti=f"REPLACE INTO Setiq({self.bridge}) Select {self.bridge} From Art Where id={id}"
            self.cursor.execute(f"SELECT Cant1, Cant2, Cant3 FROM Art WHERE id={id}")
            result=self.cursor.fetchall()
            if (not result) or all(r[0] is None for r in result):
                self.cursor.execute(instructionEti)
                self.mydb.commit()
            else: 
                self.cursor.execute(instructionSEti)
                self.mydb.commit()
        elif status==0:
            self.cursor.execute(f"DELETE FROM etiq WHERE id={id}")
            self.cursor.execute(f"DELETE FROM Setiq WHERE id={id}")
            self.mydb.commit()
    def validate_user(self, username, password):
        return self.valid_users.get(username) == password

    def writeCfg(self):
        # Get the base path for configuration files
        local_dir = os.path.join(os.getenv("LOCALAPPDATA"), "RSystems")
        config_path = os.path.join(local_dir, "Configuration.json")
        
        with open(config_path, "w") as archivo:
            json.dump(self.datos, archivo, indent=4)
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
    
    def etiquetasSearch(self,instruc):
        instruction="Select * From etiq LIMIT 1000"
        instruction1= "Select * From Setiq LIMIT 1000"
        borrar_Instruction="TRUNCATE TABLE etiq"
        borrar1_Instruction="TRUNCATE TABLE Setiq"
        if instruc==1:
            self.cursor.execute(instruction)
            result= self.cursor.fetchall()
            return result
        elif instruc==2:
            self.cursor.execute(instruction1)
            result= self.cursor.fetchall()
            return result
        elif instruc==3:
            self.cursor.execute(borrar_Instruction)
            self.mydb.commit()
            return
        elif instruc==4:
            self.cursor.execute(borrar1_Instruction)
            self.mydb.commit()
            return
    