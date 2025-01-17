import tkinter as tk
import ttkbootstrap as tb 
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import back

class caja():

    def __init__(self, *args, **kwargs):


        self.Bend= back.Logic()
        self.app = tb.Window(title = "PayPoint",size= [1024, 768] )
        self.app.config(background= '#F1EAD7')
        self.app.state('zoomed')
        self.style = tb.Style()
        self.style.configure("Custom.TButton", 
                             background="#F1EAD7",
                             bordercolor="black" ,
                             foreground="black", 
                             font=("Helvetica", 20), 
                             borderwidth=2,
                             relief="solid",

)
        self.style.map(
            "Custom.TButton",
            background=[("active", "#F1EAD7")], 
            bordercolor=[("focus", "black")],  
        )
        self.style.configure(
            "Custom.Treeview",
            background="#F1EAD7",  
            fieldbackground="#F1EAD7",  
            foreground="black",  
            borderwidth=0,  
            font=("Helvetica", 17 ),
            )
        self.style.configure(
            "Custom.Treeview.Heading",
            background="#F1EAD7",  
            foreground="black",  
            font=("Helvetica", 19, "bold"),
        )
        self.style.configure(
            "Custom.Vertical.TScrollbar",
            gripcount=0,
            background="#F1EAD7",  
            troughcolor="#F1EAD7",   
            arrowcolor="black",   
        )
        
        self.buttons=[]

        self.create_widget_menu()
    
        self.app.bind("<Return>", self.check)

        self.columnas_rows(col=8,row=15)
        self.app.mainloop()
    def create_widget_menu(self):
        self.numberCaja= tb.Label(self.app, text="- Caja 1", font=("helveica",35,"italic","bold"), background="#F1EAD7",anchor="center")

        self.User= tb.Entry(self.app, style="Custom.TButton", justify="center")
        self.Password= tb.Entry(self.app, style="Custom.TButton",justify="center", show="*")
        self.enter= tb.Button(self.app, style="Custom.TButton", text="Enter", command=self.check)
        
        self.enter.grid(column=3,row=7)
        self.Password.grid(column=3, row=6,sticky= "n")
        self.User.grid(column=3, row=5)
        self.numberCaja.grid(column=3,  row=3)   
        
    def create_widget_paypoint(self):
        self.delete_widgets()
        self.total = tb.Label(self.app,
                               text= f"$ {self.Bend.subtotal:.2f}", 
                               font = ("helvetica", 80), 
                               relief="solid", 
                               borderwidth=20, 
                               anchor="w", 
                               background= '#F1EAD7')
        self.cantidad= tb.Label(self.app,
                           text= f"{self.Bend.cant}", 
                           font=("helvetica", 80),
                           anchor="c",
                           relief="solid", 
                           borderwidth=20,
                           background= '#F1EAD7')
        self.entrada= tb.Entry(self.app,
                          style="Custom.TButton",
                          font=("helvetica", 50), 
                          justify= "center")
        detallado= tb.Frame(self.app,)
        scrollbar = tb.Scrollbar(detallado, orient="vertical", style="Custom.Vertical.TScrollbar")
        tree=("Cantidad", "Descripcion", "Monto")
        self.detalles = tb.Treeview(detallado,  columns=tree, show="headings", style="Custom.Treeview",yscrollcommand=scrollbar.set )
        self.detalles.heading("Cantidad", text="Cantidad", anchor="w")
        self.detalles.heading("Descripcion", text= "Descripcion", anchor="w")
        self.detalles.heading("Monto", text= "Precio",anchor="center")
        self.detalles.column("Cantidad", width=50, anchor="w")
        self.detalles.column("Descripcion", width=200, anchor="w")
        self.detalles.column("Monto", width=100, anchor="center")
    
        
        self.detalles.insert('', 'end', values=(" ", " ", " "))
           

        self.detalles.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        scrollbar.config(command=self.detalles.yview)

        
        self.total.place(relx=0.0, rely=0.0, relwidth=0.8, relheight=0.2 )
        self.cantidad.place(relx=0.8, rely=0.0, relwidth=0.25, relheight=0.2)
        self.entrada.place(relx=0.2, rely=0.8, relwidth=0.8, relheight=0.2)
        detallado.place(relx=0.05, rely=0.23, relwidth=0.8, relheight=0.55)

        PushButton = [[ "Precio", 0.9, 0.25, "dark"],
                    ["Cancelar", 0.9, 0.32, "info"],
                    ["Anular", 0.9, 0.39, "info"],
                    ["Suspender", 0.9, 0.5, "dark"],
                    ["Facturado", 0.9, 0.57, "dark"],
                    ["Nota Credito", 0.9, 0.64, "dark"]
                    ]
        

        for button in PushButton:
            self.create_botton(button[0], button[1], button[2], button[3])
            print("/////////////////Succeeded///////////////////")
        self.app.bind("<Return>", self.items)
        self.app.bind("<F4>", self.Resume)
        self.app.bind("<+>", lambda event: self.almacen(event, "Almacén"))
        self.app.bind("<F5>", lambda event: self.almacen(event, "Fiambrería"))  
        self.app.bind("<F6>", lambda event: self.almacen(event, "Verdulería"))              
        self.app.bind("<F7>", lambda event: self.almacen(event, "Carnicería"))
        self.app.bind("<F8>", lambda event: self.almacen(event, "Frío/Bolsa"))
        self.app.bind("<F9>", lambda event: self.almacen(event, "Envase"))

    def check(self, event=None):
        username = self.User.get()  
        password= self.Password.get()
        if self.Bend.validate_user(username,password):
            self.app.unbind("<Return>")
            self.pay= tb.Button(self.app, style= "Custom.TButton", 
            text="PayPoint", command= self.create_widget_paypoint)
            self.sales= tb.Button(self.app, style= "Custom.TButton",
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
            background= "#F1EAD7",
            foreground= "red" )
            self.error.grid(column=3, row=6, sticky= "s")
            try:
                self.pay.grid_forget()
                self.sales.grid_forget()
            except:
                pass

            
    def create_botton(self, text1, Col, Row,Style):
        button= tb.Button(self.app, bootstyle=Style, text= text1)
        button.place(relx=Col, rely=Row, relheight=0.07, relwidth=0.1)
        self.buttons.append(button)
    def items(self,event =0):
        content= self.entrada.get()
        position = content.find('*')  # Encuentra la posición del asterisco
        if position != -1:
            codigo=content[(position+1):]
            check=content[:position]
            if check.isdigit():
                mult= int(check) 
            else:
                codigo=content

        else:
            codigo=content
            mult=1
        self.entrada.delete(0, tb.END)
        result=self.Bend.item(codigo) if codigo.isdigit() else 0
        if not result:
            Messagebox.show_warning(
                title="Error", 
                message="Articulo NO registrado",
                alert=True, parent=self.app )
        else:    
 
            net=''
            value= result[5]* mult
            for x in range(3):
                if result[x]: net+= f"{result[x]} "
                
            self.detalles.insert('', 'end', values=(f"{mult}", f"{net}", f"$ {value:.2f} "))
            self.Bend.suma(value,mult)
            self.total.config(text=f'$ {self.Bend.subtotal:.2f}')           
            self.cantidad.config(text=f'{self.Bend.cant}')
    def almacen(self,event,type):
        content= self.entrada.get()[:-1] if type== 'Almacén' else self.entrada.get()
        position = content.find('*')  # Encuentra la posición del asterisco
        self.entrada.delete(0, tb.END)
        if position != -1:
            codigo=float(content[(position+1):]) if content[(position+1):].replace(".", "", 1).isdigit() and content[(position+1):].count(".") < 2 else 0
            check=content[:position]
            if check.isdigit():
                mult= int(check) 
            else:
                codigo=float(content)
        else:
            codigo=float(content[(position+1):]) if content[(position+1):].replace(".", "", 1).isdigit() and content[(position+1):].count else 0
            mult=1
        if codigo==0:
            Messagebox.show_warning(title='Error',message=f"Verifique el valor: {content}")
        else:
            value= mult*codigo
            self.detalles.insert('', 'end', values=(f"{mult}", f"{type}", f"$ {value:.2f} "))
            self.Bend.suma(value,mult)
            self.total.config(text=f'$ {self.Bend.subtotal:.2f}')           
            self.cantidad.config(text=f'{self.Bend.cant}')
    
    def delete_widgets(self):
        for widget in self.app.winfo_children():
            widget.unbind_all
        for widget in self.app.winfo_children():
            widget.destroy()

    
    def columnas_rows(self, col, row):
        "columnas y rows asignados"

        for i in range(col):
            self.app.columnconfigure(i,weight= 1)
            
        for z in range(row):
            self.app.rowconfigure(z,weight=1)
    def Resume(self,event=0):
        for widget in self.app.winfo_children():
            widget.unbind_all
        resume = tk.Frame(self.app)
        resume.config(background='#F1EAD7')
        resume.place(relx=0, rely=0, relwidth=1, relheight=1)
        resume.grab_set()
        self.app.bind("<Escape>", lambda event: resume.destroy())  

        R_total= tb.Label(resume,text= 'Total:',background='#F1EAD7',foreground='#847C67', font=("helvetica", 70))
        R_total_valor= tb.Label(resume, text= f'$ {self.Bend.subtotal:.2f}', font= ('Helvetica',70),background='#F1EAD7' ,foreground='#847C67')
        R_bonificacion= tb.Label(resume, text='Bonificación %', font= ('Helvetica',30),background='#F1EAD7' ,foreground='#847C67')
        R_efectivo= tb.Label(resume, text='+ Efectivo:' ,font= ('Helvetica',30),background='#F1EAD7' ,foreground='#847C67')
        R_PagoElec= tb.Label(resume, text='+ Pago Virtual:' ,font= ('Helvetica',30),background='#F1EAD7' ,foreground='#847C67')
        R_Tarjeta= tb.Label(resume, text='+ Tarjeta:' ,font= ('Helvetica',30),background='#F1EAD7' ,foreground='#847C67')
        R_efectivo_valor= tb.Entry(resume, style= 'Custom.TButton', font= ("helvetica",25), justify='center')
        R_PagoElec_valor= tb.Entry(resume, style= 'Custom.TButton', font= ("helvetica",25), justify='center')
        R_tarjeta_valor= tb.Entry(resume, style= 'Custom.TButton', font= ("helvetica",25), justify='center')
        R_bonificacion_valor= tb.Entry(resume, style= 'Custom.TButton', font= ("helvetica",25), justify='center')
        

        R_efectivo_valor.place(relx= 0.3244, rely= 0.3945, relwidth=0.17)
        R_PagoElec_valor.place(relx= 0.3244, rely= 0.4557, relwidth=0.17)
        R_tarjeta_valor.place(relx= 0.3244, rely= 0.5182, relwidth=0.17)
        R_efectivo.place(relx=0.0508, rely=0.3945)
        R_bonificacion_valor.place(relx= 0.72, rely= 0.1966, relwidth=0.06 )
        R_PagoElec.place(relx=0.0508, rely=0.4557)
        R_Tarjeta.place(relx=0.0508, rely=0.5182)
        R_bonificacion.place(relx=0.54, rely=0.1966)
        R_total.place(relx=0.032, rely=0.0677)
        R_total_valor.place(relx=0.65, rely=0.0677)
        
    def agregar_sim(self, contenido,event=0):
        if contenido.startswith("$"):
            numero = contenido[2:]
            numero2=contenido[1:]
            if numero2.replace(".", "", 1).isdigit() and numero2.count(".") < 2:
                
                return f"$ {float(numero2):.2f}"
                 
            else:
                if numero.replace(".", "", 1).isdigit() and numero.count(".") < 2:
                    return f"$ {float(numero):.2f}"
                else:
                    return "$ 0.00"
            


        if contenido.isdigit() or (contenido.replace(".", "", 1).isdigit() and contenido.count(".") < 2):
            return f"$ {float(contenido):.2f}" 
        else:
            return '$ 0.00'        

caja()


