import mysql.connector as sql

class connection():
    def __init__(self):
        self.mydb = sql.connect( 
        host="127.0.0.1",
        user="root",
        password="Taytay8888",
        database= "test01"
        )
        self.valid_users = {
            "1": "1",  # username: password
            
        }

   #     self.new() 
    def new(self):
        instruction= "INSERT INTO new_table (Descripcion, PLU, Precio, Fecha_de_modificacion ) VALUES('Coca', '77932221', '23.0', '2025-01-06')"
        cursor=self.mydb.cursor()
        cursor.execute(instruction)

        self.mydb.commit()
    def validate_user(self, username, password):
        return self.valid_users.get(username) == password
    

connection()