import mysql.connector as sql

class connection():
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
            
    def validate_user(self, username, password):
        return self.valid_users.get(username) == password
    