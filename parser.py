from convertGrammar import grammar

primeros = {}
siguientes = {}

# Función para calcular el conjunto de primeros
def getFirsts (symbol):
    if primeros.__contains__(symbol):
        return primeros
    #print(symbol)
    primeros[no_terminal] = set()
    for produccion in grammar[symbol]:
            
        if produccion[0] not in grammar.keys():
            primeros[symbol].add(produccion[0])
        elif produccion[0] == 'e':
            primeros[symbol].add('e')
        else:
            for element in produccion:
                #print("elemento",element)
                if element == symbol and grammar[symbol].__contains__(['e']):
                    continue
                if element not in grammar.keys():
                    primeros[symbol].add(element)
                    break
                elif not primeros.__contains__(element):
                    #print(11)
                    getFirsts(grammar, element)
                    primeros[symbol] = primeros[symbol].union(primeros[element])
                    if 'e' not in primeros[element]:
                        break
                    primeros[symbol].remove('e')
                    #print(primeros[symbol])
                else:
                    #print(22)
                    primeros[symbol] = primeros[symbol].union(primeros[element])
                    if 'e' not in primeros[element]:
                        break
                    primeros[symbol].remove('e')
                
    #print(primeros)
    return primeros

def getFollow(symbol):
   

    return 0

for no_terminal in reversed(grammar.keys()):
    #print(no_terminal)
    getFirsts(no_terminal)
for no_terminal in grammar.keys():
    getFollow(no_terminal)

print(primeros)


""" # Función para calcular el conjunto de siguientes
def calcular_siguientes(grammar):
    siguientes = {}
    # Algoritmo para calcular los siguientes
    # Implementar aquí
    return siguientes

# Función para calcular el conjunto de predicciones
def calcular_predicciones(grammar, primeros, siguientes):
    predicciones = {}
    # Algoritmo para calcular las predicciones
    # Implementar aquí
    return predicciones

 """

""" primeros = setFirsts (grammar)
siguientes = calcular_siguientes(grammar)
predicciones = calcular_predicciones(grammar, primeros, siguientes)

# Imprimir los resultados
print("Conjunto de Primeros:")
for no_terminal, primero in primeros.items():
    print(no_terminal + ": ", primero)

print("\nConjunto de Siguientes:")
for no_terminal, siguiente in siguientes.items():
    print(no_terminal + ": ", siguiente)

print("\nConjunto de Predicciones:")
for no_terminal, prediccion in predicciones.items():
    print(no_terminal + ": ", prediccion) """
