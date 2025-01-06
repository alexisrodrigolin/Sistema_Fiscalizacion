import tkinter as tk
import ttkbootstrap as tb   
import priceB 

class main():
    def __init__(self):
        self.Back= priceB.connection()
        self.app= tb.Window(themename= "darkly",title= "PriceSyncer",size= [1024, 768])

        self.create_widget_menu()
        self.columnas_rows(col=8, row=15)
        self.app.mainloop()
    def create_widget_menu(self):
        self.numberCaja= tb.Label(self.app, text="PriceSyncer", font=("helveica",35,"italic","bold"),anchor="center")

        self.User= tb.Entry(self.app, justify="center")
        self.Password= tb.Entry(self.app,justify="center", show="*")
        self.enter= tb.Button(self.app, text="Enter", command=self.check, style= "darkly")

        self.enter.grid(column=3,row=7)
        self.Password.grid(column=3, row=6,sticky= "n")
        self.User.grid(column=3, row=5)
        self.numberCaja.grid(column=3,  row=3)  
    def check(self, event=None):
        username = self.User.get()  
        password= self.Password.get()
        if self.Back.validate_user(username,password):
            self.pay= tb.Button(self.app,
            text="PayPoint", )
            self.sales= tb.Button(self.app,
            text = "SalesOverview", )
            
        
            self.sales.grid(column=3, row=11)
            self.pay.grid(column=3,row=10)
            try:
                self.error.grid_forget()
            except:
                pass
        else: 
            self.error= tb.Label(self.app, 
            text= "Usuario o Contraseña incorrecta", 
            style= "darkly",
            foreground= "red" )
            self.error.grid(column=3, row=6, sticky= "s")
            try:
                self.pay.grid_forget()
                self.sales.grid_forget()
            except:
                pass

    def columnas_rows(self, col, row):
        "columnas y rows asignados"

        for i in range(col):
            self.app.columnconfigure(i,weight= 1)
            
        for z in range(row):
            self.app.rowconfigure(z,weight=1)

        

        self.enter.grid(column=3,row=7)
        self.Password.grid(column=3, row=6,sticky= "n")
        self.User.grid(column=3, row=5)
        self.numberCaja.grid(column=3,  row=3)   
main()
        