import re
import sys
from convertGrammar import grammar

primeros = {}
follows = {}
predicts = {}

keyWords = "acadena|alogico|anumero|leer|limpiar|caso|cierto|verdadero|defecto|otro|desde|elegir|error|escribir|imprimir|poner|falso|fin|funcion|fun|hasta|imprimirf|mientras|nulo|osi|repetir|retorno|retornar|ret|romper|tipo|rango|si|sino|fun|funcion|para|en|regresar"

operators = {"&&": "and", "\|\|": "or", "\.\.": "concat", "\.": "period", "\,": "comma", ";": "semicolon",":": "colon", "\{": "opening_key", "\}": "closing_key", "\[": "opening_bra", "\]": "closing_bra", "\(": "opening_par", "\)": "closing_par", "(\+\+)": "increment", "\-\-": "decrement", "%=": "mod_assign", "/=": "div_assign", "\*=": "times_assign", "-=": "minus_assign", "\+=": "plus_assign", "\+": "plus", "-": "minus", "\*": "times", "/": "div", "\^": "power", "%": "mod", "<=": "leq", ">=": "geq", "==": "equal", "!=": "neq", "<": "less", ">": "greater", "=": "assign", "!": "not", "~=": "regex"}
operatorsKeys = "|".join(operators.keys())

idsRegex = "^[a-zA-Z_][a-zA-Z0-9_]*" 
commentsRegex = "//|#"
multiLineCommentsRegex = r'/\*(.*?)\*/' 
numbersRegex = "\d+(\.\d+)?"
stringRegex = r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\''

linesAsText = sys.stdin.read()
lines = linesAsText.split("\n")
tokens = []

def maximalToken(line, flag, j, num=False):
    if (j+1 == len(line)):
        return True
    elif (j+1 < len(line) ):              #if the token is a space
        if (line[j+1] == " "): 
            return True
        elif (line[j+1] == "\n"): 
            return True     
        elif ((re.match(operatorsKeys, line[j+1]) or re.match(commentsRegex, line[j+1:j+2])) and not num):
            return True
        elif(num):
            if (re.match("\d", line[j+1])):
                return False
            elif (re.match("\.", line[j+1])) and maximalToken(line, flag, j+1, True):
                return True 
            elif (re.fullmatch(numbersRegex, line[flag:j+3]))==None:
                return True
        else:
            if (re.match("\w", line[j+1])) and (re.match(r'[^\WñçáéíóúÁÉÍÓÚüÜ]', line[j+1])):
                return False
            else:
                return True
    else:
        return False

def findOperators(line, flag, j, i):
    for key in operators:
        if(re.fullmatch(key, line[flag:j+1])):
            #print("<tkn_"+operators[key]+","+str(i+1)+","+str(flag+1)+">")
            tokens.append(["OPERATOR",operators[key],str(i+1),str(flag+1)])
              
def defineOperators(line, flag, j, i):
    if (j+1 == len(line)):
        findOperators(line, flag, j, i)
        return True
    elif (j+1 <= len(line) and ((line[j+1] == " ") or (line[j+1] == "\n") or (j+1 == len(line)))):              #if the token is a space
        findOperators(line, flag, j, i)
        return True
    elif (re.match(commentsRegex, line[flag:j+2])): 
        #print("comentario")  
        return False  
    elif  re.match("\w+", line[j+1]):
        findOperators(line, flag, j, i) 
        return True  
    elif (re.fullmatch(operatorsKeys, line[flag:j+2])==None):
        findOperators(line, flag, j, i) 
        return True 
    else:
        return False       

def defineMultiLineComments(line, flag, j):
    comentarios = re.findall(multiLineCommentsRegex, linesAsText, re.DOTALL)
    if len(comentarios) == 0:
        return False
    elif '/*' in comentarios[0] or '*/' in comentarios[0]:
        return False
    return True

