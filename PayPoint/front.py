import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import back
import textwrap
from tkinter import messagebox
from datetime import date


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
        self.buttons = []
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
        try:
            self.delete_widgets()
            detallado = tb.Frame(self.app, )
            scrollbar = tb.Scrollbar(detallado, orient="vertical", style="Custom.Vertical.TScrollbar")
            tree = ("Cantidad", "Descripcion", "Monto")
            self.detalles = tb.Treeview(detallado, columns=tree, show="headings", style="Custom.Treeview",
                                        yscrollcommand=scrollbar.set)
            self.detalles.heading("Cantidad", text="Cantidad", anchor="w")
            self.detalles.heading("Descripcion", text="Descripcion", anchor="w")
            self.detalles.heading("Monto", text="Precio", anchor="center")
            self.detalles.column("Cantidad", width=50, anchor="w")
            self.detalles.column("Descripcion", width=200, anchor="w")
            self.detalles.column("Monto", width=100, anchor="center")
            self.detalles.insert('', 'end', values=(" ", " ", " "))
            scrollbar.config(command=self.detalles.yview)
            self.detalles.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            self.total = tb.Label(self.app,
                                text=f"$ {self.Bend.subtotal:.2f}",
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

            button1 = tb.Button(self.app, bootstyle="dark", text="Precio")
            button1.place(relx=0.9, rely=0.25, relheight=0.07, relwidth=0.1)
            self.buttons.append(button1)
            button2 = tb.Button(self.app, bootstyle="info", text="Cancelar")
            button2.place(relx=0.9, rely=0.32, relheight=0.07, relwidth=0.1)
            self.buttons.append(button2)
            button3 = tb.Button(self.app, bootstyle="info", text="Anular")
            button3.place(relx=0.9, rely=0.39, relheight=0.07, relwidth=0.1)
            self.buttons.append(button3)
            button4 = tb.Button(self.app, bootstyle="dark", text="Suspender")
            button4.place(relx=0.9, rely=0.5, relheight=0.07, relwidth=0.1)
            self.buttons.append(button4)
            button5 = tb.Button(self.app, bootstyle="dark", text="Facturado")
            button5.place(relx=0.9, rely=0.57, relheight=0.07, relwidth=0.1)
            self.buttons.append(button5)
            button6 = tb.Button(self.app, bootstyle="dark", text="Nota Credito")
            button6.place(relx=0.9, rely=0.64, relheight=0.07, relwidth=0.1)
            self.buttons.append(button6)

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
        com=tb.Entry(cfg,style="Custom.TButt    on",font=("arial", int(15 * self.Bend.font)),justify="center") 
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

    def items(self, event=0):
        content = self.entrada.get()
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
        if not result:
            self.mostrar_error("Articulo NO Registrado",1)
        else:
            net = ''
            value = result[5] * mult
            for x in range(3):
                if result[x]: net += f"{result[x]} "
            self.detalles.insert('', 'end', values=(f"{mult}", f"{net}", f"$ {value:.2f} "))
            self.Bend.suma(Descripcion=f"{net}", Precio=result[5], Plu=f"{codigo}", Cantidad=mult)
            self.total.config(text=f'$ {self.Bend.subtotal:.2f}')
            self.cantidad.config(text=f'{self.Bend.cant}')


    def almacen(self, event, type):
        content = self.entrada.get()[:-1] if type == 'Almacén' else self.entrada.get()
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
        if codigo == 0:
            self.mostrar_error(f"Verifique el valor: {content}",1)
        else:
            value = mult * codigo
            self.detalles.insert('', 'end', values=(f"{mult}", f"{type}", f"$ {value:.2f} "))
            self.Bend.suma(Descripcion=f"{type}", Cantidad=mult,  Precio=codigo, Plu='11111111')
            self.total.config(text=f'$ {self.Bend.subtotal:.2f}')
            self.cantidad.config(text=f'{self.Bend.cant}')

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
        self.app.bind("<Return>", self.items)
        self.app.bind("<+>", lambda event: self.almacen(event, "Almacén"))
        self.app.bind("<F2>", lambda event: self.cancelar_anular(event=event, status=0))
        self.app.bind("<F3>", lambda event: self.cancelar_anular(event=event, status=1))
        self.app.bind("<F4>", self.Resume)
        self.app.bind("<F5>", lambda event: self.almacen(event, "Fiambrería"))
        self.app.bind("<F6>", lambda event: self.almacen(event, "Verdulería"))
        self.app.bind("<F7>", lambda event: self.almacen(event, "Carnicería"))
        self.app.bind("<F8>", lambda event: self.almacen(event, "Frío/Bolsa"))
        self.app.bind("<F9>", lambda event: self.almacen(event, "Envase"))
        self.app.bind("<F10>", lambda event: self.almacen(event, "Bazar"))
        self.entrada.focus()


    def menu(self, event=0):
        if self.Bend.subtotal == 0:
            self.ppunbind()
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
        R_bonificacion_valor = tb.Entry(self.resume, style='Custom.TButton',
                                        font=("arial", int(25 * self.Bend.font)), justify='center')
        R_total = tb.Label(self.resume, text='Total:', background='#F1EAD7', foreground='#847C67',
                           font=("arial", int(70 * self.Bend.font)))
        R_total_valor = tb.Label(self.resume, text=f'$ {self.Bend.subtotal:.2f}',
                                 font=('arial', int(70 * self.Bend.font)), background='#F1EAD7',
                                 foreground='#847C67')
        R_bonificacion = tb.Label(self.resume, text='Bonificación %',
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
        self.R_facturacion= tb.Button(self.resume, text= 'Facturacion', style="Custom.TButton",command=lambda:self.call("tique"))
        self.R_efectivo_valor.place(relx= 0.3244, rely= 0.3945, relwidth=0.17)
        self.R_PagoElec_valor.place(relx= 0.3244, rely= 0.4557, relwidth=0.17)
        self.R_tarjeta_valor.place(relx= 0.3244, rely= 0.5182, relwidth=0.17)
        self.R_facturacion.place(relx= 0.35, rely=0.75, relwidth=0.1)
        R_efectivo.place(relx=0.0508, rely=0.3945)
        R_bonificacion_valor.place(relx= 0.72, rely= 0.1966, relwidth=0.06 )
        R_PagoElec.place(relx=0.0508, rely=0.4557)
        R_Tarjeta.place(relx=0.0508, rely=0.5182)
        R_bonificacion.place(relx=0.54, rely=0.1966)
        R_total.place(relx=0.032, rely=0.0677)
        R_total_valor.place(relx=0.65, rely=0.0677)
        R_monto.place(relx= 0.0508, rely= 0.6)
        self.R_monto_valor.place(relx= 0.3244, rely= 0.6)
        R_vuelto.place(relx= 0.0508, rely= 0.66)
        self.R_vuelto_valor.place(relx= 0.3244, rely= 0.66)
        self.R_efectivo_valor.focus()       
        self.R_suma=0
        self.resumeBind()
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
                    widget.insert(0, f"$ {float(numero2):.2f}") 
                else:
                    if numero.replace(".", "", 1).isdigit() and numero.count(".") < 2:
                        widget.delete(0, tk.END)  
                        widget.insert(0, f"$ {float(numero):.2f}")
                    else:
                        widget.delete(0, tk.END)  
            elif contenido.isdigit() or (contenido.replace(".", "", 1).isdigit() and contenido.count(".") < 2):
                widget.delete(0, tk.END)  
                widget.insert(0, f"$ {float(contenido):.2f}") 
            else:
                widget.delete(0, tk.END)
            self.R_suma=0
            for x in (self.R_efectivo_valor, self.R_PagoElec_valor, self.R_tarjeta_valor):
                val=x.get()
                result= float(val[2:]) if not val == "" else 0
                self.R_suma+= result
            R_vueltos= self.R_suma - self.Bend.subtotal
            self.R_vuelto_valor.config(text= f"$ {R_vueltos:.2f}")
            self.R_monto_valor.config(text= f"$ {self.R_suma:.2f}")

    def resumeBind(self):

        self.R_efectivo_valor.bind("<Return>", lambda event : self.enter_as_tab(event))
        self.R_PagoElec_valor.bind("<Return>", lambda event : self.enter_as_tab(event))
        self.R_tarjeta_valor.bind("<Return>", lambda event: (self.resume.focus_force(), self.call("tique",event=event)))
        self.R_efectivo_valor.bind("<FocusOut>", lambda event: self.sim(1, event))
        self.R_PagoElec_valor.bind("<FocusOut>", lambda event: self.sim(2, event))
        self.R_tarjeta_valor.bind("<FocusOut>", lambda event: self.sim(3, event))
        self.app.bind("<F4>", lambda event: self.call("tique", event))
        self.app.bind("<Escape>", lambda event: (self.resume.destroy(), self.ppbind()))
        self.app.bind("<F6>", lambda event: self.cancelar_anular(status=1, event=event))
    def call(self, command,extra=0, extra1=0, event=0):
        result= self.Bend.main(f"{command}", extra, extra1) if extra1 else self.Bend.main(f"{command}")
        if command== "tique":
            if self.R_suma >= self.Bend.subtotal:
                if not result:
                    self.cancelar_anular(status=1)
                else:
                    self.mostrar_error(f"{result}",2) 
            else: 
                self.mostrar_error("El Monto es menor al Total",2)

        elif command== "z" or command=="x":
            if result: self.mostrar_error(f"{result}",3)

        elif command== 'AuditoriaDZ' or command=='AuditoriaDF'or command=='AuditoriaF'or command=='AuditoriaZ':
            if result: self.mostrar_error(f"{result}",4)

    def cancelar_anular(self, status, event=0):
        if status ==1:
            self.Bend.suma(refresh=1)
            self.detalles.delete(*self.detalles.get_children())
            self.cantidad.config(text= f'{self.Bend.cant}')
            self.total.config(text=f'$ {self.Bend.subtotal:.2f}')
        else:
            pass

    def mostrar_error(self, error, state=0):
        def dividir_cadena(cadena):
            return '\n'.join(textwrap.wrap(cadena, width=30))
        message= dividir_cadena(f"{error}")
        error_window = tb.Toplevel(self.app)
        self.ppunbind()
        error_window.title("Error")
        error_window.geometry("600x400")
        error_window.resizable(False, False)  
        error_window.config(background="#39384B")
        ancho_pantalla = error_window.winfo_screenwidth()
        alto_pantalla = error_window.winfo_screenheight()
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
        print('1')
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



caja()