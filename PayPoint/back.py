import mysql.connector as sql
class Logic:
    def __init__(self):
        self.mydb = sql.connect( 
        host="127.0.0.1",
        user="root",
        password="",
        database= "TEST"
        )
        self.cursor= self.mydb.cursor()   
        self.valid_users = {
            "1": "1",  
        }
        self.subtotal= 0.00
        self.cant=0
        self.tique=[]
    
    def suma(self,Descripcion='',Plu='',Precio= 0,Cantidad=0 , refresh= 0):
        if refresh ==1:
            self.subtotal=0.00
            self.cant=0
        else:
            self.subtotal+= Precio
            self.cant+= Cantidad
            item=(Descripcion,Precio,Plu,Cantidad)
            self.tique.append(item)

    def validate_user(self, username, password):
        return self.valid_users.get(username) == password
        
    def item(self,PLU):
        instruction= f'SELECT Marca, Descripcion, Tipo_Sabor, Cantidad, Unidad, Precio FROM Art WHERE PLU= {PLU}'
        instruction2= f'SELECT Marca, Descripcion, Tipo_Sabor, Cantidad, Unidad, Precio FROM Art WHERE PLU2= {PLU}'
        self.cursor.execute(instruction)
        result= self.cursor.fetchone()
        self.cursor.execute(instruction2)
        result2=self.cursor.fetchone()
        if result:
            return result
        elif result2:
            return result2
        else:
            return 0
    def table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        """ + ", ".join([f"item_{i} VARCHAR(40)" for i in range(1, 101)]) + """)""")
        self.mydb.commit()