import mysql.connector as sql

class connection():
    def __init__(self):
        self.mydb = sql.connect( 
        host="127.0.0.1",
        user="root",
        password="Taytay8888",
        database= "test01"
        )
        self.cursor= self.mydb.cursor()   
        self.valid_users = {
            "1": "1",  # username: password
            
        }
        self.search(77)
    def search(self, codigo):
        
        instructionId= f"SELECT * FROM Art WHERE ID={codigo}"
        instructionPlu= f"SELECT * FROM Art WHERE PLU= {codigo}"
  
        self.cursor.execute(instructionPlu)
        resultPlu= self.cursor.fetchall()
        self.cursor.execute(instructionId)       
        resultId= self.cursor.fetchall()
        if resultId:
            print(resultId)
            return resultId
        elif resultPlu:
            print(resultPlu)
            return resultPlu
        else:
            self.create(codigo=codigo)
    def create(self,codigo):
        instruction= f"INSERT INTO Art (PLU) VALUES('{codigo}')"
        self.cursor.execute(instruction)
        self.mydb.commit()
        
    def validate_user(self, username, password):
        return self.valid_users.get(username) == password
    

connection()