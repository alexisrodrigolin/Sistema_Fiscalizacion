import tkinter as tk
import ttkbootstrap as tb   
import priceB 
import textwrap
from tkinter import messagebox

class main():
    def __init__(self):
        self.Back= priceB.connection()

        self.app= tb.Window(themename= "darkly",title= "PriceSyncer",size= [1024, 768])
        self.create_widget_menu()
        self.app.state('zoomed')

        self.settings(col=15, row=15)
        self.app.mainloop()
    def create_widget_menu(self):
        self.numberCaja= tb.Label(self.app, text="PriceSyncer", font=("Arial", int(35 * self.Back.font),"italic","bold"),anchor="center")
        self.numberCaja.grid(column=7,  row=3)  
        self.User= tb.Entry(self.app, justify="center")
        self.Password= tb.Entry(self.app,justify="center", show="*")
        self.enter= tb.Button(self.app, text="Enter", command=self.check, style= "darkly")
        
        self.enter.grid(column=7,row=7)
        self.Password.grid(column=7, row=6,sticky= "n")
        self.User.grid(column=7, row=5)

        
    def create_widget_precio(self,bind=0):
        if bind==0:
            def actualizar_texto(opcion_seleccionada):
                # Cambia el texto del Menubutton
                self.P_menubutton.config(text=opcion_seleccionada)
                self.P_control_value.set(opcion_seleccionada)
            self.P_control_value= tb.StringVar(value="1")
            self.delete_widgets()
            self.P_id= tb.Label(self.app, text= "Codigo:", font= ("Arial",  int(15 * self.Back.font)), )
            self.P_id_value= tb.Entry(self.app, style= "darkly",width=15)
            self.P_plu= tb.Label(self.app, text= "PLU:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_plu_value= tb.Entry(self.app, style= "darkly",width=15)
            self.P_plu2= tb.Label(self.app, text= "PLU 2:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_plu2_value= tb.Entry(self.app, style= "darkly",width=15)
            self.P_precio= tb.Label(self.app, text= "Precio:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_precio_value= tb.Entry(self.app, style= "darkly", width=15, font= ("Arial",15))
            self.P_marca= tb.Label(self.app, text= "Marca:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_marca_value= tb.Entry(self.app, style= "darkly", width=15, font= ("Arial",  int(15 * self.Back.font)))
            self.P_descripcion= tb.Label(self.app, text= "Descripcion:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_descripcion_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=21)
            self.P_tipo= tb.Label(self.app, text= "Tipo/Sabor:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_tipo_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=20)
            self.P_cantidad= tb.Label(self.app, text= "Cantidad:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_cantidad_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)

            self.P_control_value = tk.StringVar(value="Unidad:")
            self.P_menubutton = tb.Menubutton(self.app,textvariable=self.P_control_value, width=9,style= "darkly", )
            self.P_menu_op = tb.Menu(self.P_menubutton)
            opciones=[ "Unidad","ml","Gramos", "Litros",  "KilosGramos", "Metros", "m³"]
            for opcion in opciones:
                self.P_menu_op.add_command(
                    label=opcion,
                    command=lambda o=opcion: actualizar_texto(o)
                )

            self.P_menubutton.config(menu=self.P_menu_op)


            barras=tb.Label(self.app, text="////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
            barras1=tb.Label(self.app, text="////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
            barras2=tb.Label(self.app, text="////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

            self.P_departamento= tb.Label(self.app, text= "Deepartamento:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_departamento_value= tb.Entry(self.app, style= "darkly", width=14, font= ("Arial",  int(15 * self.Back.font)))
            self.P_pasillo= tb.Label(self.app, text= "Pasillo:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_pasillo_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=14)
            self.P_costo= tb.Label(self.app, text= "Costo s.IVA:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_costo_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_iva= tb.Label(self.app, text= "IVA:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_iva_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_ganancia= tb.Label(self.app, text= "Ganancia %:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_ganancia_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_preReco= tb.Label(self.app, text= f"Precio recomendado \n para venta: $", font= ("Arial",  int(15 * self.Back.font)), foreground="#B6B6B6")

            self.P_preCan= tb.Label(self.app, text= f"<<<Precio por Cantidad>>>", font= ("Arial",  int(15 * self.Back.font)))
            self.P_cantidad1= tb.Label(self.app, text= "Cantidad 1:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_cantidad1_value= tb.Entry(self.app, style= "darkly", width=7, font= ("Arial",  int(15 * self.Back.font)))
            self.P_cantidad2= tb.Label(self.app, text= "Canridad 2:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_cantidad2_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_cantidad3= tb.Label(self.app, text= "Cantidad 3:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_cantidad3_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_precioC1= tb.Label(self.app, text= "Precio x Uni:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_precioC1_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_precioC2= tb.Label(self.app, text= "Precio x Uni:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_precioC2_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_precioC3= tb.Label(self.app, text= "Precio x Uni:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_precioC3_value= tb.Entry(self.app, style= "darkly", font= ("Arial",int(15 * self.Back.font)), width=7)
            self.P_guardar= tb.Button(self.app, text="Guardar y emitir", bootstyle="warning-outline")
            self.P_guardarSin= tb.Button(self.app, text="Guadar sin emitir", bootstyle="warning-outline",command=self.save)
            self.P_borrar= tb.Button(self.app, text="Borrar", bootstyle="warning-outline")
            self.P_menu= tb.Button(self.app, text="Menu", bootstyle="warning-outline", command= self.menu)
            self.P_borrarOf= tb.Button(self.app, text="Borrar Oferta", bootstyle="warning-link", command=self.borrarOf)
            self.P_buscar= tb.Button(self.app, text="Buscar", bootstyle="warning-outline")
            self.P_fecha= tb.Label(self.app, text="Fecha de Modificacion:", font= ("Arial", int(20 * self.Back.font)), foreground="#7B7A7A" )

    #row 1
            self.P_id.place(relx=0.05, rely=0.07)
            self.P_id_value.place(relx=0.14, rely=0.07, relheight=0.0339, relwidth=0.17)

            self.P_plu.place(relx=0.05, rely=0.12)
            self.P_plu_value.place(relx=0.14, rely=0.12, relheight=0.0339, relwidth=0.17)

            self.P_plu2.place(relx=0.47, rely=0.07)
            self.P_plu2_value.place(relx=0.55, rely=0.07, relheight=0.0339, relwidth=0.17)

            self.P_precio.place(relx=0.47, rely=0.12)
            self.P_precio_value.place(relx=0.55, rely=0.12,  relwidth=0.17)


            self.P_marca.place(relx=0.0156, rely=0.23)
            self.P_marca_value.place(relx=0.0156, rely=0.27, relheight=0.04, relwidth=0.21) 
            self.P_descripcion.place(relx=0.24,rely= 0.23)
            self.P_descripcion_value.place(relx= 0.24, rely=0.27, relheight=0.04, relwidth=0.27)      
            self.P_tipo.place(relx=0.52, rely=0.23)
            self.P_tipo_value.place(relx=0.52, rely=0.27, relheight=0.04, relwidth=0.26) 
            self.P_cantidad.place(relx=0.7871,rely= 0.23)
            self.P_cantidad_value.place(relx= 0.7871, rely=0.27, relheight=0.04, relwidth=0.1)  
            self.P_menubutton.place(relx=0.9102 ,rely=0.27,relheight=0.040, relwidth=0.075 )
            barras.place(relx=0, rely=0.3411)
            self.P_departamento.place(relx= 0.0156, rely=0.3906)
            self.P_departamento_value.place(relx= 0.163, rely=0.3906, relheight=0.04, relwidth=0.14)
            self.P_pasillo.place(relx=0.0156, rely=0.45)
            self.P_pasillo_value.place(relx=0.163, rely= 0.45, relheight=0.04, relwidth=0.14)
            self.P_costo.place(relx= 0.36, rely=0.3906)
            self.P_costo_value.place(relx= 0.4785, rely=0.3906, relheight=0.04, relwidth=0.1)
            self.P_iva.place(relx= 0.36, rely=0.45)
            self.P_iva_value.place(relx= 0.4785, rely=0.45, relheight=0.04, relwidth=0.1)
            self.P_ganancia.place(relx=0.6025, rely=0.3906)
            self.P_ganancia_value.place(relx=0.739 , rely=0.3906, relheight=0.04, relwidth=0.14)
            self.P_preReco.place(relx=0.6816, rely=0.4557)
            barras1.place(relx=0, rely=0.5287)
            self.P_preCan.place(relx= 0.0273, rely= 0.5664)
            self.P_cantidad1.place(relx=0.0156, rely=0.63)
            self.P_cantidad1_value.place(relx=0.135, rely=0.63, relheight=0.04, relwidth=0.14)
            self.P_cantidad2.place(relx=0.3369, rely=0.63)
            self.P_cantidad2_value.place(relx=0.455, rely=0.63, relheight=0.04, relwidth=0.14)
            self.P_cantidad3.place(relx=0.6719, rely=0.63)
            self.P_cantidad3_value.place(relx=0.79, rely=0.63, relheight=0.04, relwidth=0.14)
            self.P_precioC1.place(relx=0.0156, rely=0.6914)
            self.P_precioC1_value.place(relx=0.135, rely=0.6914, relheight=0.04, relwidth=0.14)
            self.P_precioC2.place(relx=0.3369, rely=0.6914)
            self.P_precioC2_value.place(relx=0.455, rely=0.6914, relheight=0.04, relwidth=0.14)
            self.P_precioC3.place(relx=0.6719, rely=0.6914)
            self.P_precioC3_value.place(relx=0.79, rely=0.6914, relheight=0.04, relwidth=0.14)
            barras2.place(relx=0, rely=0.7917)
        
            self.P_guardar.place(relx= 0.0283, rely=0.872)
            self.P_guardarSin.place(relx=0.2246,rely=0.872)
            self.P_borrar.place(relx=0.3984,rely=0.872)
            self.P_menu.place(relx=0.50,rely=0.872)
            self.P_borrarOf.place(relx=0.837,rely=0.5664)
            self.P_buscar.place(relx=0.874,rely=0.0911)
            self.P_fecha.place(relx=0.6426,rely=0.872)

            
            self.orden= ['plu', 'plu2','precio','marca','descripcion', 'tipo', 'cantidad', 'control',
                        'departamento', 'pasillo', 'costo','iva', 'ganancia', 
                        "cantidad1",'precioC1', 'cantidad2', 'precioC2','cantidad3', 'precioC3']      
            self.colsql= ['PLU','PLU2', 'Precio','Marca','Descripcion', 'Tipo_Sabor','Cantidad', 'Unidad',
                        'Departamento', 'Pasillo', 'Costo','IVA', 'Ganancia', 
                        "Cant1",'Precio1', 'Cant2', 'Precio2','Cant3', 'Precio3']  
        self.disable_entries(exclude=[self.P_id_value])
        self.P_precio_value.bind("<FocusOut>", lambda event:self.agregar_sim(status=0, event=event))
        self.P_precioC1_value.bind("<FocusOut>", lambda event:self.agregar_sim(status=1, event=event))
        self.P_precioC2_value.bind("<FocusOut>", lambda event:self.agregar_sim(status=2, event=event))
        self.P_precioC3_value.bind("<FocusOut>", lambda event:self.agregar_sim(status=3, event=event))
        self.P_cantidad1_value.bind("<FocusOut>", lambda event:self.integral(status=1, event=event))
        self.P_cantidad2_value.bind("<FocusOut>", lambda event:self.integral(status=2, event=event))
        self.P_cantidad3_value.bind("<FocusOut>", lambda event:self.integral(status=3, event=event))
        self.app.bind("<Escape>", self.menu)  
        self.app.bind("<Return>", self.buscar)  
        self.app.bind("<F1>", self.SearchByName)
    def SearchByName(self,event=0):
           
            
            self.frame = tb.Frame(self.app)
            self.frame.place(rely=0,relheight=1,relwidth=1,relx=0)
            
            tb.Label(self.frame, text="Búsqueda General (marca, descripción, sabor):").pack(pady=5)
            self.entry_busqueda = tb.Entry(self.frame, width=50)
            self.entry_busqueda.pack(pady=5)
            self.entry_busqueda.bind("<Return>", self.realizar_busqueda)

            tb.Label(self.frame, text="Cantidad exacta (Sin unidad):").pack(pady=5)
            self.entry_cantidad = tb.Entry(self.frame, width=20)
            self.entry_cantidad.pack(pady=5)
            self.entry_cantidad.bind("<Return>", self.realizar_busqueda)
            
            self.btn_buscar = tb.Button(
                self.frame, text="Buscar", command=self.realizar_busqueda, 
            )
            self.btn_buscar.pack(pady=10)

            self.tree = tb.Treeview(
                self.frame, 
                columns=("Marca", "Descripción", "Tipo/Sabor", "Cantidad"), 
                show="headings",
                height=15
            )
            self.tree.heading("Marca", text="Marca")
            self.tree.heading("Descripción", text="Descripción")
            self.tree.heading("Tipo/Sabor", text="Tipo/Sabor")
            self.tree.heading("Cantidad", text="Cantidad ")
            self.tree.pack(fill="both", expand=True)
            
            # Scrollbar
            scrollbar = tb.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
            self.tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
        
        
    def realizar_busqueda(self, event=None):
            terminos_general = self.entry_busqueda.get().strip()
            cantidad = self.entry_cantidad.get().strip()
            
            # Limpiar resultados
            self.tree.delete(*self.tree.get_children())
            
            resultados = self.Back.buscar_productos(terminos_general, cantidad)
            print(resultados)
            if not resultados:
                messagebox.showinfo("Información", "No se encontraron coincidencias")
                return
            
            for producto in resultados:
                self.tree.insert("", 'end', values=(
                    producto[4],
                    producto[5],
                    producto[6],
                    producto[7]
                ))
                

    def borrarOf(self):
        Of= ["cantidad1",'precioC1', 'cantidad2', 'precioC2','cantidad3', 'precioC3']
        for x in Of:
            command= getattr(self, f'P_{x}_value')
            command.delete(0, tb.END)

    def save(self):
        command= []
        precio= self.P_precio_value.get()
        dic={'Precio':f'{precio[2:]}'}

        for x in range(len(self.orden)):
            com=getattr(self, f'P_{self.orden[x]}_value')
            command.append(com.get())
            if not (command[x]== '' or x==2 or x==14 or x==16 or x==18):
                dic.update({f'{self.colsql[x]}':f'{command[x]}'})
            elif (not command[x]== '') and (x==14 or x==16 or x==18):
                dic.update({f'{self.colsql[x]}':f'{command[x][2:]}'})  
            elif command[x]=='':
                dic.update({f'{self.colsql[x]}':'NULL'})
        self.Back.guardar(dic, self.P_id_value.get())

        self.clean()

    def buscar(self,event=0):
        self.app.bind("<Escape>", self.clean)
        value= self.P_id_value.get()
        if not value.isdigit():
            self.P_id_value.delete(0, tk.END)
            return
        
        results=self.Back.search(codigo=value)
        if results:
            self.app.unbind("<Return>")
            result=results[0]
            self.able_entries()

            self.P_id_value.delete(0, tb.END)
            self.P_id_value.insert(0, str(result[0]))

            self.P_id_value.config(state= "readonly")

            for x, y in enumerate(self.orden, start=1):
                command= getattr(self, f'P_{y}_value')
                if result[x] and not (x==3 or x==8 or x==15 or x==17 or x==19):
                    command.insert(0, result[x])
                elif result[x] and x==8:
                    self.P_control_value.set(result[x])
                elif result[x] and (x==3 or x==15 or x==17 or x==19):
                    command.insert(0, f"$ {result[x]:.2f}")
                else:
                    continue
        else:
            self.buscar() 
                  
    def clean(self, event=0):

        self.P_id_value.config(state= 'normal')
        for widget in self.app.winfo_children():
            if isinstance(widget, tb.Entry):
                widget.delete(0, tb.END)
        self.P_control_value.set('Unidad:') 
        self.app.bind("<Return>", self.buscar)
        self.app.bind("<Escape>", self.menu) 
        self.disable_entries(exclude=[self.P_id_value])

    def agregar_sim(self, status=0, event=None):
            # Mapear los status a los diferentes Entry widgets
            entries = {
                0: self.P_precio_value,
                1: self.P_precioC1_value,
                2: self.P_precioC2_value,
                3: self.P_precioC3_value
            }
            
            # Obtener el Entry correspondiente al status
            entry = entries.get(status)
            if not entry:
                return

            contenido = entry.get()
            
            # Eliminar símbolos de formato existentes
            raw_value = contenido.replace("$", "").strip()
            
            try:
                # Intentar convertir a float
                numeric_value = float(raw_value)
                # Formatear con 2 decimales y símbolo $
                formatted = f"$ {numeric_value:.2f}"
                entry.delete(0, tk.END)
                entry.insert(0, formatted)
            except ValueError:
                # Si no es número válido, limpiar el campo
                entry.delete(0, tk.END)
     
    def integral(self,status, event=0):
            entries = {

                1: self.P_cantidad1_value,
                2: self.P_cantidad2_value,
                3: self.P_cantidad3_value
            }
            entry=entries.get(status)
            valor=entry.get()
            if status==1:
                valor1=self.P_cantidad2_value.get()
                valor2=self.P_cantidad3_value.get()
            elif status==2:
                valor1=self.P_cantidad1_value.get()
                valor2=self.P_cantidad3_value.get()
            elif status==3:
                valor1=self.P_cantidad2_value.get()
                valor2=self.P_cantidad1_value.get()
            if valor=="":
                pass
            elif not valor.isdigit():
                entry.delete(0, tk.END)
                messagebox.showerror("Error", "Verifique el valor")
            elif valor==valor1 or valor==valor2: 
                entry.delete(0, tk.END)
                messagebox.showerror("Error", "Cantidad de Oferta Repetida")
    def entrada(self):
            self.precio= tb.Button(self.app,
            text="Precio", style= "darkly",command=self.create_widget_precio)
            self.etiquetas= tb.Button(self.app,
            text = "etiquetas", style= "darkly")
        
            self.etiquetas.grid(column=7, row=11, )
            self.precio.grid(column=7,row=10, )
    def menu(self,event=0):
            self.delete_widgets()       
            self.app.unbind("<Return>")
            self.app.unbind("<Escape>")
            self.numberCaja= tb.Label(self.app, text="PriceSyncer", font=("Arial",int(35 * self.Back.font),"italic","bold"),anchor="center")
            self.numberCaja.grid(column=7,  row=3)
            self.entrada()
    def disable_entries(self, exclude=[]):
        for widget in self.app.winfo_children():
            if isinstance(widget, tb.Entry) and widget not in exclude:
                widget.config(state="disabled")
        self.P_guardar.config(state='disabled')
        self.P_guardarSin.config(state='disabled')
        self.P_borrar.config(state='disabled')
        self.P_borrarOf.config(state='disabled')
        self.P_menubutton.config(state='disabled')
    def able_entries(self, exclude=[]):
        for widget in self.app.winfo_children():
            if isinstance(widget, tb.Entry) and widget not in exclude:
                widget.config(state="normal")
        self.P_guardar.config(state='normal')
        self.P_guardarSin.config(state='normal')
        self.P_borrar.config(state='normal')
        self.P_borrarOf.config(state='normal')
        self.P_menubutton.config(state='normal')

    def delete_widgets(self):
        
        for widget in self.app.winfo_children():
            widget.destroy()
        

    def check(self, event=None):
        key=0
        username = self.User.get()  
        password= self.Password.get()
        if username== 'admin':
            if password== self.Back.datos['AdminPass']:
                self.app.unbind("<Return>")
                self.entrada()
                config= tb.Button(self.app, style= "darkly", text= "Configuration", command= lambda: self.conf(0))
                config.grid(column=7, row=12)
                key=1
            elif password== 'rksystems2505':
                self.app.unbind("<Return>")
                self.entrada()
                config= tb.Button(self.app, style= "darkly", text= "Configuration", command= lambda: self.conf(1))
                config.grid(column=7, row=12)
                key=1
        try:
            self.Back.Connection()
        
        except:
            self.mostrar_error("Error de Conexion con Base Central")
            return
        if self.Back.validate_user(username,password):
            self.entrada()
            self.app.unbind("<Return>")
            try:
                self.error.grid_forget()
            except:
                pass
        elif key==1:
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
        
        
    def mostrar_error(self, error, state=0):
            def dividir_cadena(cadena):
                return '\n'.join(textwrap.wrap(cadena, width=30))
            message= dividir_cadena(f"{error}")
            error_window = tb.Toplevel(self.app)

            error_window.title("Error")
            error_window.geometry("600x400")
            error_window.resizable(False, False)  
            error_window.config(background="#39384B")
            ancho_pantalla = error_window.winfo_screenwidth()
            alto_pantalla = error_window.winfo_screenheight()
            pos_x = (ancho_pantalla - 600) // 2
            pos_y = (alto_pantalla - 400) // 2
            error_window.geometry(f"{600}x{400}+{pos_x}+{pos_y}")
            label = tb.Label(error_window, text=f"⚠︎  {message}",font=("Arial", int(30*self.Back.font)),  justify="center", foreground="#AB9F9F", background="#39384B")
            label.pack(pady=30)
            if not state:tb.Label(error_window, text= 'Contáctese con el técnico',font=("Arial", int(15*self.Back.font)),  justify="center", foreground="red", background="#39384B").pack(pady=30)
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
    def conf(self, status=0):
        cfg= tk.Frame(self.app, )
        cfg.place(relx=0, rely=0, relheight=1, relwidth=1)
        def save():
            repuestas=messagebox.askokcancel('Save', 'Desea guardar los cambios?')
            if repuestas:
                self.Back.datos['AdminPass']= passwordA.get()
                self.Back.datos['EntryPass']= passwordE.get()

  
                if status==1: 
                    self.Back.datos['Db']= Db.get()
                    self.Back.datos['User']= DbU.get()
                    self.Back.datos['Password']= DbP.get()[5:] 
                    self.Back.datos['Font']= font.get()            
                self.Back.writeCfg()
                cfg.destroy()
            


        tb.Label(cfg, text="Contraseña Entrada:",font=("arial", int(30 * self.Back.font))).pack()
        passwordE=tb.Entry(cfg,font=("arial", int(15 * self.Back.font)),justify="center") 
        passwordE.pack()
        tb.Label(cfg, text="Contraseña Administrador:",font=("arial", int(30 * self.Back.font))).pack()
        passwordA=tb.Entry(cfg,font=("arial", int(15 * self.Back.font)),justify="center") 
        passwordA.pack()
        tb.Label(cfg, text="#Mantener Precaución al manipular las configuraciones", foreground="grey").pack()

        passwordA.insert(0, self.Back.datos['AdminPass'])
        passwordE.insert(0, self.Back.datos['EntryPass'])


        if status== 1:
            tb.Label(cfg, text="Database:",font=("Arial", int(30 * self.Back.font))).pack()
            Db=tb.Entry(cfg,font=("Arial", int(15 * self.Back.font)),justify="center") 
            Db.pack()
            tb.Label(cfg, text="Db User:",font=("arial", int(30 * self.Back.font))).pack()
            DbU=tb.Entry(cfg,font=("arial", int(15 * self.Back.font)),justify="center") 
            DbU.pack()
            tb.Label(cfg, text="Db Password:",font=("arial", int(30 * self.Back.font))).pack()
            DbP=tb.Entry(cfg,font=("arial", int(15 * self.Back.font)),justify="center") 
            DbP.pack()
            Db.insert(0, self.Back.datos['Db'])
            DbU.insert(0, self.Back.datos['User'])
            DbP.insert(0, f"dadds{self.Back.datos['Password']}")
            tb.Label(cfg, text="Font:",font=("arial", int(30 * self.Back.font))).pack()
            font=tb.Entry(cfg,font=("arial", int(15 * self.Back.font)),justify="center") 
            font.pack()
            font.insert(0, self.Back.datos['Font'])
        tb.Button(cfg, style= "darkly", text="Guardar", command=save).pack(pady=10)
        tb.Button(cfg, text="Menu", style= "darkly", command=cfg.destroy).pack(pady=10)
main()
        