def lexer(linesAsText, lines):
    ignore = False
    romper = False
    for i in range(len(lines)):
        flag = 0
        line = lines[i]
        contador = 0
        if not line.strip():
            continue
        for j in range(0,len(line)):    
            if (re.fullmatch(keyWords, line[flag:j+1])):           #if the token is a keyword
                if ignore:
                    continue 
                elif (maximalToken(line, flag, j)):
                    #print("<"+line[flag:j+1]+","+str(i+1)+","+str(flag+1)+">")
                    tokens.append(["KEYWORD",line[flag:j+1],str(i+1),str(flag+1)])
                    flag = j+1
                else:
                    continue  
            elif (re.match(commentsRegex, line[flag:j+2])):         #if the token is a comment
                if ignore:
                    break 
                else:
                    break
            elif(re.match(operatorsKeys, line[flag:j+1]) or re.match(operatorsKeys, line[flag:j+2]) or ignore):     #if the token is an operator or special character
                if (re.match(r'/\*', line[flag:j+2])) and not ignore:
                    if(not defineMultiLineComments(line, flag, j)):
                        
                        #print(">>> Error lexico (linea:", str(i+1)+ ", posicion:", str(flag+1)+")")

                        romper = True
                        break
                    else:
                        
                        
                        ignore = True
                        flag = j+2
                elif (re.search('\*/', line[flag:j+1])) and ignore:
                    ignore = False
                    flag = j+1
                #elif (re.match(r'\*/', line[flag:j+2])) and not ignore:
            
                    #romper = True
                    #break
                elif not ignore:
                    if defineOperators(line, flag, j, i):
                        flag = j+1
                else:
            
                    continue        
            elif (re.match(idsRegex, line[flag:j+1])):                  #if the token is an identifier
                if ignore:
                    continue      
                elif (maximalToken(line, flag, j)):
                    #print("<id,"+line[flag:j+1]+","+str(i+1)+","+str(flag+1)+">")
                    tokens.append(["ID",line[flag:j+1],str(i+1),str(flag+1)])
                    flag = j+1
                else:
                    continue
            elif (re.match(numbersRegex, line[flag:j+1])):     #if the token is a number
                if ignore:
                    continue 
                elif(maximalToken(line, flag, j, True)):
                    #print("<tkn_real,"+line[flag:j+1]+","+str(i+1)+","+str(flag+1)+">")
                    tokens.append(["REAL",line[flag:j+1],str(i+1),str(flag+1)])
                    flag = j+1
            elif len(re.findall(stringRegex, line[flag:len(line)])) > 0 and re.match((r'"|\''), line[flag]) and not ignore:  #if the token is a string
                if ignore:
                    continue                                          
                elif contador==0 :
                    if re.match((r'"|\''), line[j]) and j!=flag:
                        flag = flag + len(foundStrings[0])
                    else:
                        foundStrings = re.findall(stringRegex, line[flag:len(line)])
                        cadena = foundStrings[0]
                        cadena = cadena[1:-1]
                        contador = len(foundStrings[0])-2
                        #print("<tkn_str,"+cadena+","+str(i+1)+","+str(flag+1)+">")
                        tokens.append(["STRING",cadena,str(i+1),str(flag+1)])
                else:
                    contador = contador - 1
            elif (j+1 <= len(line)) and ((line[j] == " ") or (line[j] == "\t") or (line[j] == "\n")):                           #if the token is a space
                flag = j+1
            else:
                if not ignore:
                    #print(">>> Error lexico (linea:", str(i+1)+ ", posicion:", str(flag+1)+")")
                    romper = True
                    break
        linesAsText = '\n'.join(linesAsText.split("\n")[1:])
        if linesAsText.split("\n")[0] == "" or linesAsText.split("\n")[0] == "\n":
            linesAsText = '\n'.join(linesAsText.split("\n")[1:])
        if romper:
            break
    return tokens
# Función para calcular el conjunto de primeros
def getFirsts (symbol):
    if primeros.__contains__(symbol):
        return primeros
    #print(symbol)
    primeros[symbol] = set()
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

def checkLL1():
    for nonTerminal in grammar.keys():
        setsNonTerminal = [conjunto for produccion, conjunto in predicts.items() if produccion.startswith(nonTerminal)]
        #print(nonTerminal,setsNonTerminal)
        if not setsNonTerminal:
            return True
        elementos = set()
        for conjunto in setsNonTerminal:
            for elemento in conjunto:
                if elemento in elementos:
                    return False
                elementos.add(elemento)
    return True

def parser():
    global currentRule
    currentRule = ["S"]
    for token in tokens:
        print(token)
        if seePredicts(token):
            expected = currentRule.pop(0)
            if(not emparejar(token[1],expected)):
                print("Error sintactico en linea, se esperaba",expected)
                break
    print("El analisis sintactico ha finalizado exitosamente.")

def seePredicts(token):
    current = currentRule.pop(0)
    posiblePredicts = set()
    if current not in grammar.keys():
        currentRule.insert(0,current)
        return True
    while current in grammar.keys():
        for rules in grammar[current]:
            strRule = ' '.join(rule)
            setPredict = symbol+" -> "+strRule
            posiblePredicts = posiblePredicts.union(predicts[setPredict])
        if token[1] not in posiblePredicts:
            print("Error sintactico en linea, se esperaba",posiblePredicts)
            return False
        else:
            for rules in grammar[current]:
                strRule = ' '.join(rule)
                setPredict = symbol+" -> "+strRule
                if token[1] in predicts[setPredict]:
                    currentRule += rules
                    print ("Nueva regla",currentRule)
                    break
                    if currentRule[0] == 'e' and len(currentRule) > 1:
                        currentRule.pop(0)
                    else:
                        break
        if len(currentRule) == 0:
            print("Error sintactico en linea, se esperaba",posiblePredicts)
            return False
        current = currentRule.pop(0)
    
    currentRule.insert(0,current)
    return True

def emparejar(token, waitedToken):
    if len(currentRule) == 0: return False
    if token == "$" and currentRule[0] == "e":
        return True
    if token == waitedToken:
        return True
    else:
        currentRule.insert(0,waitedToken)
        return False

for nonTerminal in reversed(grammar.keys()):
    #print(nonTerminal)
    getFirsts(nonTerminal)
for nonTerminal in grammar.keys():
    getFollows(nonTerminal)
for nonTerminal in grammar.keys():
    getPredict(nonTerminal)

#print(checkLL1())
lexer(linesAsText, lines)
tokens.append(["FIN","$"])
parser()



