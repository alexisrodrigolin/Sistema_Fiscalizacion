from datetime import date
import tkinter as tk
import ttkbootstrap as tb   
import priceB 
import textwrap
from tkinter import messagebox
from reportlab.lib.utils import simpleSplit
import os
import subprocess
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.graphics.barcode import code128, eanbc, createBarcodeDrawing, code39, usps,usps4s,ecc200datamatrix,code93
from reportlab.lib.colors import black, red
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPM



class main():
    def __init__(self):
        self.Back= priceB.connection()

        self.app= tb.Window(themename= "darkly",title= "PriceSyncer",size= [1024, 768])
        try:
            self.app.iconbitmap('price.ico')
        except Exception as e:
            print(f'No se pudo cargar el icono: {e}')
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
        self.User.focus()
        
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
            opciones=[ "u","ml","gr", "L",  "Kl",'mg', "Mt", "m³"]
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
            self.P_cantidad2= tb.Label(self.app, text= "Cantidad 2:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_cantidad2_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_cantidad3= tb.Label(self.app, text= "Cantidad 3:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_cantidad3_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_precioC1= tb.Label(self.app, text= "Precio x Uni:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_precioC1_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_precioC2= tb.Label(self.app, text= "Precio x Uni:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_precioC2_value= tb.Entry(self.app, style= "darkly", font= ("Arial",  int(15 * self.Back.font)), width=7)
            self.P_precioC3= tb.Label(self.app, text= "Precio x Uni:", font= ("Arial",  int(15 * self.Back.font)))
            self.P_precioC3_value= tb.Entry(self.app, style= "darkly", font= ("Arial",int(15 * self.Back.font)), width=7)
            self.P_guardar= tb.Button(self.app, text="Guardar y emitir", bootstyle="warning-outline",command= lambda:self.save(status=1))
            self.P_guardarSin= tb.Button(self.app, text="Guadar sin emitir", bootstyle="warning-outline",command=self.save)
            self.P_borrar= tb.Button(self.app, text="Borrar", bootstyle="warning-outline")
            self.P_menu= tb.Button(self.app, text="Menu", bootstyle="warning-outline", command= self.menu)
            self.P_borrarOf= tb.Button(self.app, text="Borrar Oferta", bootstyle="warning-link", command=self.borrarOf)
            self.P_buscar= tb.Button(self.app, text="Buscar", bootstyle="warning-outline",command=self.SearchByName)
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
                        "cantidad1",'precioC1', 'cantidad2', 'precioC2','cantidad3', 'precioC3',]      
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
        self.app.bind("<F2>", self.save)
        self.app.bind("<F3>", lambda:self.save(status=1))
        self.P_id_value.focus_set()
    def SearchByName(self,event=0):
            def select(event=0):
                selected_item = self.tree.selection()
                if selected_item:
                    item = selected_item[0]
                    # Obtener los valores de la fila
                    valores = self.tree.item(item, "values")
                    # Obtener el valor de la segunda columna (índice 1, porque comienza en 0)
                    valor_columna = valores[3]
                    escape()
        
                    # if status==0:
                    self.buscar(Re=valor_columna)
                    # elif status==1:
                    #      self.etiFrame(x=valor_columna)
            # if status==0:
            self.frame = tb.Frame(self.app)
            self.frame.place(rely=0,relheight=1,relwidth=1,relx=0)
            # elif status==1:
            #      self.frame = tb.Toplevel(self.app)
            #      self.frame.state("zoomed")
                 
            def escape(event=0,):
                # if state==0:
                self.app.bind("<Return>", self.buscar)
                self.app.bind("<Escape>",self.menu)
                # elif state==1:
                #     pass
                self.frame.destroy()
                
            self.app.bind("<Escape>",escape)
            tb.Label(self.frame, text="Búsqueda General (marca, descripción, sabor):").pack(pady=5)
            self.entry_busqueda = tb.Entry(self.frame, width=50)
            self.entry_busqueda.pack(pady=5)
            # self.entry_busqueda.bind("<Return>", self.realizar_busqueda)
            self.entry_busqueda.focus_set()

            tb.Label(self.frame, text="Cantidad exacta (Sin unidad):").pack(pady=5)
            self.entry_cantidad = tb.Entry(self.frame, width=20)
            self.entry_cantidad.pack(pady=5)
            # self.app.bind("<Return>", self.realizar_busqueda)
            
            self.btn_buscar = tb.Button(
                self.frame, text="Buscar", command=self.realizar_busqueda, 
            )
            self.btn_buscar.pack(pady=10)

            self.tree = tb.Treeview(
                self.frame, 
                columns=( "Descripcion", "Cantidad","Precio","PLU",), 
                show="headings",
                height=15
            )
 
            self.tree.column("Descripcion", width=600)
            self.tree.column("Cantidad", width=40)
            self.tree.column("Precio", width=40)
            self.tree.column("PLU", width=40,)
            self.tree.heading("Descripcion", text="Descripcion")
            self.tree.heading("Cantidad", text="Cantidad ")
            self.tree.heading("Precio", text="Precio ")
            self.tree.heading("PLU", text="PLU",)
            self.tree.pack(fill="both", expand=True)
            
            # Scrollbar
            scrollbar = tb.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
            self.tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
            self.tree.bind("<<TreeviewSelect>>", select)
        
    def realizar_busqueda(self, event=None):
            terminos_general = self.entry_busqueda.get().strip()
            cantidad = self.entry_cantidad.get().strip()
            
            # Limpiar resultados
            self.tree.delete(*self.tree.get_children())
            
            resultados = self.Back.buscar_productos(terminos_general, cantidad)
            if not resultados:
                messagebox.showinfo("Información", "No se encontraron coincidencias")
                return
            
            for producto in resultados:
                net=''  
                for x in (4,5,6):
                     if producto[x] is not None: net+=f"{producto[x]} "
                cant= ''
                
                for y in (7,8):
                    if producto[y] is not None and producto[y]!= "Unidad:":
                         
                         if y==7:
                            cant+=f"{int(producto[y]) if producto[y] == int(producto[y]) else producto[y]}"   
                         else:
                            cant+=f"{producto[y]}"
                print('ds')
                self.tree.insert("", 'end', values=(
                    net,
                    cant,
                    f"$ {format(producto[3],',.2f')}",
                    producto[1]
                ))

    def borrarOf(self):
        Of= ["cantidad1",'precioC1', 'cantidad2', 'precioC2','cantidad3', 'precioC3']
        for x in Of:
            command= getattr(self, f'P_{x}_value')
            command.delete(0, tb.END)

    def save(self,status=0):
        command= []
        precio= self.P_precio_value.get()
        pprecio=precio[2:].replace(",","")
        if pprecio is None or pprecio== ''or pprecio== 0:
            messagebox.showinfo("Información", "El precio no puede ser nulo")
        else:
            dic={'Precio':f'{pprecio}'}

            for x in range(len(self.orden)):
                com=getattr(self, f'P_{self.orden[x]}_value')
                command.append(com.get())
                if not (command[x]== '' or x==2 or x==14 or x==16 or x==18):
                    dic.update({f'{self.colsql[x]}':f'{command[x]}'})
                elif (not command[x]== '') and (x==14 or x==16 or x==18):
                    dic.update({f'{self.colsql[x]}':f'{command[x][2:].replace(",","")}'})  
                elif command[x]=='':
                    dic.update({f'{self.colsql[x]}':'NULL'})
            dic.update({'Fecha_de_modificacion': f'{date.today()}'})
            self.Back.guardar(dic, self.P_id_value.get(),status=status)

            self.clean()

    def buscar(self,event=0,Re=0):

        value= Re if Re else self.P_id_value.get()
        self.clean()
        self.app.bind("<Escape>", self.clean)
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
                    command.insert(0, f"$ {format(result[x],',.2f')}")
                else:
                    continue
            self.P_fecha.config(text=f'Fecha de Modificacion: {result[20]}')
            self.P_precio_value.focus()
        else:
            self.buscar(Re=value) 
                  
    def clean(self, event=0):
        self.P_fecha.config(text="Fecha de Modificacion: ")
        self.P_id_value.config(state= 'normal')
        for widget in self.app.winfo_children():
            if isinstance(widget, tb.Entry):
                widget.delete(0, tb.END)
        self.P_control_value.set('Unidad:') 
        self.app.bind("<Return>", self.buscar)
        self.app.bind("<Escape>", self.menu) 
        self.disable_entries(exclude=[self.P_id_value])
        self.create_widget_precio(1)
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
                formatted = f"$ {format(numeric_value,',.2f')}"
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
            text = "etiquetas", style= "darkly", command=self.etiFrame)
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
    def etiFrame(self,event=0,x=0):

            
        def desmarcar_columna(columna,x=1):
        # Iterar sobre todas las filas (listas de variables BooleanVar)
                for vars_list in check_dict.values():
                    # Verificar si la columna existe en esta fila
                    if columna < len(vars_list):
                        # Cambiar el valor de la variable a False
                        if x==1:
                            vars_list[columna].set(True) 
                        else:
                            vars_list[columna].set(False) 
        def cargar(status=1):
            self.datos_productos=[]
            for res in self.Back.etiquetasSearch(instruc=status):
                net=""
                for w in (4,5,6,7,8):
                    if w==7:
                        net+=f"{int(res[w]) if res[w] is not None and str(res[w]).isdigit() else res[w]}"
                    elif w==8 and res[8] =="Unidad:":
                        pass
                    elif res[w]: 
                        net+=f"{res[w]} "
                # Plu, precio, descr, pasillo, precio1, precio2, precio3, fecha de mod, 0, cant1,cant2,cant3, cant u, uni
                values=(res[1], res[3], f"{net}", res[9], res[14], res[16], res[18],res[19], "",res[13],res[15],res[17],res[7],res[8]) 
                self.datos_productos.append(values)
            
            self.datos_productos.sort(key= lambda x: (x[3] is None,x[3]))
            cargar_filas_desde_tuplas(self.datos_productos)
            if status==1:
                Rap.config(state="Normal")
                Of1.config(state="disabled")
                Of2.config(state="disabled")
                Of4.config(state="disabled")
                changeControl(1)
                desmarcar_columna(0)
            else:
                Rap.config(state="disabled")
                Of1.config(state="normal")
                Of2.config(state="normal")
                Of4.config(state="normal")
                changeControl(2)
                desmarcar_columna(1)
        def limpiarPantalla():
                for row_frame in check_frame.winfo_children():
                                            for i, chk in enumerate(row_frame.winfo_children()):
                                                if i == 0:
                                                    
                                                    chk.configure(state="disabled")
                                                else:
                                                    chk.configure(state="normal")
                tree.delete(*tree.get_children())  # Eliminar todas las filas del Treeview
                for widget in check_frame.winfo_children():  # Destruir todos los Checkbuttons anteriores
                        widget.destroy()
                check_dict.clear()  
                Rap.config(state="normal")
                Of1.config(state="normal")
                Of2.config(state="normal")
                Of4.config(state="normal")
                self.datos_productos.clear()
        
        def entrada(event=0,Re=0):
        
                print(Re)
                if Re:
                    val= Re 
                else:
                     val=Etientrada.get()
                     Etientrada.delete(0,tk.END)
                doc=self.Back.search(val,status=1)
                
                if doc is not None:
                    for res in doc:
                                    net=""
                                    for w in (4,5,6,7,8):
                                        if w==7:
                                            net+=f"{int(res[w]) if res[w] is not None and str(res[w]).isdigit() else res[w]}"
                                        elif w==8 and res[8] =="Unidad:":
                                            pass
                                        elif res[w]: 
                                            net+=f"{res[w]} "
                                    # Plu, precio, descr, pasillo, precio1, precio2, precio3, fecha de mod, 0, cant1,cant2,cant3, cant u, uni
                                    values=(res[1], res[3], f"{net}", res[10], res[15], res[17], res[19],res[20], "",res[14],res[16],res[18],res[7],res[8]) 
                                    self.datos_productos.append(values)
                                    
                    self.datos_productos.sort(key= lambda x: (x[3] is None,x[3]))
                    cargar_filas_desde_tuplas(self.datos_productos)
                    changeControl(status=self.estado)
                    if self.estado==1:
                        desmarcar_columna(0)
                    else:
                        desmarcar_columna(1)
                else:
                    messagebox.showerror("error","Articulo NO registrado")
                    return

        def changeControl(status):
        
                if status==1:
                    Rap.config(bootstyle="Success")
                    Of1.config(bootstyle="dark")
                    Of2.config(bootstyle="dark")
                    Of4.config(bootstyle="dark")
                    self.estado=1
                    desmarcar_columna(1,0)
                    desmarcar_columna(2,0)
                    desmarcar_columna(3,0)
                elif status==2:
                    Rap.config(bootstyle="dark")
                    Of1.config(bootstyle="Dark")
                    Of2.config(bootstyle="Dark")
                    Of4.config(bootstyle="Success")
                    desmarcar_columna(0,0)
                    self.estado=2
                elif status==3:
                    Rap.config(bootstyle="Dark")
                    Of1.config(bootstyle="Dark")
                    Of2.config(bootstyle="Success")
                    Of4.config(bootstyle="Dark")
                    desmarcar_columna(0,0)
                    self.estado=3
                elif status==4:
                    Rap.config(bootstyle="dark")
                    Of1.config(bootstyle="Success")
                    Of2.config(bootstyle="Dark")
                    Of4.config(bootstyle="Dark")
                    desmarcar_columna(0,0)
                    self.estado=4
                if status==3 or status==2 or status==4:
                    for row_frame in check_frame.winfo_children():
                                for i, chk in enumerate(row_frame.winfo_children()):
                                    if i == 0:
                                        
                                        chk.configure(state="disabled")
                                        
                                    else:
                                        chk.configure(state="normal")
                elif status==1:
                    for row_frame in check_frame.winfo_children():
                                for i, chk in enumerate(row_frame.winfo_children()):
                                    if not i == 0:  
                                        chk.configure(state="disabled")
                                    else:
                                        chk.configure(state="normal")
        def actualizar_treeview():
                for item_id, vars_list in check_dict.items():
                    if any(var.get() for var in vars_list):  # Si al menos un Checkbutton está activado
                        tree.item(item_id, tags=("seleccionado",))
                    else:
                        tree.item(item_id, tags=())
        def cargar_filas_desde_tuplas(datos):
                # Limpiar datos previos
                tree.delete(*tree.get_children())  # Eliminar todas las filas del Treeview
                for widget in check_frame.winfo_children():  # Destruir todos los Checkbuttons anteriores
                    widget.destroy()
                check_dict.clear()  # Reiniciar el diccionario de Checkbuttons

                # Cargar nuevos datos
                for producto in datos:
                    precio = f"$ {producto[1]}" if producto[1] is not None else "$"
                    precio1 = f"$ {producto[4]}" if producto[4] is not None else "$"
                    precio2 = f"$ {producto[5]}" if producto[5] is not None else "$"
                    precio3 = f"$ {producto[6]}" if producto[6] is not None else "$"
                    descripcion = producto[2]
                    opciones = producto[8:12]

                    # Insertar fila en Treeview
                    item_id = tree.insert("", "end", values=(descripcion, precio, precio1, precio2, precio3))

                    # Crear Frame para checkboxes
                    row_frame = tb.Frame(check_frame)
                    row_frame.grid(row=len(check_dict), column=0, sticky="w")

                    # Variables y checkboxes
                    row_vars = []
                    for i, texto_opcion in enumerate(opciones):
                        var = tk.BooleanVar(value=False)
                        row_vars.append(var)
                        chk = tb.Checkbutton(
                            row_frame, 
                            text=texto_opcion,
                            variable=var,
                            command=actualizar_treeview
                        )
                        chk.pack(side="left", padx=5)
                    
                    check_dict[item_id] = row_vars

                # Actualizar scroll y altura del treeview
                tree["height"] = len(datos)
                canvas.update_idletasks()
                canvas.configure(scrollregion=canvas.bbox("all"))
                actualizar_treeview()
            # Cargar los datos al iniciar
        def delete(x):
                y=messagebox.askyesno("Borrar", "Desea limpiar etiquetas")
                if y:
                    self.Back.etiquetasSearch(x)
                    limpiarPantalla()
                else:
                    pass
        def obtener_productos_seleccionados():
            try:
                if not tree.get_children():
                    messagebox.showerror("error",'No hay productos para imprimir')
                    return
                
                productos = []
                selecciones_validas = False
                
                for item_id, vars_list in check_dict.items():
                    estados = [var.get() for var in vars_list]
                    if any(estados):  # Si al menos un checkbox está seleccionado
                        selecciones_validas = True
                        nombre_producto = tree.item(item_id, "values")[0]
                        
                        for producto in self.datos_productos:
                            if producto[2] == nombre_producto:
                                try:
                                    # Convertir a float si es posible, si no, usar 1
                                    try:
                                        Cunidad = float(producto[12]) if producto[12] is not None and str(producto[12]).replace('.','',1).isdigit() else 1
                                    except Exception:
                                        Cunidad = 1
                                    unidad = producto[13] 
                                    
                                    if producto[13] == "Unidad:":
                                        unidad = 'unidad'
                                    elif producto[13] == "gr":
                                        unidad = 'Kg'
                                        Cunidad = Cunidad/1000
                                    elif producto[13] == "ml" or producto[13] == "m³":
                                        unidad = 'Lt'
                                        Cunidad = Cunidad/1000
                                    elif producto[13] == "mg":
                                        unidad = "gr"
                                        Cunidad = Cunidad/1000
                                except (ValueError, TypeError):
                                    # Si hay error en la conversión, usar valores por defecto
                                    unidad = 'unidad'
                                    Cunidad = 1
                                    
                                if estados[0]:
                                    value = {
                                        "nombre": f"{producto[2]}", 
                                        "precio": float(producto[1]) if producto[1] else 0, 
                                        "codigo": f"{producto[0]}",
                                        "cunidad": Cunidad,
                                        "unidad": f"{unidad}",
                                        "fecha": f"{producto[7]}"
                                    }
                                    productos.append(value)
                                if estados[1]:
                                    try:
                                        precio_anterior = float(producto[1])*float(producto[9]) if producto[1] and producto[9] else 0
                                    except Exception:
                                        precio_anterior = 0
                                    value = {
                                        "descripcion": f"{producto[2]}", 
                                        "precio_anterior": precio_anterior,
                                        "precio": float(producto[4]) if producto[4] else 0, 
                                        "codigo_barras": f"{producto[0]}",
                                        "CantUni": Cunidad,
                                        "unidad": f"{unidad}",
                                        "cant": float(producto[9]) if producto[9] else 0
                                    }
                                    productos.append(value)
                                if estados[2]:
                                    try:
                                        precio_anterior = float(producto[1])*float(producto[10]) if producto[1] and producto[10] else 0
                                    except Exception:
                                        precio_anterior = 0
                                    value = {
                                        "descripcion": f"{producto[2]}", 
                                        "precio_anterior": precio_anterior,
                                        "precio": float(producto[5]) if producto[5] else 0, 
                                        "codigo_barras": f"{producto[0]}",
                                        "CantUni": Cunidad,
                                        "unidad": f"{unidad}",
                                        "cant": float(producto[10]) if producto[10] else 0
                                    }
                                    productos.append(value)
                                if estados[3]:
                                    try:
                                        precio_anterior = float(producto[1])*float(producto[11]) if producto[1] and producto[11] else 0
                                    except Exception:
                                        precio_anterior = 0
                                    value = {
                                        "descripcion": f"{producto[2]}", 
                                        "precio_anterior": precio_anterior,
                                        "precio": float(producto[6]) if producto[6] else 0, 
                                        "codigo_barras": f"{producto[0]}",
                                        "CantUni": Cunidad,
                                        "unidad": f"{unidad}",
                                        "cant": float(producto[11]) if producto[11] else 0
                                    }
                                    productos.append(value)
                                break
                
                if not selecciones_validas:
                    messagebox.showerror("Error", "No hay productos seleccionados")
                    return
                    
                if not productos:
                    messagebox.showerror("Error", "No se encontraron datos válidos para los productos seleccionados")
                    return
                    
                if self.estado == 1:                        
                    self.eti(productos)
                elif self.estado == 2:
                    self.generar_oferta(productos=productos, disposicion="4x1")
                elif self.estado == 3:
                    self.generar_oferta(productos=productos, disposicion="2x1")
                elif self.estado == 4:
                    self.generar_oferta(productos=productos, disposicion="1x1")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Error al procesar las selecciones: {str(e)}")
        
        self.datos_productos=[]
        self.etiF=tk.Frame(self.app,)
        control=tk.StringVar(value="EtiR")
        self.estado=1
        self.etiF.place(relheight=1,relwidth=1,   relx=0,rely=0)
        Rap=tb.Button(self.etiF, style="Success",text="Etiqueta Rapida", command=lambda: changeControl(1))
        Of4=tb.Button(self.etiF, style="dark",text="Oferta 4x1", command=lambda: changeControl(2))
        Of2=tb.Button(self.etiF, style="dark",text="Oferta 2x1", command=lambda: changeControl(3))
        Of1=tb.Button(self.etiF, style="dark",text="Oferta 1x1", command=lambda: changeControl(4))
        Etientrada= tb.Entry(self.etiF, style="dark",width=10)
        Etientrada.place(relheight=0.05,relwidth=0.4,relx=0.3,rely=0.9)
        Rap.place(relx=0., rely=0.2,relheight=0.05,relwidth=0.09)
        Of4.place(relx=0., rely=0.27,relheight=0.05,relwidth=0.09)
        Of2.place(relx=0., rely=0.34,relheight=0.05,relwidth=0.09)
        Of1.place(relx=0, rely=0.41,relheight=0.05,relwidth=0.09)
        # tb.Button(self.etiF, style="dark",text="Buscar",command=lambda :self.SearchByName(status=1)).place(relheight=0.05,relwidth=0.09,relx=0.8, rely=0.9)
        main_frame = tk.Frame(self.etiF)
        main_frame.place(relx=0.1,relheight=0.65,relwidth=0.85,rely=0.1)

            # Canvas para permitir desplazamiento
        canvas = tk.Canvas(main_frame)
        scrollbar = tb.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
            # Frame interno dentro del canvas

        scrollable_frame = tb.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

            # Frame para organizar Checkbuttons y Treeview
        content_frame = tb.Frame(scrollable_frame)
        content_frame.pack(fill="both", expand=True)

            # Frame para Checkbuttons (lado izquierdo)
        check_frame = tb.Frame(content_frame)
        check_frame.grid(row=0, column=0, sticky="nw", padx=5)

            # Treeview (lado derecho)
        tree =tb.Treeview(content_frame, columns=("data","Precion","Precio1","Precio2","Precio3"), show="tree", height=0)

        tree.column("data", width=400, anchor="w")
        tree.column("Precion", width=80, anchor="center")
        tree.column("Precio1", width=80, anchor="center")
        tree.column("Precio2", width=80, anchor="center")
        tree.column("Precio3", width=80, anchor="center")
        tree.grid(row=0, column=1, columnspan=5, sticky="nwe", padx=1)
        tree.configure(selectmode="none")
            # Diccionario para almacenar Checkbuttons vinculados con filas del Treeview
        check_dict = {}

            # Función para actualizar selección en el Treeview
            
            # Configurar color de filas seleccionadas
        tree.tag_configure("seleccionado", background="green")

        # Función modificada para cargar desde tuplas
            
            # Empaquetar el canvas y el scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        tb.Button(self.etiF, style="success-outline",text= "Cargar Etiquetas", command= lambda: cargar(status=1)).place(relheight=0.05, relwidth=0.09, relx=0.2, rely=0.9)
        tb.Button(self.etiF, style= "success-outline",text= "Cargar Ofertas", command= lambda: cargar(status=2)).place(relheight=0.05, relwidth=0.09, relx=0.1, rely=0.9)
        tb.Button(self.etiF, style="dark",text= "Borrar Etiquetas", command= lambda: delete(3)).place(relheight=0.05, relwidth=0.09, relx=0.9, rely=0.84)
        tb.Button(self.etiF, style= "dark",text= "Borrar Ofertas", command= lambda: delete(4)).place(relheight=0.05, relwidth=0.09, relx=0.9, rely=0.9)
        tb.Button(self.etiF, style= "success-outline",text= "Limpiar Pantalla", command= lambda: limpiarPantalla()).place(relheight=0.05, relwidth=0.09, relx=0, rely=0.9)
        tb.Button(self.etiF, style= "dark",text= "Imprimir", command= lambda: obtener_productos_seleccionados()).place(relheight=0.05, relwidth=0.09, relx=0.8, rely=0.84)
            
        self.app.bind("<Escape>",lambda event:self.etiF.destroy())
        self.app.bind("<Return>", lambda event: entrada(event))
    def eti(self,productos):
        
        PAGE_WIDTH, PAGE_HEIGHT = A4
        LABEL_WIDTH = 5.8 * cm
        LABEL_HEIGHT = 2.8 * cm
        MARGIN_LEFT = (PAGE_WIDTH - (3 * LABEL_WIDTH)) / 2
        ROWS_PER_PAGE = 10

        # Estilo del texto
        NOMBRE_FUENTE = "Helvetica"
        TAMANO_PRECIO = 20  # Reducido para mejor ajuste
        TAMANO_TEXTO = 10   # Reducido para mejor ajuste
        TAMANO_CODIGO = 6
        ESPACIADO = 0.15 * cm  # Aumentado para mejor separación

        # Zonas verticales de la etiqueta (en cm desde el borde superior)
        ZONA_NOMBRE = 0.5 * cm    # Aumentado
        ZONA_PRECIO = 1.6 * cm    # Ajustado
        ZONA_CODIGO = 2.2 * cm    # Ajustado

        def generar_codigo_barras(codigo):
            try:
                codigo = str(codigo).strip()
                if not codigo:
                    raise ValueError("El código está vacío")
                
                # Configurar el código de barras con opciones más robustas
                barcode_options = {
                    'barHeight': 0.4*cm,
                    'humanReadable': False,
                    'fontName': 'Helvetica'  # Usar Helvetica en lugar de Times-Roman
                }
                
                if len(codigo) == 13:
                    barcode = createBarcodeDrawing('EAN13', value=codigo[:-1], **barcode_options)
                elif len(codigo) == 12:
                    barcode = createBarcodeDrawing('UPCA', value=codigo, **barcode_options)
                elif len(codigo) == 8:
                    barcode = createBarcodeDrawing('EAN8', value=codigo[:-1], **barcode_options)
                else:
                    barcode = createBarcodeDrawing('Code128', value=codigo, **barcode_options)
                
                nombre_archivo = f"temp_{codigo}.png"
                renderPM.drawToFile(barcode, nombre_archivo, fmt='PNG')
                return nombre_archivo
                
            except Exception as e:
                try:
                    # Intento alternativo con Code128 y opciones mínimas
                    barcode = createBarcodeDrawing('Code128', 
                                                 value=str(codigo), 
                                                 barHeight=0.4*cm,
                                                 humanReadable=False)
                    nombre_archivo = f"temp_{codigo}.png"
                    renderPM.drawToFile(barcode, nombre_archivo, fmt='PNG')
                    return nombre_archivo
                except Exception as inner_e:
                    print(f"Error al generar código de barras: {str(inner_e)}")
                    # Crear un código de barras simple como fallback
                    try:
                        barcode = createBarcodeDrawing('Code128', 
                                                     value="000000000000", 
                                                     barHeight=0.4*cm,
                                                     humanReadable=False)
                        nombre_archivo = "temp_fallback.png"
                        renderPM.drawToFile(barcode, nombre_archivo, fmt='PNG')
                        return nombre_archivo
                    except:
                        raise ValueError(f"No se pudo generar ningún código de barras: {str(e)}")

        def crear_etiquetas():
            c = canvas.Canvas("etiquetas_precios.pdf", pagesize=A4)

            for i, producto in enumerate(productos):
                # Saltar a una nueva página cuando se llenan las filas por hoja
                if i % (ROWS_PER_PAGE * 3) == 0 and i != 0:
                    c.showPage()

                columna = i % 3
                fila = (i // 3) % ROWS_PER_PAGE

                # Coordenadas base de cada etiqueta
                x = MARGIN_LEFT + columna * LABEL_WIDTH
                y = PAGE_HEIGHT - LABEL_HEIGHT - fila * LABEL_HEIGHT - 1 * cm

                # Dibuja el borde de la etiqueta
                c.rect(x, y, LABEL_WIDTH, LABEL_HEIGHT)

                # Nombre del producto
                c.setFont(NOMBRE_FUENTE, TAMANO_TEXTO)
                nombre = simpleSplit(producto['nombre'], NOMBRE_FUENTE, TAMANO_TEXTO, LABEL_WIDTH - 2 * ESPACIADO)
                text_y = y + LABEL_HEIGHT - ZONA_NOMBRE
                for line in nombre:
                    c.drawString(x + ESPACIADO, text_y, line)
                    text_y -= TAMANO_TEXTO * 1.2

                # Fecha
                c.setFont(NOMBRE_FUENTE, 5)
                c.drawCentredString(
                    x + LABEL_WIDTH - 0.8 * cm,
                    y + ESPACIADO,
                    f"{producto['fecha']}"
                )

                # Precio por litro
                precio_xlt = producto['cunidad'] * producto['precio']
                c.drawString(
                    x + ESPACIADO,
                    y  +LABEL_HEIGHT- ZONA_PRECIO - 0.65 * cm,
                    f"$ {format(precio_xlt, ',.2f')} xLt"
                )

                # Precio principal
                c.setFont(NOMBRE_FUENTE + "-Bold", TAMANO_PRECIO)
                c.drawCentredString(
                    x + LABEL_WIDTH / 2,
                    y + LABEL_HEIGHT - ZONA_PRECIO,
                    f"$ {format(producto['precio'], ',.2f')}"
                )

                # Precio sin impuestos
                precio_sin_iva = producto["precio"] * 0.79
                c.setFont(NOMBRE_FUENTE, 5)
                c.drawString(
                    x + ESPACIADO,
                    y + LABEL_HEIGHT - ZONA_PRECIO - 0.85 * cm,
                    f"PRECIO SIN IMPUESTOS NACIONALES: $ {format(precio_sin_iva, ',.2f')}"
                )

                # Código de barras (comentado por ahora)
                # codigo_img = generar_codigo_barras(producto["codigo"])
                # c.drawImage(codigo_img, 
                #     x + ESPACIADO + 0.1 * cm,
                #     y + ESPACIADO + 0.3 * cm,
                #     width=2.8 * cm,
                #     height=0.4 * cm
                # )

                # Texto del código
                c.setFont(NOMBRE_FUENTE, TAMANO_CODIGO)
                c.drawString(
                    x + ESPACIADO,
                    y + ESPACIADO,
                    f"PLU: {producto['codigo']}"
                )
                
                # os.remove(codigo_img)
            
            c.save()
        crear_etiquetas()
        self.abrir_pdf("etiquetas_precios.pdf")
    def abrir_pdf(self,ruta_archivo):
    # Para Windows
            if os.name == 'nt':
                os.startfile(ruta_archivo)
            # Para Linux o macOS
            else:
                opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
                subprocess.run([opener, ruta_archivo])

        # Ejemplo de uso
        
    def generar_oferta(self,productos, disposicion, nombre_archivo="ofertas.pdf"):
        def formatear_float(num):
            return str(num).rstrip('0').rstrip('.') if '.' in str(num) else str(num)

        def generar_codigo_barras(codigo):
            try:
                codigo = str(codigo).strip()
                if not codigo:
                    raise ValueError("El código está vacío")
                
                if len(codigo) == 13:
                    barcode = createBarcodeDrawing('EAN13', value=codigo[:-1], barHeight=0.4*cm, humanReadable=False)
                elif len(codigo) == 12:
                    barcode = createBarcodeDrawing('UPCA', value=codigo, barHeight=0.4*cm, humanReadable=False)
                elif len(codigo) == 8:
                    barcode = createBarcodeDrawing('EAN8', value=codigo[:-1], barHeight=0.4*cm, humanReadable=False)
                else:
                    barcode = createBarcodeDrawing('Code128', value=codigo, barHeight=0.4*cm, humanReadable=False)
                
                nombre_archivo = f"temp_{codigo}.png"
                renderPM.drawToFile(barcode, nombre_archivo, fmt='PNG')
                return nombre_archivo
                
            except Exception as e:
                try:
                    barcode = createBarcodeDrawing('Code128', value=str(codigo), barHeight=0.4*cm, humanReadable=False)
                    nombre_archivo = f"temp_{codigo}.png"
                    renderPM.drawToFile(barcode, nombre_archivo, fmt='PNG')
                    return nombre_archivo
                except:
                    raise ValueError(f"Error al generar código de barras: {str(e)}")

        # Configurar disposición y orientación
        if disposicion == "1x1":
            ancho, alto = landscape(A4)
            state = 1.5
            margen = 1.2 * cm
        elif disposicion == "4x1":
            ancho, alto = landscape(A4)
            state = 1
            margen = 1.5 * cm
        else:
            state = 1.2
            ancho, alto = A4
            margen = 1.2 * cm

        tamanio_fuente = {
            '1x1': {'titulo': 36, 'precio': 44, 'normal': 14},
            '2x1': {'titulo': 28, 'precio': 36, 'normal': 12},
            '4x1': {'titulo': 20, 'precio': 28, 'normal': 8}
        }[disposicion]

        estilos = {
            'titulo': ParagraphStyle(
                name='Titulo',
                fontSize=tamanio_fuente["titulo"],
                textColor=black,
                leading=26,
                alignment=TA_CENTER
            ),
            'precio': ParagraphStyle(
                name='Precio',
                fontSize=tamanio_fuente["precio"],
                textColor=black,
                leading=20,
                alignment=TA_CENTER
            ),
            'normal': ParagraphStyle(
                name='Normal',
                fontSize=tamanio_fuente['normal'],
                textColor=black,
                leading=18,
                alignment=TA_CENTER
            ),
            'other': ParagraphStyle(
                name='other',
                fontSize=tamanio_fuente['normal'],
                textColor=black,
                leading=9,
            ),
            'other1': ParagraphStyle(
                name='other1',
                fontSize=tamanio_fuente['normal'],
                textColor=black,
                leading=11,
                alignment=TA_RIGHT
            )
        }

        if disposicion == "1x1":
            columnas, filas = 1, 1
        elif disposicion == "2x1":
            columnas, filas = 1, 2
        elif disposicion == "4x1":
            columnas, filas = 2, 2
        else:
            raise ValueError("Disposición no válida: usar 1x1, 2x1 o 4x1")

        ancho_etiqueta = (ancho - 2 * margen) / columnas
        alto_etiqueta = (alto - 2 * margen) / filas

        c = canvas.Canvas(nombre_archivo, pagesize=(ancho, alto))

        for i, producto in enumerate(productos):
            col = i % columnas
            fila = (i // columnas) % filas

            if i % (columnas * filas) == 0 and i != 0:
                c.showPage()

            x = margen + col * ancho_etiqueta
            y = alto - margen - (fila + 1) * alto_etiqueta

            c.rect(x, y, ancho_etiqueta, alto_etiqueta)

            # Oferta
            oferta = Paragraph(f"<b><u>OFERTA</u></b>", estilos['precio'])
            oferta.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
            x_pos = x + (ancho_etiqueta - oferta.width) / 2
            oferta.drawOn(c, x_pos, y + alto_etiqueta - (0.6 * cm*state) - oferta.height)

            # Descripción
            descripcion = Paragraph(producto['descripcion'], estilos['titulo'])
            descripcion.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
            x_pos = x + (ancho_etiqueta - descripcion.width) / 2
            descripcion.drawOn(c, x_pos, y + alto_etiqueta - (2.0 * cm*state) - descripcion.height)

            # Precio actual
            if producto["cant"]==1:
                precio_actual = Paragraph(f"Ahora: <b> ${format((producto['precio']*producto['cant']),',.2f')}</b>", estilos['precio'])
            else:
                precio_actual = Paragraph(f"Ahora: <b>{int(producto['cant'])}x ${format((producto['precio']*producto['cant']),',.2f')}</b>", estilos['precio'])
            precio_actual.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
            x_pos = x + (ancho_etiqueta - precio_actual.width) / 2
            precio_actual.drawOn(c, x_pos, y + alto_etiqueta - (4.7 * cm*state) - precio_actual.height)

            # Precio sin impuestos
            precio_sin_impuestos = producto['precio'] * 0.79
            precio_sin_impuestos_text = Paragraph(f"PRECIO SIN IMPUESTOS NACIONALES: $ {format(precio_sin_impuestos,',.2f')}", estilos['other'])
            precio_sin_impuestos_text.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
            x_pos = x + 0.5 * cm
            precio_sin_impuestos_text.drawOn(c, x_pos, y + 0.6 * cm)

            # Precio anterior
            precio_anterior = Paragraph(f"<b>Antes:</b> $ {format(producto['precio_anterior'],',.2f')}", estilos['other'])
            precio_anterior.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
            x_pos = x + 5*cm+(ancho_etiqueta - precio_anterior.width) / 2
            precio_anterior.drawOn(c, x_pos, y + alto_etiqueta - (6.7 * cm*state) - precio_anterior.height)
            
            # Precio por unidad
            uni = producto['unidad'] if not producto['unidad']== 'Unidad:' else 'unidad'
            if producto["cant"]==1:
                precio_litro = Paragraph(f"Precio por {uni}: $ {format((producto['CantUni']*producto['precio']), ',.2f')}", estilos['other'])
            else:
                precio_litro = Paragraph(f"Precio por Unidad: $ {format(producto['precio'], ',.2f')}", estilos['other'])
            precio_litro.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
            x_pos = x + 0.5 * cm
            precio_litro.drawOn(c, x_pos, y + 1.2 * cm)

            # Código de artículo
            codigo = Paragraph(f"Art: {producto['codigo_barras']}", estilos['other1'])
            codigo.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
            x_pos = x + ancho_etiqueta - codigo.width - 0.5 * cm
            codigo.drawOn(c, x_pos, y + 1.2 * cm)

            # Código de barras
            # codigo_img = generar_codigo_barras(producto['codigo_barras'])
            # c.drawImage(codigo_img, 
            #         x_pos,
            #         y + 1.7 * cm,
            #         width=2.8 * cm,
            #         height=0.4 * cm
            # )
            # os.remove(codigo_img)

        c.save()
        self.abrir_pdf("ofertas.pdf")


    # Ejemplo de uso
    productos = [
        {
            'titulo': '',
            'descripcion': 'Extra virgen 1L botella vidrio',
            'precio': '6.99',
            'precio_anterior': '8.99',
            'precio_litro': '6.99',
            'codigo_barras': '123456789012',
            'unidad':'Unidad:',
            'CantUni':'350',
            "cant":1
        },
        {
            'titulo': '',
            'descripcion': 'Leche Entera Pack Pack de 6 boewewtellas de 1L',
            'precio': '11,999.99',
            'precio_anterior': '5.99',
            'precio_litro': '0.75',
            'codigo_barras': '987654321098'
        },
        {
            'titulo': 'Leche Entera',
            'descripcion': 'Pack de 6 botellas de 1L',
            'precio': '4499.99',
            'precio_anterior': '5.99',
            'precio_litro': '0.75',
            'codigo_barras': '987654321098'
        },
        {
            'titulo': 'Leche Entera',
            'descripcion': 'Pack de 6 botellas de 1L',
            'precio': '3999.99',
            'precio_anterior': '299925.99',
            'precio_litro': '0.75',
            'codigo_barras': '987654321098'
        },
        # Agrega más productos según necesites
    ]

    # disposicion = input("Elige disposición (1x1, 2x1, 4x1): ").strip().lower()

main()
        