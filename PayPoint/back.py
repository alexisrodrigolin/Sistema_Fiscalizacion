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
            "1": "1",  # username: password
            
        }
        self.subtotal= 0.00
    def suma(self,precio):
        self.subtotal+= precio
        
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
        