import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import back
import textwrap
from tkinter import messagebox
from datetime import date
import math
import itertools
import copy

class caja():

    def __init__(self, *args, **kwargs):

        self.app = tb.Window(title="PayPoint", size=[1024, 768])
        self.app.config(background='#F1EAD7')
        self.app.state('zoomed')
        self.Bend = back.Logic() 


        self.style = tb.Style()
        self.style.configure("Custom.TButton",
                             background="#F1EAD7",
                             bordercolor="black",
                             foreground="black",
                             font=("arial", int(20 * self.Bend.font)),
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
            font=("arial", int(17 * self.Bend.font)),
        )
        self.style.configure(
            "Custom.Treeview.Heading",
            background="#F1EAD7",
            foreground="black",
            font=("arial", int(19 * self.Bend.font), "bold"),
        )
        self.style.configure(
            "Custom.Vertical.TScrollbar",
            gripcount=0,
            background="#F1EAD7",
            troughcolor="#F1EAD7",
            arrowcolor="black",
        )

        self.create_widget_menu()
        self.app.bind("<Return>", self.check)
        self.columnas_rows(col=8, row=15)


        
        self.app.mainloop()



    def create_widget_menu(self):
        self.numberCaja = tb.Label(self.app, text="- Caja 1",
                                   font=("arial", int(35 * self.Bend.font), "italic", "bold"),
                                   background="#F1EAD7", anchor="center")
        self.User = tb.Entry(self.app, style="Custom.TButton", justify="center")
        self.Password = tb.Entry(self.app, style="Custom.TButton", justify="center", show="*")
        self.enter = tb.Button(self.app, style="Custom.TButton", text="Enter", command=self.check)
        self.enter.grid(column=3, row=7)
        self.Password.grid(column=3, row=6, sticky="n")
        self.User.grid(column=3, row=5)
        self.numberCaja.grid(column=3, row=3)
        self.User.focus()

    def create_widget_paypoint(self):
        self.OFstatus=1
        self.guardado=0
        self.suspendido=[]
        def change_OFstatus(status):
           
            if not self.detalles.get_children():
                if status==1:
                    self.OFstatus=1
                    button4.config(text="Ofertas ap ✔ ", bootstyle="success")      
                    button5.config(text="SIN ofertas ap ", bootstyle="dark")        
                elif status==0:
                    self.OFstatus=0
                    button4.config(text="Ofertas ap ", bootstyle="dark")      
                    button5.config(text="SIN ofertas ap ✔", bootstyle="success")        
            else:
                self.mostrar_error("Cancele el tique para cambiar estado", 1)
        try:
            self.delete_widgets()
            detallado = tb.Frame(self.app, )
            scrollbar = tb.Scrollbar(detallado, orient="vertical", style="Custom.Vertical.TScrollbar")
            tree = ("Cantidad", "Descripcion", "MontoU","Monto")
            self.detalles = tb.Treeview(detallado, columns=tree, show="headings", style="Custom.Treeview",
                                        yscrollcommand=scrollbar.set)
            self.detalles.heading("Cantidad", text="Cantidad", anchor="w")
            self.detalles.heading("Descripcion", text="Descripcion", anchor="w")
            self.detalles.heading("MontoU", text="Precio Uni", anchor="e")
            self.detalles.heading("Monto", text="Precio", anchor="e")
            self.detalles.column("Cantidad", width=5, anchor="center")
            self.detalles.column("Descripcion", width=200, anchor="w")
            self.detalles.column("MontoU", width=70, anchor="e")
            self.detalles.column("Monto", width=70, anchor="e")
            self.detalles.insert('', 'end', values=(" ", " ", " "))
            scrollbar.config(command=self.detalles.yview)
            self.detalles.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            self.total = tb.Label(self.app,
                                text=f"$ {format(self.Bend.subtotal, ',.2f')}",
                                font=("arial", int(80 * self.Bend.font)),
                                relief="solid",
                                borderwidth=20,
                                anchor="w",
                                background='#F1EAD7')
            self.cantidad = tb.Label(self.app,
                                    text=f"{self.Bend.cant}",
                                    font=("arial", int(80 * self.Bend.font)),
                                    anchor="c",
                                    relief="solid",
                                    borderwidth=20,
                                    background='#F1EAD7')
            self.entrada = tb.Entry(self.app,
                                    style="Custom.TButton",
                                    font=("arial", int(50 * self.Bend.font)),
                                    justify="center")
            detallado.place(relx=0.05, rely=0.23, relwidth=0.8, relheight=0.55)
            self.total.place(relx=0.0, rely=0.0, relwidth=0.8, relheight=0.2)
            self.cantidad.place(relx=0.8, rely=0.0, relwidth=0.25, relheight=0.2)
            self.entrada.place(relx=0.2, rely=0.8, relwidth=0.8, relheight=0.2)

            button1 = tb.Button(self.app, bootstyle="dark", text="Precio", command=lambda:self.precio())
            button1.place(relx=0.9, rely=0.25, relheight=0.07, relwidth=0.1)
        
            button2 = tb.Button(self.app, bootstyle="info", text="Cancelar",command=lambda: self.password(status=1))
            button2.place(relx=0.9, rely=0.32, relheight=0.07, relwidth=0.1)
            
     
            button3 = tb.Button(self.app, bootstyle="info", text="Anular", command=lambda: self.password(status=0))
            button3.place(relx=0.9, rely=0.39, relheight=0.07, relwidth=0.1)
        
            button4 = tb.Button(self.app, bootstyle="success", text="Ofertas ap ✔", command=lambda: change_OFstatus(1))
            button4.place(relx=0.9, rely=0.5, relheight=0.07, relwidth=0.1)
          
            button5 = tb.Button(self.app, bootstyle="dark", text="SIN ofertas ap", command=lambda: change_OFstatus(0))
            button5.place(relx=0.9, rely=0.57, relheight=0.07, relwidth=0.1)
        
            self.button6 = tb.Button(self.app, bootstyle="dark", text="Suspender",command=lambda:self.suspender())
            self.button6.place(relx=0.9, rely=0.64, relheight=0.07, relwidth=0.1)
            

            self.ppbind()
        except:
            self.mostrar_error("Error Fatal")
    def conf(self, status=0):
        cfg= tk.Frame(self.app, )
        cfg.config(background='#F1EAD7')
        cfg.place(relx=0, rely=0, relheight=1, relwidth=1)
        def save():
            repuestas=messagebox.askokcancel('Save', 'Desea guardar los cambios?')
            if repuestas:
                self.Bend.datos['Baudrate']= baudrate.get()
                self.Bend.datos['Com']= com.get()
                self.Bend.datos['AdminPass']= passwordA.get()
                self.Bend.datos['EntryPass']= passwordE.get()
                self.Bend.datos['SuperPass']= passwordS.get()
  
                if status==1: 
                    self.Bend.datos['Db']= Db.get()
                    self.Bend.datos['User']= DbU.get()
                    self.Bend.datos['Password']= DbP.get()[5:] 
                    self.Bend.datos['Font']= font.get()            
                self.Bend.writeCfg()
                cfg.destroy()
            

        tb.Label(cfg, text="COM:", background='#F1EAD7',font=("arial", int(30 * self.Bend.font))).pack()
        com=tb.Entry(cfg,style="Custom.TButton",font=("arial", int(15 * self.Bend.font)),justify="center") 
        com.pack()
        tb.Label(cfg, text="Baudrate:", background='#F1EAD7',font=("arial", int(30 * self.Bend.font))).pack()
        baudrate=tb.Entry(cfg,style="Custom.TButton",font=("arial", int(15 * self.Bend.font)),justify="center") 
        baudrate.pack()
        tb.Label(cfg, text="Contraseña Supervisor:", background='#F1EAD7',font=("arial", int(30 * self.Bend.font))).pack()
        passwordS=tb.Entry(cfg,style="Custom.TButton",font=("arial", int(15 * self.Bend.font)),justify="center") 
        passwordS.pack()
        tb.Label(cfg, text="Contraseña Entrada:", background='#F1EAD7',font=("arial", int(30 * self.Bend.font))).pack()
        passwordE=tb.Entry(cfg,style="Custom.TButton",font=("arial", int(15 * self.Bend.font)),justify="center") 
        passwordE.pack()
        tb.Label(cfg, text="Contraseña Administrador:", background='#F1EAD7',font=("arial", int(30 * self.Bend.font))).pack()
        passwordA=tb.Entry(cfg,style="Custom.TButton",font=("arial", int(15 * self.Bend.font)),justify="center") 
        passwordA.pack()
        tb.Label(cfg, text="#Mantener Precaución al manipular las configuraciones", background='#F1EAD7', foreground="grey").pack()

        com.insert(0, self.Bend.datos['Com'])
        baudrate.insert(0, self.Bend.datos['Baudrate'])
        passwordA.insert(0, self.Bend.datos['AdminPass'])
        passwordE.insert(0, self.Bend.datos['EntryPass'])
        passwordS.insert(0, self.Bend.datos['SuperPass'])

        if status== 1:
            tb.Label(cfg, text="Database:", background='#F1EAD7',font=("Arial", int(30 * self.Bend.font))).pack()
            Db=tb.Entry(cfg,style="Custom.TButton",font=("Arial", int(15 * self.Bend.font)),justify="center") 
            Db.pack()
            tb.Label(cfg, text="Db User:", background='#F1EAD7',font=("arial", int(30 * self.Bend.font))).pack()
            DbU=tb.Entry(cfg,style="Custom.TButton",font=("arial", int(15 * self.Bend.font)),justify="center") 
            DbU.pack()
            tb.Label(cfg, text="Db Password:", background='#F1EAD7',font=("arial", int(30 * self.Bend.font))).pack()
            DbP=tb.Entry(cfg,style="Custom.TButton",font=("arial", int(15 * self.Bend.font)),justify="center") 
            DbP.pack()
            Db.insert(0, self.Bend.datos['Db'])
            DbU.insert(0, self.Bend.datos['User'])
            DbP.insert(0, f"dadds{self.Bend.datos['Password']}")
            tb.Label(cfg, text="Font:", background='#F1EAD7',font=("arial", int(30 * self.Bend.font))).pack()
            font=tb.Entry(cfg,style="Custom.TButton",font=("arial", int(15 * self.Bend.font)),justify="center") 
            font.pack()
            font.insert(0, self.Bend.datos['Font'])
        tb.Button(cfg, text="Guardar", style="Custom.TButton", command=save).pack(pady=10)
        tb.Button(cfg, text="Menu", style="Custom.TButton", command=cfg.destroy).pack(pady=10)
    def check(self, event=None):
        key=0
        username = self.User.get()
        password = self.Password.get()
        if username== 'admin':
            if password== '888888':
                self.app.unbind("<Return>")
                self.M_entrada()
                config= tb.Button(self.app, text= "Configuration", style="Custom.TButton", command= lambda: self.conf(0))
                config.grid(column=3, row=12)
                key=1
            elif password== 'rksystems2505':
                self.app.unbind("<Return>")
                self.M_entrada()
                config= tb.Button(self.app, text= "Configuration", style="Custom.TButton", command= lambda: self.conf(1))
                config.grid(column=3, row=12)
                key=1
        try:
            self.Bend.Conection()
        
        except:
            self.mostrar_error("Error de Conexion con Base Central")
            return
        if self.Bend.validate_user(username, password):
            self.app.unbind("<Return>")
            self.M_entrada()
            try:
                self.error.grid_forget()
            except:
                pass
        elif key==1:
            pass
        else:
            self.error = tb.Label(self.app,
                                  text="Usuario o Contraseña incorrecta",
                                  background="#F1EAD7",
                                  foreground="red")
            self.error.grid(column=3, row=6, sticky="s")
            try:
                self.pay.grid_forget()
                self.sales.grid_forget()
            except:
                pass

            
    def M_entrada(self):
        
            self.pay = tb.Button(self.app, style="Custom.TButton",
                                text="PayPoint", command=self.create_widget_paypoint)
            self.sales = tb.Button(self.app, style="Custom.TButton",
                                text="SalesOverview", command=self.Sales )
            self.sales.grid(column=3, row=11)
            self.pay.grid(column=3, row=10)

    def items(self, event=0, status=0,Re=0, values=0,extra=0):
        if Re:
            content=Re
        else:
            content = self.entrada.get()
        cantOf=0
        self.ppbind()
        position = content.find('*')  # Encuentra la posición del asterisco
        if position!= -1:
            codigo = content[(position + 1):]
            check = content[:position]
            if check.isdigit():
                mult = int(check)
            else:
                codigo = content
        else:
            codigo = content
            mult = 1
        self.entrada.delete(0, tb.END)
        result = self.Bend.item(codigo) if codigo.isdigit() else 0
        if result==0 and status==0:
            self.mostrar_error("Articulo NO Registrado",1)
        elif result==0 and status==1:
            self.mostrar_error("Articulo NO Registrado",5)
        else:
            of=1
            if not self.OFstatus:
                value = result[5] * mult
                resto=0
                net = ''    
                price=result[5]
               
            elif self.OFstatus:
                variables = [(result[6], result[7]), ( result[8], result[9]), (result[10], result[11])]
                ordenadas = sorted(variables, key=lambda x: (x[0] is not None, x[0] if x[0] is not None else float('-inf')), reverse=True)
           
                if ordenadas[0][0] is not None and ordenadas[0][0] <= mult:
                    of=ordenadas[0][0]
                    enteros= math.floor(mult/ordenadas[0][0])
                    cantOf=(enteros*ordenadas[0][0])
                    resto= mult-cantOf
                    value=cantOf* ordenadas[0][1]
                    net = 'PROMO '
                    price=ordenadas[0][1]
                elif ordenadas[1][0] is not None  and ordenadas[1][0] <= mult:
                    of=ordenadas[1][0]
                    enteros= math.floor(mult/ordenadas[1][0])
                    cantOf=(enteros*ordenadas[1][0])
                    resto= mult-cantOf
                    value=cantOf* ordenadas[1][1]
                    price=ordenadas[1][1]
                    net = 'PROMO '
                elif ordenadas[2][0] is not None  and ordenadas[2][0] <= mult:
                    of=ordenadas[2][0]
                    enteros= math.floor(mult/ordenadas[2][0])
                    cantOf=(enteros*ordenadas[2][0])
                    resto= mult-cantOf
                    value=cantOf* ordenadas[2][1]
                    price=ordenadas[2][1]
                    net = 'PROMO '
                else:
                    price=result[5]
                    resto=0
                    net = ''
                    value=mult*price
            for x in range(3):
                if result[x]: net += f"{result[x]} "
            if status==0:
                if cantOf:
                    self.detalles.insert('', 'end', values=(f"{cantOf}", f"{net}",f"$ {format(price, ',.2f')}", f"$ {format(value, ',.2f')}"))
                    self.Bend.suma(Descripcion=f"{net}", Precio=price, Plu=f"{codigo}", Cantidad=cantOf, cantOF=of)
                else:
                    self.detalles.insert('', 'end', values=(f"{mult}", f"{net}",f"$ {format(price, ',.2f')}", f"$ {format(value, ',.2f')}"))
                    self.Bend.suma(Descripcion=f"{net}", Precio=price, Plu=f"{codigo}", Cantidad=mult, cantOF=of)
                self.total.config(text=f"$ {format(self.Bend.subtotal, ',.2f')}")
                self.cantidad.config(text=f'{self.Bend.cant}')
            elif status==1 and resto==0:
                if extra:
                    self.Pitem.config(text= f"PROMO {net} x{mult+extra}")    
                else:
                    self.Pitem.config(text= f"{net} x{mult+extra}")    
                self.Pprice.config(text= f"$ {format((value+values),',.2f')}")
            elif status==2:
                if cantOf:
                    self.detalles.insert('', 'end', values=(f"- {cantOf}", f"{net}",f"- $ {format(price, ',.2f')}", f"- $ {format(value, ',.2f')}"))
                else:
                    self.detalles.insert('', 'end', values=(f"- {mult}", f"{net}",f"- $ {format(price, ',.2f')}", f"- $ {format(value, ',.2f')}"))
                self.Bend.suma(Descripcion=f"{net}", Precio=price, Plu=f"{codigo}", Cantidad=(mult*(-1)))
                self.total.config(text=f"$ {format(self.Bend.subtotal, ',.2f')}")
                self.cantidad.config(text=f'{self.Bend.cant}')
            if resto and (status==0 or status==2):
                self.items(Re=f"{resto}*{codigo}",status=status)
            elif resto and status==1:
                self.items(Re=f"{resto}*{codigo}",status=status, values=+value,extra=cantOf)
    def password(self, event=0, status=0):
        def read(event=0):
            if cont.get()== self.Bend.datos["SuperPass"]:
                self.passw.destroy()
                self.ppbind()             
                if status==1:
                    self.cancelar_anular(1)    
                elif status==0:
                    self.app.bind("<Return>", lambda event: self.cancelar_anular(event=event, status=0))
                    self.app.bind("<+>", lambda event: self.almacen(event=event, type= "Almacén",status=2))
                    self.app.bind("<F5>", lambda event: self.almacen(event=event, type=  "Fiambrería",status=2))
                    self.app.bind("<F6>", lambda event: self.almacen(event=event, type= "Verdulería",status=2))
                    self.app.bind("<F7>", lambda event: self.almacen(event=event, type=  "Carnicería",status=2))
                    self.app.bind("<F8>", lambda event: self.almacen(event=event, type= "Frío/Bolsa",status=2))
                    self.app.bind("<F9>", lambda event: self.almacen(event=event, type= "Envase",status=2))
                    self.app.bind("<F10>", lambda event: self.almacen(event=event, type=  "Bazar",status=2))
            else: 
                error.pack(pady=20)
        hijos = self.detalles.get_children()
        if self.Bend.subtotal==0.00 and status==0:
            self.mostrar_error("No hay Item para anular", 1)
            return
        if (not hijos) and status==1:
            self.mostrar_error("No hay Tique para Cancelar", 1)
            return
        color= 'grey'
        self.passw=tk.Frame(self.app)
        self.passw.config(background=color)
        self.passw.place(relheight=0.5,relwidth=0.5, rely=0.2, relx=0.25)
        self.ppunbind()
        tb.Label(self.passw, text= 'Ingrese contraseña de Supervisor', background='grey',font=("arial", int(30 * self.Bend.font))).pack(pady=10)
        self.app.bind("<Return>", read)
        cont=tb.Entry(self.passw, justify="center",show='*',font=("arial", int(30 * self.Bend.font)) )
        error=tb.Label(self.passw,text= "Contraseña Incorrecta",foreground='red', background='grey',font=("arial", int(15 * self.Bend.font)))
        cont.pack(pady=20)
        cont.focus_set()
        self.app.bind("<Escape>", lambda event: (self.ppbind(event), self.passw.destroy()))
    def precio(self,event=0):
        color= 'grey'
        self.Precio=tk.Frame(self.app)
        self.Precio.config(background=color)
        self.Precio.place(relheight=0.5,relwidth=0.5, rely=0.2, relx=0.25)
        tb.Label(self.Precio, text= 'Consulte el Precio:', background='grey',font=("arial", int(30 * self.Bend.font))).pack(pady=10)
        self.preciobind()
        self.Pitem=tb.Label(self.Precio, text= "",foreground='white', background='grey',font=("arial", int(30 * self.Bend.font)) )
        self.Pprice=tb.Label(self.Precio,text= "",foreground='white', background='grey',font=("arial", int(30 * self.Bend.font)))
        self.Pitem.pack(pady=20)
        self.Pprice.pack(pady=20)
    def preciobind(self):
        self.app.bind("<Escape>", lambda event: (self.Precio.destroy(), self.ppbind()))
        self.app.bind("<Return>", lambda event: self.items(event,1))
        self.app.bind("<+>", lambda event: self.almacen(event=event, type="Almacén",status=1))
        self.app.bind("<F5>", lambda event: self.almacen(event=event, type="Fiambrería",status=1))
        self.app.bind("<F6>", lambda event: self.almacen(event=event, type="Verdulería",status=1))
        self.app.bind("<F7>", lambda event: self.almacen(event=event, type="Carnicería",status=1))
        self.app.bind("<F8>", lambda event: self.almacen(event=event, type="Frío/Bolsa",status=1))
        self.app.bind("<F9>", lambda event: self.almacen(event=event, type="Envase",status=1))
        self.app.bind("<F10>", lambda event: self.almacen(event=event, type="Bazar",status=1))
    def almacen(self,type,event=0,status=0, re=0 ):
        if re:
            content=re
        else:
            content = self.entrada.get()[:-1] if type == 'Almacén' else self.entrada.get()
        self.ppbind()
        if not content:
            return
        position = content.find('*')
        self.entrada.delete(0, tb.END)
        if position!= -1:
            codigo = float(content[(position + 1):]) if content[(position + 1):].replace(".", "", 1).isdigit() and \
                                                      content[(position + 1):].count(".") < 2 else 0
            check = content[:position]
            if check.isdigit():
                mult = int(check)
            else:
                codigo = float(content)
        else:
            codigo = float(content[(position + 1):]) if content[(position + 1):].replace(".", "", 1).isdigit() and \
                                                      content[(position + 1):].count else 0
            mult = 1
        if codigo == 0 and status==0:
            self.mostrar_error(f"Verifique el valor: {content}",1)
        elif codigo == 0 and status==1:
            self.mostrar_error(f"Verifique el valor: {content}",5)
        else:
            value = mult * codigo
            if status==0:
                self.detalles.insert('', 'end', values=(f"{mult}", f"{type}",f"$ {format(codigo,',.2f')}", f"$ {format(value,',.2f')}"))
                self.Bend.suma(Descripcion=f"{type}", Cantidad=mult,  Precio=codigo, Plu='11111111')
                self.total.config(text=f"$ {format(self.Bend.subtotal,',.2f')}")
                self.cantidad.config(text=f'{self.Bend.cant}')
            elif status==1:
                self.Pitem.config(text= f"{type} x{mult}")    
                self.Pprice.config(text= f"$ {format(value,',.2f')}")
            elif status==2:
                resultados = [item for item in self.Bend.internal if (item[0] == type and item[1]==codigo)]
                sumainterna=0
                for values in resultados:
                    sumainterna+= values[3]
                if resultados and sumainterna>=mult:
                    self.detalles.insert('', 'end', values=(f"- {mult}", f"{type}",f"- $ {format(codigo,',.2f')}", f"- $ {format(value,',.2f')}"))
                    self.Bend.suma(Descripcion=f"{type}", Cantidad=(mult*(-1)),  Precio=codigo, Plu='11111111')
                    self.total.config(text=f"$ {format(self.Bend.subtotal,',.2f')}")
                    self.cantidad.config(text=f'{self.Bend.cant}')
                   
                    self.Bend.internal = [t for t in self.Bend.internal if not (t[0]==type and t[1]== codigo)]
                    RestoFacturado= sumainterna- mult
                    self.Bend.nitem+=1
                    item=(f"{type}",codigo, '11111111', RestoFacturado,1,self.Bend.nitem)
                    if RestoFacturado>0: self.Bend.internal.append(item)
                else:
                    self.mostrar_error("Producto NO Facturado",1)
    def delete_widgets(self):
        self.ppunbind()
        for widget in self.app.winfo_children():
            widget.destroy()

    def columnas_rows(self, col, row):
        for i in range(col):
            self.app.columnconfigure(i, weight=1)
        for z in range(row):
            self.app.rowconfigure(z, weight=1)

    def enter_as_tab(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def ppbind(self, event=0):
        self.app.bind("<Escape>", self.menu)
        self.app.bind("<Return>", lambda event: self.items(event, 0))
        self.app.bind("<+>", lambda event: self.almacen(event=event, type= "Almacén"))
        self.app.bind("<F1>", lambda event: self.precio(event))
        self.app.bind("<F2>", lambda event: self.password(event=event, status=0))
        self.app.bind("<F3>", lambda event: self.password(event=event, status=1))
        self.app.bind("<F4>", self.Resume)
        self.app.bind("<F5>", lambda event: self.almacen(event=event, type=  "Fiambrería"))
        self.app.bind("<F6>", lambda event: self.almacen(event=event, type= "Verdulería"))
        self.app.bind("<F7>", lambda event: self.almacen(event=event, type=  "Carnicería"))
        self.app.bind("<F8>", lambda event: self.almacen(event=event, type= "Frío/Bolsa"))
        self.app.bind("<F9>", lambda event: self.almacen(event=event, type= "Envase"))
        self.app.bind("<F10>", lambda event: self.almacen(event=event, type=  "Bazar"))
        self.entrada.focus_set()

    def menu(self, event=0):
       
        if not self.detalles.get_children():
            self.ppunbind()
            self.cancelar_anular(1)
            for widget in self.app.winfo_children():
                widget.destroy()
            self.numberCaja = tb.Label(self.app, text="- Caja 1",
                                       font=("helveica", int(35 * self.Bend.font), "italic", "bold"),
                                       background="#F1EAD7", anchor="center")
            self.numberCaja.grid(column=3, row=3)
            self.M_entrada()
        else:
            self.mostrar_error("Tique Abierto",1 )

    def ppunbind(self,event=0):
        for event_type in ("<Return>","<Escape>", "<+>", "<F1>","<F2>", "<F3>", "<F4>", "<F5>", "<F6>", "<F7>", "<F8>", "<F9>", "<F10>"):
            self.app.unbind(event_type)

    def Resume(self, event=0):
        if not self.Bend.subtotal:
            return

        self.entrada.delete(0, tb.END)
        self.ppunbind()

        self.resume = tk.Frame(self.app)
        self.resume.config(background='#F1EAD7')
        self.resume.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.resume.grab_set()
        self.R_bonificacion_valor = tb.Entry(self.resume, style='Custom.TButton',
                                        font=("arial", int(25 * self.Bend.font)), justify='center',width=3)
        self.R_recargo_valor = tb.Entry(self.resume, style='Custom.TButton',
                                        font=("arial", int(25 * self.Bend.font)), justify='center',width=3)
        R_total = tb.Label(self.resume, text='Total:', background='#F1EAD7', foreground='#847C67',
                           font=("arial", int(70 * self.Bend.font)))
        self.R_total_valor = tb.Label(self.resume, text=f"$ {format(self.Bend.subtotal, ',.2f')}",
                                 font=('arial', int(70 * self.Bend.font)), background='#F1EAD7',
                                 foreground='#847C67')
        R_bonificacion = tb.Label(self.resume, text='Bonificación %',
                                  font=('arial', int(30 * self.Bend.font)), background='#F1EAD7',
                                  foreground='#847C67')
        R_recargo = tb.Label(self.resume, text='Recargo %',
                                  font=('arial', int(30 * self.Bend.font)), background='#F1EAD7',
                                  foreground='#847C67')

        R_efectivo = tb.Label(self.resume, text='+ Efectivo:',
                              font=('arial', int(30 * self.Bend.font)), background='#F1EAD7',
                              foreground='#847C67')
        R_PagoElec = tb.Label(self.resume, text='+ Pago Virtual:',
                              font=('arial', int(30 * self.Bend.font)), background='#F1EAD7',
                              foreground='#847C67')
        R_Tarjeta = tb.Label(self.resume, text='+ Tarjeta:',
                             font=('arial', int(30 * self.Bend.font)), background='#F1EAD7',
                             foreground='#847C67')
        self.R_efectivo_valor = tb.Entry(self.resume, style='Custom.TButton',
                                    font=("arial", int(25 * self.Bend.font)), justify='center')
        self.R_PagoElec_valor = tb.Entry(self.resume, style='Custom.TButton',
                                    font=("arial", int(25 * self.Bend.font)), justify='center')
        self.R_tarjeta_valor = tb.Entry(self.resume, style='Custom.TButton',
                                   font=("arial", int(25 * self.Bend.font)), justify='center')
        R_monto = tb.Label(self.resume, text='Total recibido:', background='#F1EAD7', foreground='#847C67',
                           font=("arial", int(30 * self.Bend.font)))
        self.R_monto_valor = tb.Label(self.resume, text=f'$ 0.00',
                                 font=('arial', int(30 * self.Bend.font)), background='#F1EAD7',
                                 foreground='#847C67')
        R_vuelto = tb.Label(self.resume, text='Vuelto:', background='#F1EAD7', foreground='#847C67',
                            font=("arial", int(30 * self.Bend.font)))
        self.R_vuelto_valor = tb.Label(self.resume, text=f'$ 0.00',
                                  font=('arial', int(30 * self.Bend.font)), background='#F1EAD7',
                                  foreground='#847C67')
        self.R_facturacion = tb.Button(
            self.resume, 
            text='Facturacion', 
            style="Custom.TButton",
            command=lambda: self.facturacion_click(event)
        )
        self.R_efectivo_valor.place(relx= 0.3244, rely= 0.3945, relwidth=0.17)
        self.R_PagoElec_valor.place(relx= 0.3244, rely= 0.4557, relwidth=0.17)
        self.R_tarjeta_valor.place(relx= 0.3244, rely= 0.5182, relwidth=0.17)
        self.R_facturacion.place(relx= 0.35, rely=0.75, relwidth=0.1)
        R_efectivo.place(relx=0.0508, rely=0.3945)
        self.R_bonificacion_valor.place(relx= 0.72, rely= 0.1966,  )
        self.R_recargo_valor.place(relx= 0.72, rely= 0.25,  )
        R_PagoElec.place(relx=0.0508, rely=0.4557)
        R_Tarjeta.place(relx=0.0508, rely=0.5182)
        R_bonificacion.place(relx=0.54, rely=0.1966)
        R_recargo.place(relx=0.54, rely=0.25)
        R_total.place(relx=0.032, rely=0.0677)
        self.R_total_valor.place(relx=0.65, rely=0.0677)
        R_monto.place(relx= 0.0508, rely= 0.6)
        self.R_monto_valor.place(relx= 0.3244, rely= 0.6)
        R_vuelto.place(relx= 0.0508, rely= 0.66)
        self.R_vuelto_valor.place(relx= 0.3244, rely= 0.66)
        self.R_efectivo_valor.focus()       
        self.R_suma=0
        self.resumeBind()
    def suspender(self,event=0):
        
        if not self.guardado:
            if not self.detalles.get_children():
                self.mostrar_error("No hay Tique abierto",1)
                return
            self.suspendido=copy.deepcopy(self.Bend.tique)
            self.guardado=1
            self.cancelar_anular(status=1)
            self.button6.config(bootstyle="Success", text="Suspendido")
        elif self.guardado:
            if self.detalles.get_children():
                self.mostrar_error("Cierre Tique actual",1)
                return
            self.guardado=0
            self.button6.config(bootstyle="dark", text="Suspender")
            for items in self.suspendido:
                intern= f"{items[3]}*{items[1]}"
                if items[3]>0:
                    if items[0]=="Almacén":
                        self.almacen(re=intern, type="Almacén")
                    elif items[0]=="Fiambrería":
                        self.almacen(re=intern, type="Fiambrería")
                    elif items[0]=="Verdulería":
                        self.almacen(re=intern, type="Verdulería")
                    elif items[0]=="Carnicería":
                        self.almacen(re=intern, type="Carnicería")
                    elif items[0]=="Frío/Bolsa":
                        self.almacen(re=intern, type="Frío/Bolsa")
                    elif items[0]=="Envase":
                        self.almacen(re=intern, type="Envase")
                    elif items[0]=="Bazar":
                        self.almacen(re=intern, type="Bazar")
                    else:
                        self.items(Re=f"{items[3]}*{items[2]}")
                elif items[3]<0:
                    intern= f"{items[3]*(-1)}*{items[1]}"
                    if items[0]=="Almacén":
                        self.almacen(re=intern, status=2,type="Almacén")
                    elif items[0]=="Fiambrería":
                        self.almacen(re=intern, status=2,type="Fiambrería")
                    elif items[0]=="Verdulería":
                        self.almacen(re=intern, status=2,type="Verdulería")
                    elif items[0]=="Carnicería":
                        self.almacen(re=intern, status=2,type="Carnicería")
                    elif items[0]=="Frío/Bolsa":
                        self.almacen(re=intern, status=2,type="Frío/Bolsa")
                    elif items[0]=="Envase":
                        self.almacen(re=intern,status=2, type="Envase")
                    elif items[0]=="Bazar":
                        self.almacen(status=2,re=intern, type="Bazar")
                    else:
                        self.items(status=2,Re=f"{items[3]*(-1)}*{items[2]}")

    def sim(self,status, event=0):  
            
            if status ==1:
                widget= self.R_efectivo_valor
            elif status== 2: 
                widget= self.R_PagoElec_valor
            else:
                widget= self.R_tarjeta_valor
            contenido = widget.get()  
            if contenido.startswith("$"):
                numero = contenido[2:]
                numero2=contenido[1:]
                if numero2.replace(".", "", 1).isdigit() and numero2.count(".") < 2:
                    widget.delete(0, tk.END)  
                    widget.insert(0, f"$ {format(float(numero2),',.2f')}") 
                else:
                    if numero.replace(".", "", 1).isdigit() and numero.count(".") < 2:
                        widget.delete(0, tk.END)  
                        widget.insert(0, f"$ {format(float(numero2),',.2f')}")
                    else:
                        widget.delete(0, tk.END)  
            elif contenido.isdigit() or (contenido.replace(".", "", 1).isdigit() and contenido.count(".") < 2):
                widget.delete(0, tk.END)  
                widget.insert(0, f"$ {format(float(contenido ),',.2f')}") 
            else:
                widget.delete(0, tk.END)
            self.R_suma=0
            for x in (self.R_efectivo_valor, self.R_PagoElec_valor, self.R_tarjeta_valor):
                val=x.get()
                result= float(val[2:].replace(',','')) if not val == "" else 0
                self.R_suma+= result
            R_vueltos= self.R_suma - self.Bend.subtotal
            self.R_vuelto_valor.config(text= f"$ {format(R_vueltos,',.2f')}")
            self.R_monto_valor.config(text= f"$ {format(self.R_suma,',.2f')}")

    def resumeBind(self):
        def bon(event=0):
            rec= int(self.R_recargo_valor.get()) if self.R_recargo_valor.get().isdigit() else 0
            if rec<=0: self.R_recargo_valor.delete(0, tk.END)
            boni= int(self.R_bonificacion_valor.get()) if self.R_bonificacion_valor.get().isdigit() else 0
            if boni<=0 or boni>=100: 
                self.R_bonificacion_valor.delete(0, tk.END)
                boni=0
            porcentaje= 100+rec-boni
            value=(porcentaje*self.Bend.subtotal)/100
            self.R_total_valor.config(text= f"$ {format(value, ',.2f')}")
            if not value== self.Bend.subtotal:
                tb.Label(self.resume, text=f"Subtotal:  $ {format(self.Bend.subtotal, ',.2f')}",
                                  font=('arial', int(30 * self.Bend.font)), background='#F1EAD7',
                                  foreground='#847C67').place(relx=0.54, rely=0.35)
        self.R_efectivo_valor.bind("<Return>", lambda event : self.enter_as_tab(event))
        self.R_PagoElec_valor.bind("<Return>", lambda event : self.enter_as_tab(event))
        self.R_tarjeta_valor.bind("<Return>", lambda event: (self.resume.focus_force(), self.resume.destroy(), 
                                                             self.ppbind(),self.call("tique", event)))
        self.R_efectivo_valor.bind("<FocusOut>", lambda event: self.sim(1, event))
        self.R_PagoElec_valor.bind("<FocusOut>", lambda event: self.sim(2, event))
        self.R_tarjeta_valor.bind("<FocusOut>", lambda event: self.sim(3, event))
        self.R_recargo_valor.bind("<FocusOut>", lambda event: bon(event))
        self.R_bonificacion_valor.bind("<FocusOut>", lambda event: bon(event))
        self.app.bind("<F4>", lambda event: (self.resume.destroy(), self.ppbind(),self.call("tique", event)))
        self.app.bind("<Escape>", lambda event: (self.resume.destroy(), self.ppbind()))
    def call(self, command,extra=0, extra1=0, event=0):
        if command == 'tique':
            if self.R_suma >= self.Bend.subtotal:
                iva = self.Bend.subtotal * 0.21
                result = self.Bend.main(f"{command}", extra, extra1, iva=iva) if extra1 else self.Bend.main(f"{command}", iva=iva)
                
                if not result:
                    self.cancelar_anular(status=1)
                else:
                    self.mostrar_error(f"{result}", 1)
            else:
                self.mostrar_error("El Monto es menor al Total", 1)
        else:
            result = self.Bend.main(f"{command}", extra, extra1) if extra1 else self.Bend.main(f"{command}")

            if command == 'z' or command == 'x':
                if result:
                    self.mostrar_error(f"{result}", 3)

            elif command in ['AuditoriaDZ', 'AuditoriaDF', 'AuditoriaF', 'AuditoriaZ']:
                if result:
                    self.mostrar_error(f"{result}", 4)
    def cancelar_anular(self, status, event=0, achieve=0):
        if achieve:
            # Update Caja1 table with cancellation
            self.Bend.update_caja1(
                facturated=0,
                non_facturated=0,
                card=0,
                cash=0,
                virtual=0,
                tcard=0,
                tcash=0,
                tvirtual=0,
                tcancelled=1,  # Add 1 to cancelled transactions count
                cancelled=self.Bend.subtotal  # Add subtotal to cancelled amount
            )
            
        if status == 1:
            self.Bend.suma(refresh=1)
            self.detalles.delete(*self.detalles.get_children())
            self.cantidad.config(text= f'{self.Bend.cant}')
            self.total.config(text=f"$ {format(self.Bend.subtotal, ',.2f')}")
        elif status==0:
            content=self.entrada.get()
            position = content.find('*')  # Encuentra la posición del asterisco
            if position!= -1:
                codigo = content[(position + 1):]
                check = content[:position]
                if check.isdigit():
                    mult = int(check)
                else:
                    codigo = content
            else:
                codigo = content
                mult = 1
            valor = codigo if codigo.isdigit() else 0
            totalC=0
            resultados = [item for item in self.Bend.internal if item[2] == valor]
            res_ordenado = sorted(resultados, key=lambda x: x[3])

                        
            def encontrar_combinacion(numeros, objetivo):

                numeros_ordenados = sorted(numeros)
                mejor_suma = float('inf')
                mejor_combinacion = None
        
                for longitud in range(1, len(numeros_ordenados) + 1):
                    for combinacion in itertools.combinations(numeros_ordenados, longitud):
                        suma_actual = sum(combinacion)
                        if suma_actual >= objetivo:
                            if suma_actual == objetivo:
                                return combinacion
                            if suma_actual < mejor_suma:
                                mejor_suma = suma_actual
                                mejor_combinacion = combinacion
                return mejor_combinacion
            for x in res_ordenado:
                totalC+=x[3]
            print(totalC)
            if (not res_ordenado) or totalC< mult:
                self.mostrar_error("Producto NO Facturado",1)
                self.entrada.delete(0,tk.END)
            else:
                subC=0
                eliminacion=[]
                for x in res_ordenado:
                    subC+=x[3]
                    eliminacion.append(x)  
                    if x[3]>=mult and mult% x[4] ==0:
         
                        self.Bend.internal = [t for t in self.Bend.internal if not t[5]==x[5]]
                        RestoFacturado= x[3]- mult
                        self.Bend.nitem+=1
                        item=(x[0],x[1],x[2],RestoFacturado, x[4],self.Bend.nitem)
                        if RestoFacturado>0: self.Bend.internal.append(item)
                        self.items(status=2,Re=f'{mult}*{valor}')
                        return    
                    elif mult<=subC:
                        valores=[]
                        
                        for w in eliminacion:
                            valores.append(w[3])
                        resultado=encontrar_combinacion(valores,mult) 
                        sumainterna=0
                        for nums in resultado:
                            sumainterna+=nums
                            for i, t in enumerate(self.Bend.internal):
                                if t[3] == nums and t[2] == valor:
                                    del self.Bend.internal[i]  # Elimina el primer elemento que cumple la condición
                                    break 
                            print(self.Bend.internal)
                            
                           
                            self.items(status=2,Re=f'{nums}*{valor}')
                        resto=sumainterna-mult
                        if resto: self.items(status=0,Re=f'{resto}*{valor}')
                        return
    def mostrar_error(self, error, state=0):
        self.ppunbind()
        def dividir_cadena(cadena):
            return '\n'.join(textwrap.wrap(cadena, width=30))
        message= dividir_cadena(f"{error}")
        error_window = tb.Toplevel(self.app)
        try:
            self.passw.destroy()
        except:
            pass
            
        error_window.title("Error")
        error_window.geometry("600x400")
        error_window.resizable(False, False)  
        error_window.config(background="#39384B")
        ancho_pantalla = error_window.winfo_screenwidth()
        alto_pantalla = error_window.winfo_screenheight()
        self.app.focus_set()
        pos_x = (ancho_pantalla - 600) // 2
        pos_y = (alto_pantalla - 400) // 2
        error_window.geometry(f"{600}x{400}+{pos_x}+{pos_y}")
        label = tb.Label(error_window, text=f"⚠︎  {message}",font=("Arial", int(30*self.Bend.font)),  justify="center", foreground="#AB9F9F", background="#39384B")
        label.pack(pady=30)
        if not state:tb.Label(error_window, text= 'Contáctese con el técnico',font=("Arial", int(15*self.Bend.font)),  justify="center", foreground="red", background="#39384B").pack(pady=30)
        if state==4:
            self.app.bind("<Escape>", lambda event:(self.auditoriaBind(),  error_window.destroy()))
            close_button = tb.Button(error_window, text="Cerrar", style= "secondary",command= lambda: (error_window.destroy(),self.auditoriaBind()))       
        elif state==1:
            self.app.bind("<Escape>", lambda event: (error_window.destroy(), self.ppbind()))
            close_button = tb.Button(error_window, text="Cerrar", style= "secondary",command=lambda: (error_window.destroy(), self.ppbind()))
        elif state==5:
            self.app.bind("<Escape>", lambda event: (error_window.destroy(), self.preciobind()))
            close_button = tb.Button(error_window, text="Cerrar", style= "secondary",command=lambda: (error_window.destroy(), self.preciobind()))
        elif state==2:
            self.app.bind("<Escape>", lambda event: (error_window.destroy(), self.resumeBind()))
            close_button = tb.Button(error_window, text="Cerrar", style= "secondary",command= lambda: (error_window.destroy(), self.resumeBind()))
        elif state==3:
            self.app.bind("<Escape>", lambda event: (error_window.destroy(), self.SalesBind()))
            close_button = tb.Button(error_window, text="Cerrar", style= "secondary",command=lambda: (error_window.destroy(), self.SalesBind()))
        if state: close_button.pack(pady=30)
        error_window.transient()  
        error_window.attributes("-topmost", True) 
        error_window.grab_set()
        error_window.wait_window()
    def SalesBind(self):
        self.app.bind("<Escape>", lambda event : (self.sales.destroy(),self.ppunbind(event)))
        self.app.bind("<F1>", lambda event: self.cierre('z', event))
        self.app.bind("<F2>", lambda event: self.cierre('x', event))
        self.app.bind("<F3>", lambda event: self.Auditoria(event))
   
    def Sales(self):
        try:
            self.sales = tk.Frame(self.app)
            self.sales.config(background='#F1EAD7')
            self.sales.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.SalesBind()
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="Caja:", font=("Arial", int(30*self.Bend.font))).place(relx=0.05, rely=0.05, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="Fecha: ", font=("Arial", int(30*self.Bend.font))).place(relx=0.35, rely=0.05, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="Monto Ac.", font=("Arial", int(30*self.Bend.font))).place(relx=0.05, rely=0.15, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="Facturado SF", font=("Arial", int(30*self.Bend.font))).place(relx=0.3, rely=0.15, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="Total", font=("Arial", int(30*self.Bend.font))).place(relx=0.55, rely=0.15, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="Efectivo:", font=("Arial", int(30*self.Bend.font))).place(relx=0.05, rely=0.25, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="$4000", font=("Arial", int(30*self.Bend.font))).place(relx=0.3, rely=0.25, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="$4000", font=("Arial", int(30*self.Bend.font))).place(relx=0.55, rely=0.25, relwidth=0.2, relheight=0.05)

            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="Pago Elect:", font=("Arial", int(30*self.Bend.font))).place(relx=0.05, rely=0.35, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="$4000", font=("Arial", int(30*self.Bend.font))).place(relx=0.3, rely=0.35, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="$4000", font=("Arial", int(30*self.Bend.font))).place(relx=0.55, rely=0.35, relwidth=0.2, relheight=0.05)

            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="Tarjeta:", font=("Arial", int(30*self.Bend.font))).place(relx=0.05, rely=0.45, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="$4000", font=("Arial", int(30*self.Bend.font))).place(relx=0.3, rely=0.45, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="$4000", font=("Arial", int(30*self.Bend.font))).place(relx=0.55, rely=0.45, relwidth=0.2, relheight=0.05)

            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="Total:", font=("Arial", int(30*self.Bend.font))).place(relx=0.05, rely=0.55, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="$4000", font=("Arial", int(30*self.Bend.font))).place(relx=0.3, rely=0.55, relwidth=0.2, relheight=0.05)
            tb.Label(self.sales, background= '#F1EAD7', foreground= '#847C67', text="$4000", font=("Arial", int(30*self.Bend.font))).place(relx=0.55, rely=0.55, relwidth=0.2, relheight=0.05)
            cierre_total_btn = tb.Button(self.sales, text="Cierre Total [z]", style="Custom.TButton", command=lambda: self.cierre("z"))    
            cierre_total_btn.place(relx=0.05, rely=0.9, relwidth=0.15, relheight=0.05)
            cierre_parcial_btn = tb.Button(self.sales, text="Cierre Parcial [x]", style="Custom.TButton",command=lambda:(self.cierre("x")))
            cierre_parcial_btn.place(relx=0.35, rely=0.9, relwidth=0.15, relheight=0.05)
            auditoria_btn = tb.Button(self.sales, text="Auditoria", style="Custom.TButton", command=lambda: self.Auditoria())
            auditoria_btn.place(relx=0.65, rely=0.9, relwidth=0.15, relheight=0.05)
        except:
            self.mostrar_error("Error Fatal")
    def cierre(self, status, event=0):
            repuesta= messagebox.askokcancel(f"cierre {status}", f"Desea hacer un Cierre de caja {status}")
            if repuesta:
                self.call(status)
    def auditoriaBind(self):
        self.app.bind("<Escape>", lambda event: (self.auditoria.destroy(), self.SalesBind()))
    def Auditoria(self, event=0):
        self.auditoria= tk.Frame(self.app)
        self.auditoria.config(background='#F1EAD7')
        self.auditoriaBind()
        self.auditoria.place(relx=0, rely=0, relheight=1, relwidth=1)
        var1 = tk.BooleanVar(value=True)
        var2 = tk.BooleanVar(value=False)

        def manejar_seleccion(state):
            if state==1: 
                var2.set(False)    
            elif state==2: 
                var1.set(False)  
        def llamado(state):
            if state==1:

                Syyyy= S_fecha.get()[2:4]
                Smm= S_fecha.get()[5:7]
                Sdd= S_fecha.get()[8:10]
                Fyyyy= S_fecha.get()[2:4]
                Fmm= S_fecha.get()[5:7]
                Fdd= S_fecha.get()[8:10]
                S= Syyyy+Smm+Sdd if len(S_fecha.get()) == 10 and len(F_fecha.get()) == 10 else 0
                F=Fyyyy+Fmm+Fdd
            if state==1 and var1.get():self.call("AuditoriaF",S,F)  
            elif state==1 and var2.get():self.call("AuditoriaDF",S,F)   
            elif state==2 and var1.get():self.call("Auditoria2", S_numZ.get(), F_numZ.get())                      
            elif state==2 and var2.get():self.call("AuditoriaDZ", S_numZ.get(), F_numZ.get())        
        tb.Label(self.auditoria, text= "Por Fecha", background= '#F1EAD7', foreground= '#847C67',font=("Arial", int(30*self.Bend.font))).place(relx=0.245, rely=0.1016,)
        tb.Label(self.auditoria, text= "Por Num de Z", background= '#F1EAD7', foreground= '#847C67',font=("Arial", int(30*self.Bend.font))).place(relx=0.5586, rely=0.1016, )
        tb.Button(self.auditoria,text= "Imprimir", style="Custom.TButton",command= lambda: llamado(1)).place(relx=0.2334, rely=0.57, relwidth=0.14, relheight=0.048)
        tb.Button(self.auditoria,text= "Imprimir", style="Custom.TButton", command= lambda: llamado(2)).place(relx=0.5586, rely=0.57, relwidth=0.14, relheight=0.048)
        tk.Checkbutton(self.auditoria, text="Detallado",variable=var2, command=lambda: (manejar_seleccion(2)) ).place(relx=0., rely=0.9,relwidth=0.08, relheight=0.048)   
        tk.Checkbutton(self.auditoria, text="Resumida",variable=var1, command=lambda: (manejar_seleccion(1)) ).place(relx=0., rely=0.85,relwidth=0.08, relheight=0.048)          
        S_fecha= tb.Entry(self.auditoria, style="Custom.TButton",font=("arial", int(25 * self.Bend.font)), justify='center')
        F_fecha= tb.Entry(self.auditoria, style="Custom.TButton",font=("arial", int(25 * self.Bend.font)), justify='center')
        S_fecha.place(relx=0.205, rely=0.24, relwidth=0.18, relheight=0.048)
        F_fecha.place(relx=0.205, rely=0.3, relwidth=0.18, relheight=0.048)
        S_numZ= tb.Entry(self.auditoria, style="Custom.TButton",font=("arial", int(25 * self.Bend.font)), justify='center')
        F_numZ= tb.Entry(self.auditoria, style="Custom.TButton",font=("arial", int(25 * self.Bend.font)), justify='center')
        S_numZ.place(relx=0.54, rely=0.24, relwidth=0.18, relheight=0.048)
        F_numZ.place(relx=0.54, rely=0.3, relwidth=0.18, relheight=0.048)
        S_fecha.insert(0, f'{date.today()}')
        F_fecha.insert(0, f'{date.today()}')

    def facturacion_click(self, event=0, status=0):
        # Initialize payment counters
        card = 0
        cash = 0
        virtual = 0
        tcard = 0
        tcash = 0
        tvirtual = 0
        
        # Get payment amounts from the transaction
        if hasattr(self, 'R_efectivo_valor') and self.R_efectivo_valor.get():
            cash = float(self.R_efectivo_valor.get().replace('$', '').replace(',', ''))
            tcash = 1  # Count as one cash transaction
        if hasattr(self, 'R_tarjeta_valor') and self.R_tarjeta_valor.get():
            card = float(self.R_tarjeta_valor.get().replace('$', '').replace(',', ''))
            tcard = 1  # Count as one card transaction
        if hasattr(self, 'R_PagoElec_valor') and self.R_PagoElec_valor.get():
            virtual = float(self.R_PagoElec_valor.get().replace('$', '').replace(',', ''))
            tvirtual = 1  # Count as one virtual transaction
        
        # Calculate total payment
        total_payment = cash + card + virtual
        
        # If only cash payment, adjust to subtotal
        if tcash == 1 and tcard == 0 and tvirtual == 0:
            cash = self.Bend.subtotal
        # If combined payment, validate total
        elif total_payment != self.Bend.subtotal:
            self.mostrar_error("La suma de los pagos debe ser igual al total", 1)
            return
        
        # Update Caja1 table
        self.Bend.update_caja1(
            facturated=self.Bend.subtotal if status == 1 else 0 ,
            non_facturated=self.Bend.subtotal if status == 2 else 0,
            card=card,
            cash=cash,
            virtual=virtual,
            tcard=tcard,
            tcash=tcash,
            tvirtual=tvirtual,
            tcancelled=0,
            cancelled=0
        )
        self.resume.destroy()
        self.ppbind()
        if status == 1:
            self.call("tique", event)
        elif status == 2:
            self.cancelar_anular(status=1)

caja()