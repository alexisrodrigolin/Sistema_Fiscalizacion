   
def guardar( dic):
        net=""
        for clave, valor in dic.items():
            net+= f"{clave} + {valor}, "
        print(net)

guardar({"one":"w","oda":"ds"})