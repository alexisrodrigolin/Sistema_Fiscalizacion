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

        self.total = tb.Label(self.app,
                               text= f"$ {self.Bend.subtotal:.2f}", 
                               font = ("helvetica", 80), 
                               relief="solid", 
                               borderwidth=20, 
                               anchor="w", 
                               background= '#F1EAD7')
        cantidad= tb.Label(self.app,
                           text= "25", 
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
        self.detalles.heading("Monto", text= "Precio",anchor="e")
        self.detalles.column("Cantidad", width=50, anchor="w")
        self.detalles.column("Descripcion", width=200, anchor="w")
        self.detalles.column("Monto", width=100, anchor="e")
    
        
        self.detalles.insert('', 'end', values=(" ", " ", " "))
           

        self.detalles.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        scrollbar.config(command=self.detalles.yview)

        
        self.total.place(relx=0.0, rely=0.0, relwidth=0.8, relheight=0.2 )
        cantidad.place(relx=0.8, rely=0.0, relwidth=0.25, relheight=0.2)
        self.entrada.place(relx=0.2, rely=0.8, relwidth=0.8, relheight=0.2)
        detallado.place(relx=0.05, rely=0.23, relwidth=0.85, relheight=0.4)

        PushButton = [[ "Precio", 0.9, 0.25, "dark"],
                    ["Cancelar", 0.9, 0.32, "info"],
                    ["Anular", 0.9, 0.39, "info"],
                    ["Suspender", 0.9, 0.5, "dark"],
                    ["Facturado", 0.9, 0.57, "dark"],
                    ["Nota Credito", 0.9, 0.64, "dark"]
                    ]
        self.app.bind("<Return>", self.items)

        for button in PushButton:
            self.create_botton(button[0], button[1], button[2], button[3])
            print("/////////////////Succeeded///////////////////")
            self.app.bind("<Return>", self.items)        
    def check(self, event=None):
        username = self.User.get()  
        password= self.Password.get()
        if self.Bend.validate_user(username,password):
            self.pay= tb.Button(self.app, style= "Custom.TButton", 
            text="PayPoint", command= self.payp)
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
    def payp(self):
            widgets_to_hide= [self.pay, self.sales, self.numberCaja, self.User, self.Password,self.enter]
            for widget in widgets_to_hide:
                widget.grid_forget()
            self.create_widget_paypoint()
            
    def create_botton(self, text1, Col, Row,Style):
        button= tb.Button(self.app, bootstyle=Style, text= text1)
        button.place(relx=Col, rely=Row, relheight=0.07, relwidth=0.1)
        self.buttons.append(button)
    def items(self,event =0):
        codigo= self.entrada.get()
        self.entrada.delete(0, tb.END)
        result=self.Bend.item(codigo) if codigo.isdigit() else 0
        if not result:
            Messagebox.show_warning(
            title="Error", 
            message="Articulo NO registrado",
            alert=True, parent=self.app )
        else:    
            net=''
            for x in range(3):
                if result[x]: net+= f"{result[x]} "
            
            self.detalles.insert('', 'end', values=("1", f"{net}", f"$ {result[5]:.2f} "))
            self.Bend.suma(result[5])
            self.total.config(text=f'$ {self.Bend.subtotal:.2f}')           

    
    
    
    def columnas_rows(self, col, row):
        "columnas y rows asignados"

        for i in range(col):
            self.app.columnconfigure(i,weight= 1)
            
        for z in range(row):
            self.app.rowconfigure(z,weight=1)

caja()


