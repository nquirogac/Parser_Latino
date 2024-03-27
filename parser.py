from convertGrammar import grammar

primeros = {}
follows = {}
predicts = {}

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

def getFollows(symbol):
    #print("sigue",symbol)
    follows[symbol] = set()
    if symbol == "S": 
        follows[symbol].add('$')
    for nonTerminal in grammar.keys():
        ##print(nonTerminal)
        for rule in grammar[nonTerminal]:
            #print(nonTerminal, rule)
            if symbol in rule:
                index = rule.index(symbol)
                #print("esta en ",index)
                if index == len(rule)-1:
                    #print("es el ultimo")
                    if not follows.__contains__(nonTerminal):
                        getFollows(nonTerminal)
                    #print("se le agrega",follows[nonTerminal])
                    follows[symbol] = follows[symbol].union(follows[nonTerminal])
                elif rule[index+1] in grammar.keys():
                    #print("el que le sigue es", rule[index+1])  
                    if not primeros.__contains__(rule[index+1]):
                        getFirsts(rule[index+1])
                    while index < len(rule)-1 and rule[index+1] in grammar.keys():
                        #print("index en while ",index)
                        if not primeros.__contains__(rule[index+1]):
                            getFirsts(rule[index+1])
                        #print("se le agrega",primeros[rule[index+1]])
                        follows[symbol] = follows[symbol].union(primeros[rule[index+1]])
                        if 'e' in primeros[rule[index+1]]:
                            index += 1
                        else:
                            break
                    if index == len(rule)-1:
                        #print("se le agrega el no terminal",nonTerminal)
                        if not follows.__contains__(nonTerminal):
                            getFollows(nonTerminal)
                        follows[symbol] = follows[symbol].union(follows[nonTerminal])    
                else:
                    follows[symbol].add(rule[index+1])
                        
        if 'e' in follows[symbol]:
            follows[symbol].remove('e')
        #print(follows)

def getPredict(symbol):
    for rule in grammar[symbol]:
        strRule = ' '.join(rule)
        setPredict = symbol+" -> "+strRule
        follow = True
        predicts[setPredict] = set()
        if rule[0] in grammar.keys():
            for element in rule:
                if element not in grammar.keys():
                    predicts[setPredict] = predicts[setPredict].union({element})
                    follow = False
                    break
                elif element in grammar.keys() and not primeros.__contains__(element):
                    getFirsts(element)
                predicts[setPredict] = predicts[setPredict].union(primeros[element])
                if 'e' not in primeros[element]:
                    follow = False
                    break
                elif 'e' in primeros[element]:
                    predicts[setPredict].remove('e')
            if follow and 'e' in primeros[rule[-1]]: #si primeros de alfa tiene e, hay que agregar sigue de A
                predicts[setPredict] = predicts[setPredict].union(follows[symbol])  
                
        else:
            if rule[0] == 'e':
                predicts[setPredict] = predicts[setPredict].union(follows[symbol])
            else:
                predicts[setPredict].add(rule[0])

        if 'e' in predicts[setPredict]:
            predicts[setPredict].remove('e')

for no_terminal in reversed(grammar.keys()):
    #print(no_terminal)
    getFirsts(no_terminal)
for no_terminal in grammar.keys():
    getFollows(no_terminal)
for no_terminal in grammar.keys():
    getPredict(no_terminal)


print(predicts)

