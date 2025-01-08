import tkinter as tk
import ttkbootstrap as tb   
import priceB 

class main():
    def __init__(self):
        self.Back= priceB.connection()
        self.app= tb.Window(themename= "darkly",title= "PriceSyncer",size= [1024, 768])

        self.create_widget_menu()
        self.settings(col=15, row=15)

        self.app.mainloop()
    def create_widget_menu(self):
        self.numberCaja= tb.Label(self.app, text="PriceSyncer", font=("helveica",35,"italic","bold"),anchor="center")

        self.User= tb.Entry(self.app, justify="center")
        self.Password= tb.Entry(self.app,justify="center", show="*")
        self.enter= tb.Button(self.app, text="Enter", command=self.check, style= "darkly")

        self.enter.grid(column=7,row=7)
        self.Password.grid(column=7, row=6,sticky= "n")
        self.User.grid(column=7, row=5)
        self.numberCaja.grid(column=7,  row=3)  
    def create_widget_precio(self):
        self.hide_menu()
        self.P_id= tb.Label(self.app, text= "ID:", font= ("helvetica", 20), )
        self.P_id_value= tb.Entry(self.app, style= "darkly",width=15)
        self.P_plu= tb.Label(self.app, text= "PLU:", font= ("helvetica", 20))
        self.P_plu_value= tb.Entry(self.app, style= "darkly",width=15)
        self.P_precio= tb.Label(self.app, text= "Precio:", font= ("helvetica", 20))
        self.P_precio_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20))
        self.P_marca= tb.Label(self.app, text= "Marca:", font= ("helvetica", 20))
        self.P_marca_value= tb.Entry(self.app, style= "darkly", width=15, font= ("helvetica", 20),)
        self.P_descripcion= tb.Label(self.app, text= "Descripcion:", font= ("helvetica", 20))
        self.P_descripcion_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=21)
        self.P_tipo= tb.Label(self.app, text= "Tipo/Sabor:", font= ("helvetica", 20))
        self.P_tipo_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=20)
        self.P_cantidad= tb.Label(self.app, text= "Cantidad:", font= ("helvetica", 20))
        self.P_cantidad_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=7)
        barras=tb.Label(self.app, text="////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        barras1=tb.Label(self.app, text="////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        barras2=tb.Label(self.app, text="////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

        self.P_departamento= tb.Label(self.app, text= "Deepartamento:", font= ("helvetica", 20))
        self.P_departamento_value= tb.Entry(self.app, style= "darkly", width=14, font= ("helvetica", 20))
        self.P_pasillo= tb.Label(self.app, text= "Pasillo:", font= ("helvetica", 20))
        self.P_pasillo_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=14)
        self.P_costo= tb.Label(self.app, text= "Costo s.IVA:", font= ("helvetica", 20))
        self.P_costo_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=7)
        self.P_iva= tb.Label(self.app, text= "IVA:", font= ("helvetica", 20))
        self.P_iva_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=7)
        self.P_ganancia= tb.Label(self.app, text= "Ganancia %:", font= ("helvetica", 20))
        self.P_ganancia_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=7)
        self.P_preReco= tb.Label(self.app, text= f"Precio recomendado \n para venta: $",font= ("helvetica", 20), foreground="#B6B6B6")

        self.P_preCan= tb.Label(self.app, text= f"<<<Precio por Cantidad>>>",font= ("helvetica", 20), )
        self.P_cantidad1= tb.Label(self.app, text= "Cantidad 1:", font= ("helvetica", 20))
        self.P_cantidad1_value= tb.Entry(self.app, style= "darkly", width=7, font= ("helvetica", 20))
        self.P_cantidad2= tb.Label(self.app, text= "Canridad 2:", font= ("helvetica", 20))
        self.P_cantidad2_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=7)
        self.P_cantidad3= tb.Label(self.app, text= "Cantidad 3:", font= ("helvetica", 20))
        self.P_cantidad3_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=7)
        self.P_precioC1= tb.Label(self.app, text= "Precio x Uni:", font= ("helvetica", 20))
        self.P_precioC1_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=7)
        self.P_precioC2= tb.Label(self.app, text= "Precio x Uni:", font= ("helvetica", 20))
        self.P_precioC2_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=7)
        self.P_precioC3= tb.Label(self.app, text= "Precio x Uni:", font= ("helvetica", 20))
        self.P_precioC3_value= tb.Entry(self.app, style= "darkly", font= ("helvetica", 20),width=7)

        self.P_guardar= tb.Button(self.app, text="Guardar sin emitir", bootstyle="warning-outline")
        self.P_guardarSin= tb.Button(self.app, text="Guadar y emitir", bootstyle="warning-outline")
        self.P_borrar= tb.Button(self.app, text="Borrar", bootstyle="warning-outline")
        self.P_menu= tb.Button(self.app, text="Menu", bootstyle="warning-outline")
        self.P_borrarOf= tb.Button(self.app, text="Borrar Oferta", bootstyle="warning-link")
        self.P_buscar= tb.Button(self.app, text="Buscar", bootstyle="warning-outline")
        self.P_fecha= tb.Label(self.app, text="Fecha de Modificacion:", font= ("helvetica", 20), foreground="#7B7A7A" )

