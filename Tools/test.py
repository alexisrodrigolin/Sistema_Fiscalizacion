class main():
    def __init__(self):
        self.orden= ['plu', 'plu2', 'precio','marca','descripcion', 'tipo', 'cantidad', 'control',
                     'departamento', 'pasillo', 'costo','iva', 'ganancia', 
                     "cantidad1",'precioC1', 'cantidad2', 'precioC2','cantidad3', 'precioC3']      
        self.colsql= ['PLU','PLU2', 'Precio','Marca','Descripcion', 'Tipo_Sabor','Cantidad', 'Unidad',
                     'Departamento', 'Pasillo', 'Costo','IVA', 'Ganancia', 
                     "Cant1",'Precio1', 'Cant2', 'Precio2','Cant3', 'Precio3']  

    def save(self):
        command= []
        dic={}
        for x in range(len(self.orden)):
            command.append= getattr(self, f'P_{self.orden[x]}_value')
            dic.update({f'{self.orden[x]}':f'{self.colsql[x]}'})
        print(command)
main().save()