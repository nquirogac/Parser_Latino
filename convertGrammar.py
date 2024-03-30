# grammar de txt a diccionario
def convertGrammar(file):
    with open(file, 'r') as file:
        grammar = {}
        for linea in file:
            partes = linea.strip().split(' -> ')
            no_terminal = partes[0].strip()
            sentencias = partes[1].strip().split('|')
            producciones = []   
            for i in range(len(sentencias)):
                sentencias[i] = sentencias[i].split()
                producciones.append(sentencias[i]) 
            grammar[no_terminal] = producciones
    with open('FinalGrammar.py', 'w') as output_file:
        output_file.write("grammar={\n")
        for non_terminal, productions in grammar.items():
            output_file.write('\t"' + non_terminal + '": [\n')
            for production in productions:
                output_file.write('\t\t' + str(production) + ',\n')
            output_file.write('\t],\n')
        output_file.write("}")
    return grammar

# Nombre del file que contiene la gramática
archivo = 'grammar.txt'

# Leer la gramática desde el archivo
grammar = convertGrammar(archivo)
#print(grammar)