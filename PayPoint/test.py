import itertools

def encontrar_combinacion(numeros, objetivo):
    # Ordenar los números de menor a mayor
    numeros_ordenados = sorted(numeros)
    mejor_suma = float('inf')
    mejor_combinacion = None
    
    # Buscar combinaciones de menor a mayor longitud
    for longitud in range(1, len(numeros_ordenados) + 1):
        for combinacion in itertools.combinations(numeros_ordenados, longitud):
            suma_actual = sum(combinacion)
            if suma_actual >= objetivo:
                # Si hay coincidencia exacta, retornar inmediatamente
                if suma_actual == objetivo:
                    return combinacion
                # Si no, buscar la menor suma que supere el objetivo
                if suma_actual < mejor_suma:
                    mejor_suma = suma_actual
                    mejor_combinacion = combinacion
    return mejor_combinacion

# Ejemplo de uso
numeros = [8,6,10, 8,28,5, 10]
objetivo = 40
resultado = encontrar_combinacion(numeros, objetivo)

if resultado:
    print(type(resultado))
    print(resultado)
    print(f"Combinación óptima: {' + '.join(map(str, resultado))} = {sum(resultado)}")
else:
    print("No hay combinación que alcance el objetivo.")