#row 1
        self.P_id.place(relx=0.05, rely=0.07)
        self.P_id_value.place(relx=0.14,rely=0.07)
        self.P_plu.place(relx=0.05, rely=0.12)
        self.P_plu_value.place(relx=0.14, rely=0.12)
        self.P_precio.place(relx=0.47,rely= 0.087)
        self.P_precio_value.place(relx=0.55,rely=0.087)
        self.P_marca.place(relx=0.0156, rely=0.23)
        self.P_marca_value.place(relx=0.0156, rely=0.27) 
        self.P_descripcion.place(relx=0.24,rely= 0.23)
        self.P_descripcion_value.place(relx= 0.24, rely=0.27)      
        self.P_tipo.place(relx=0.52, rely=0.23)
        self.P_tipo_value.place(relx=0.52, rely=0.27) 
        self.P_cantidad.place(relx=0.7871,rely= 0.23)
        self.P_cantidad_value.place(relx= 0.7871, rely=0.27)  
        barras.place(relx=0, rely=0.3411)
        self.P_departamento.place(relx= 0.0156, rely=0.3906)
        self.P_departamento_value.place(relx= 0.163, rely=0.3906)
        self.P_pasillo.place(relx=0.0156, rely=0.45)
        self.P_pasillo_value.place(relx=0.163, rely= 0.45)
        self.P_costo.place(relx= 0.36, rely=0.3906)
        self.P_costo_value.place(relx= 0.4785, rely=0.3906)
        self.P_iva.place(relx= 0.36, rely=0.45)
        self.P_iva_value.place(relx= 0.4785, rely=0.45)
        self.P_ganancia.place(relx=0.6025, rely=0.3906)
        self.P_ganancia_value.place(relx=0.739 , rely=0.3906)
        self.P_preReco.place(relx=0.6816, rely=0.4557)
        barras1.place(relx=0, rely=0.5287)
        self.P_preCan.place(relx= 0.0273, rely= 0.5664)
        self.P_cantidad1.place(relx=0.0156, rely=0.63)
        self.P_cantidad1_value.place(relx=0.135, rely=0.63)
        self.P_cantidad2.place(relx=0.3369, rely=0.63)
        self.P_cantidad2_value.place(relx=0.455, rely=0.63)
        self.P_cantidad3.place(relx=0.6719, rely=0.63)
        self.P_cantidad3_value.place(relx=0.79, rely=0.63)
        self.P_precioC1.place(relx=0.0156, rely=0.6914)
        self.P_precioC1_value.place(relx=0.135, rely=0.6914)
        self.P_precioC2.place(relx=0.3369, rely=0.6914)
        self.P_precioC2_value.place(relx=0.455, rely=0.6914)
        self.P_precioC3.place(relx=0.6719, rely=0.6914)
        self.P_precioC3_value.place(relx=0.79, rely=0.6914)
        barras2.place(relx=0, rely=0.7917)

        self.P_guardar.place(relx= 0.0283, rely=0.872)
        self.P_guardarSin.place(relx=0.2246,rely=0.872)
        self.P_borrar.place(relx=0.3984,rely=0.872)
        self.P_menu.place(relx=0.50,rely=0.872)
        self.P_borrarOf.place(relx=0.837,rely=0.5664)
        self.P_buscar.place(relx=0.874,rely=0.0911)
        self.P_fecha.place(relx=0.6426,rely=0.872)

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
            
        
            self.etiquetas.grid(column=7, row=11, )
            self.precio.grid(column=7,row=10, )
            try:
                self.error.grid_forget()
            except:
                pass
        else: 
            self.error= tb.Label(self.app,  
            text= "Usuario o Contraseña incorrecta", 
            style= "darkly",
            foreground= "red" )
            self.error.grid(column=7, row=6, sticky= "s")
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
        