import tkinter as tk
import ttkbootstrap as tb   
import priceB 

class main():
    def __init__(self):
        self.Back= priceB.connection()
        self.app= tb.Window(themename= "darkly",title= "PriceSyncer",size= [1024, 768])

        self.create_widget_menu()
        self.settings(col=20, row=20)

        self.app.mainloop()
    def create_widget_menu(self):
        self.numberCaja= tb.Label(self.app, text="PriceSyncer", font=("helveica",35,"italic","bold"),anchor="center")

        self.User= tb.Entry(self.app, justify="center")
        self.Password= tb.Entry(self.app,justify="center", show="*")
        self.enter= tb.Button(self.app, text="Enter", command=self.check, style= "darkly")

        self.enter.grid(column=9,row=10)
        self.Password.grid(column=9, row=9,sticky= "n")
        self.User.grid(column=9, row=8)
        self.numberCaja.grid(column=9,  row=6)  
    def create_widget_precio(self):
        self.hide_menu()
        self.P_id= tb.Label(self.app, text= "ID:", font= ("helvetica", 20))
        self.P_id_value= tb.Entry(self.app, style= "darkly")
        self.P_plu= tb.Label(self.app, text= "PLU:", font= ("helvetica", 20))
        self.P_plu_value= tb.Entry(self.app, style= "darkly")
        self.P_precio= tb.Label(self.app, text= "Precio:", font= ("helvetica", 20))
        self.P_precio_value= tb.Entry(self.app, style= "darkly")
        self.P_marca= tb.Label(self.app, text= "Marca:", font= ("helvetica", 20))
        self.P_marca_value= tb.Entry(self.app, style= "darkly", width=20, font= ("helvetica", 20))
        self.P_descripcion= tb.Label(self.app, text= "Descripcion:", font= ("helvetica", 20))
        self.P_descripcion_value= tb.Entry(self.app, style= "darkly")
        self.P_tipo= tb.Label(self.app, text= "Marca:", font= ("helvetica", 20))
        self.P_tipo_value= tb.Entry(self.app, style= "darkly")
        self.P_cantidad= tb.Label(self.app, text= "Descripcion:", font= ("helvetica", 20))
        self.P_cantidad_value= tb.Entry(self.app, style= "darkly")
#row 1
        self.P_id.grid(column= 1, row= 1, sticky= 'w')
        self.P_id_value.grid(column=2, row=1, sticky= 'w')
        self.P_plu.grid(column= 1, row= 2, sticky='nw')
        self.P_plu_value.grid(column= 2, row= 2, sticky= 'wn')
        self.P_precio.grid(column=8, row= 1, sticky= 's')
        self.P_precio_value.grid(column=9, row=1, sticky= "s")
#row 2
        self.P_marca.grid(column=0,columnspan=2, row=3, sticky='wse', padx= 15)
        self.P_marca_value.grid(column=0, columnspan=2, row=4, sticky='w', padx= 15)
        self.P_descripcion.grid(column= 2 , row= 3, sticky='ws')
        self.P_descripcion_value.grid(column=2, row=4, sticky='w')
 #       self.P_plu.grid(column= 1, row= 2, sticky='nw')
  #      self.P_plu_value.grid(column= 2, row= 2, sticky= 'wn')
   #     self.P_precio.grid(column=8, row= 1, sticky= 's')
    #    self.P_precio_value.grid(column=9, row=1, sticky= "s")

    def hide_menu(self):
            widgets_to_hide= [self.precio, self.etiquetas, self.numberCaja, self.User, self.Password,self.enter]
            for widget in widgets_to_hide:
                widget.grid_forget()        

    def check(self, event=None):
        username = self.User.get()  
        password= self.Password.get()
        if self.Back.validate_user(username,password):
            self.precio= tb.Button(self.app,
            text="Precio", style= "darkly",command=self.create_widget_precio)
            self.etiquetas= tb.Button(self.app,
            text = "etiquetas", style= "darkly")
            
        
            self.etiquetas.grid(column=9, row=14, )
            self.precio.grid(column=9,row=13, )
            try:
                self.error.grid_forget()
            except:
                pass
        else: 
            self.error= tb.Label(self.app,  
            text= "Usuario o Contraseña incorrecta", 
            style= "darkly",
            foreground= "red" )
            self.error.grid(column=9, row=9, sticky= "s")
            try:
                self.precio.grid_forget()
                self.etiquetas.grid_forget()
            except:
                pass

    def settings(self, col, row):
        "columnas y rows asignados"
        self.app.bind("<Return>", self.check)

        for i in range(col):
            self.app.columnconfigure(i,weight= 1)
            
        for z in range(row):
            self.app.rowconfigure(z,weight=1)



        

main()
        