# Definir las variables
a = 15
b = 30
c = 10

# Crear una lista con índices y valores
variables = [('a', a), ('b', b), ('c', c)]

# Ordenar de mayor a menor según los valores
ordenadas = sorted(variables, key=lambda x: x[1], reverse=True)

# Obtener los nombres en orden
nombres_orden = [nombre for nombre, _ in ordenadas]

print(nombres_orden[0])