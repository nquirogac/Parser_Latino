noTerminales = []

import sys

tokens = {"=": "assign", ".": "period", ",": "comma", ";": "semicolon", "]": "closing_bra", "[": "opening_bra", "(": "opening_par",
          ")": "closing_par", "*": "times", "/": "div", "%": "mod", "+": "plus", "-": "minus", "==": "equal", "!=": "neq", "<": "less",
          ">": "greater", ">=": "geq", "<=": "leq", "?": "question_mark"}

inv_tokens = {"tkn_"+v: k for k, v in tokens.items()}
inv_tokens["$"] = "final de archivo"

reservadas = {"Get", "next", "input", "Put", "to", "output", "if", "elseif", "else", "while", "for", "integer", "float",
              "array", "Function", "returns", "SquareRoot", "RaiseToPower", "AbsoluteValue", "RandomNumber", "SeedRandomNumbers",
              "with", "decimal", "places", "size", "Main", "or", "and", "not", "nothing"}

class Number:
    num_allowed = [str(x) for x in range(10)] + ["."]
    error = False

    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column

    def correct(self, char):
        if ("." in self.value and char == "."):
            return False
        return char in self.num_allowed

    def update(self, char):
        if self.correct(char):
            self.value = self.value.strip() + char
            return True
        return False

    def __str__(self):
        name = "tkn_integer"
        if "." in self.value:
            if self.value[-1] != ".":
                name = "tkn_float"
            else:
                self.value = self.value[:len(self.value) - 1]
                return "<{},{},{},{}>".format(name, self.value, self.row, self.column)+"\n<{},{},{}>".format("tkn_"+tokens["."], self.row, self.column+len(self.value))
        return "<{},{},{},{}>".format(name, self.value, self.row, self.column)


class Sign:
    starts_with = ["=", ">", "<", "!"]
    error = False

    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column
        self.error = False

    def correct(self, char):
        if len(self.value) > 1:
            error = True
            return False
        if len(self.value) == 0:
            if char == "/": return True
            error = char not in self.starts_with
            return not error
        else:
            if char == "/" and self.value[0] in (self.starts_with+["/"]): return True
            if self.value[0] not in self.starts_with: return False
            error = char != "="
            return not error

    def update(self, char):
        if self.correct(char):
            self.value = self.value.strip() + char
            return True
        return False

    def __str__(self):
        if self.error: return f">>> Error lexico (linea: {self.row}, posicion: {self.column})"
        if self.value == "//":
            return "<{},{},{}>".format("tkn_" + tokens[self.value[0]], self.row, self.column)+"\n<{},{},{}>".format("tkn_" + tokens[self.value[1]], self.row, self.column+1)
        return "<{},{},{}>".format("tkn_" + tokens[self.value], self.row, self.column)


class Identificador:
    starts_with = [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]
    id_allowed = starts_with + [str(x) for x in range(10)] + ["_"]
    error = False

    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column + 1

    def correct(self, char):
        if len(self.value) == 0:
            return char in self.starts_with
        elif len(self.value) == 1:
            return (self.value[0] in self.starts_with) and (char in self.id_allowed)
        return char in self.id_allowed

    def update(self, char):
        if self.correct(char):
            self.value = self.value.strip() + char
            return True
        return False

    def __str__(self):
        name = "id"
        if self.value in reservadas:
            return "<{},{},{}>".format(self.value, self.row, self.column)
        if self.value in tokens:
            return "<{},{},{}>".format("tkn_" + tokens[self.value], self.row, self.column)
        for x in self.value.strip():
            if (x not in self.id_allowed and x not in tokens) or self.error:
                self.error = True
                return f">>> Error lexico (linea: {self.row}, posicion: {self.column})"
        return "<{},{},{},{}>".format(name, self.value, self.row, self.column)


class String(Identificador):

    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column

    def correct(self, char):
        if len(self.value) == 0:
            return char == '"'
        positions = [x for x in range(len(self.value)) if self.value[x] == '"']
        flag = False
        for i in positions:
            if i>0 and i<len(self.value) and self.value[i-1] != "\\": flag = True
        if self.value.count('"') > 1 and flag:
            return False
        return True

    def update(self, char):
        if self.correct(char):
            self.value += char
            return True
        return False

    def __str__(self):
        if self.value[-1] != '"' or self.value.count('"')-self.value.count('\\"')<2:
            self.error = True
            return f">>> Error lexico (linea: {self.row}, posicion: {self.column})"
        return "<tkn_str,{},{},{}>".format(self.value[1:len(self.value)-1], self.row, self.column)

class Grammar:
    no_terminals = []
    rules = []

    def __init__(self, no_terminals):
        self.no_terminals = no_terminals
        for symbol in self.no_terminals:
            for rule in symbol.rules:
                self.rules.append(rule)

class Rule:
    def __init__(self, nonTerminal, production):
        self.nonTerminal = nonTerminal
        self.production = production
        self.predict = set()

    def getPredictT(self):
        if self.production == ["e"]:
            if not self.nonTerminal.follow: self.nonTerminal.getFollows()
            self.predict = self.predict.union(self.nonTerminal.follow)
        elif "e" in self.production:
            auxRule = Rule(self.nonTerminal, self.production[self.production.index("e") + 1:])
            auxRule.getPredict()
            self.predict = auxRule.predict
        else:
            self.predict = {self.production[0]}

    def getPredict(self):
        follow = True
        if type(self.production[0]) is NonTerminal:
            # Cuadrarlo bien: Meter los primeros del siguiente mientras el actual tenga e; si es el ultimo y tiene e, entonces meter los siguientes del simbolo de la regla | S -> A B C
            for i in self.production:
                if type(i) is not NonTerminal:
                    self.predict = self.predict.union({i})
                    follow = False
                    break
                if not i.first: i.getFirsts()
                self.predict = self.predict.union(i.first)
                if "e" not in i.first:
                    follow = False
                    break

                if "e" in self.predict: self.predict.remove("e")

            if follow and "e" in self.production[-1].first:
                if not self.nonTerminal.follow: self.nonTerminal.getFollows()
                self.predict = self.predict.union(self.nonTerminal.follow)

        else:
            self.getPredictT()

        if "e" in self.predict: self.predict.remove("e")

    def __repr__(self):
        return f"{self.nonTerminal} -> {self.production}"

class NonTerminal:
    def __init__(self, name):
        self.name = name
        self.rules = []
        self.first = set()
        self.follow = set()

    def getFirsts(self):
        for rule in self.rules:
            for item in rule.production:
                if type(item) is not NonTerminal:
                    self.first.add(item)
                    if item != "e": break
                else:
                    if not item.first: item.getFirsts()
                    self.first = self.first.union(item.first)
                    if "e" not in item.first:
                        if "e" in self.first: self.first.remove("e")
                        break

    def getFollows(self):
        if self.name == "INICIAL": self.follow.add("$")
        for rule in Grammar.rules:
            if self in rule.production:
                index = rule.production.index(self)
                if index == len(rule.production) - 1:
                    if not rule.nonTerminal.follow: rule.nonTerminal.getFollows()
                    self.follow = self.follow.union(rule.nonTerminal.follow)
                elif type(rule.production[index + 1]) is NonTerminal:
                    if not rule.production[index + 1].first: rule.production[index + 1].getFirsts()
                    while (index < len(rule.production) - 1 and type(rule.production[index + 1]) is NonTerminal):
                        if not rule.production[index + 1].first: rule.production[index + 1].getFirsts()
                        self.follow = self.follow.union(rule.production[index + 1].first)
                        if "e" in rule.production[index + 1].first:
                            index += 1
                        else:
                            break
                    if index == len(rule.production) - 1:
                        if not rule.nonTerminal.follow: rule.nonTerminal.getFollows()
                        self.follow = self.follow.union(rule.nonTerminal.follow)
                else:
                    self.follow.add(rule.production[index + 1])

        if "e" in self.follow: self.follow.remove("e")

    def __repr__(self):
        return self.name


totalLineas = [0,0]

def lexer():
    global totalLineas
    code = sys.stdin.read().split("\n")
    for i in code:
      if i.strip()[:2] != "//": totalLineas[0] += 1
    totalLineas[1] = len(code)
    exit = False
    blank = True
    row = 0
    lexico = []

    for line in code:

        row += 1
        i = 0
        group = ""
        ident = Identificador("", row, i)
        blank = True

        while i < (len(line)):
            if ident.correct(line[i]):
                ident.update(line[i])
                group += line[i]
                if group.strip() not in ["/", "//"]: blank = False
            else:
                if group.strip():
                    try:
                        float(group.strip())
                        ident = Number(group, row, ident.column)
                        if not ident.correct(group):  # End of float
                            lexico.append(str(ident))
                            group = ""
                            ident = Identificador("", row, i)
                        elif ident.update(line[i]):  # Continue float
                            group += line[i]
                            if group.strip() not in ["/", "//"]: blank = False
                            i += 1
                        else:  # End Integer
                            lexico.append(str(ident))
                            group = ""
                            ident = Identificador("", row, i)
                        continue
                    except:
                        temp = Sign(ident.value, ident.row, ident.column)
                        if temp.correct(line[i]):
                            ident = Sign(ident.value, ident.row, ident.column)
                            if ident.update(line[i]):
                                group += line[i]
                                if group.strip() not in ["/", "//"]: blank = False
                                i += 1
                                continue
                        else:
                            temp = String("", ident.row, ident.column)
                            if temp.correct(ident.value):
                                ident = String(ident.value, ident.row, ident.column)
                                if ident.update(line[i]):
                                    group += line[i]
                                    i += 1
                                    continue
                        # print("Except:", group, ident)
                        pass
                    if ident.value == "//" and blank: break
                    lexico.append(str(ident))
                    blank = False
                    if ident.error:
                        exit = True
                        break
                group = line[i]
                if group.strip() not in ["/", "//", ""]: blank = False
                ident = Identificador(group, row, i)
                if ident.value == "_": ident.error = True
            i += 1
        if exit: break
        if ident.value == "//" and blank: continue
        if ident.value.strip():
            if ident.value in "0123456789": ident = Number(ident.value, ident.row, ident.column)
            lexico.append(str(ident))
        if ident.error: break

    return lexico

def getIndex(name, noTerminales=noTerminales):
    for nt in range(len(noTerminales)):
        if name == noTerminales[nt].name:
            return nt
    return -1

def getGrammar():
    # Sin writefile
    gramatica = """INICIAL -> Function id tkn_opening_par AO tkn_closing_par returns AQ A AR
    INICIAL -> A
    A -> id B Q
    A -> SeedRandomNumbers tkn_opening_par D tkn_closing_par Q
    A -> Put S
    A -> U V id Q
    A -> for id C tkn_assign D tkn_semicolon Y tkn_semicolon id C tkn_assign D X Q
    A -> while Y X Q
    A -> if Y X AM Z
    B -> C tkn_assign P
    B -> tkn_opening_par N tkn_closing_par
    C -> tkn_opening_bra D tkn_closing_bra
    C -> tkn_period size
    C -> e
    D -> I F E
    E -> J F E
    E -> e
    F -> H G
    G -> K H G
    G -> e
    H -> L
    H -> tkn_opening_par D tkn_closing_par
    I -> tkn_minus
    I -> e
    J -> tkn_plus
    J -> tkn_minus
    K -> tkn_times
    K -> tkn_div
    K -> tkn_mod
    L -> tkn_integer
    L -> id R
    L -> SquareRoot tkn_opening_par D tkn_closing_par
    L -> AbsoluteValue tkn_opening_par D tkn_closing_par
    L -> RaiseToPower tkn_opening_par D tkn_comma D tkn_closing_par
    L -> RandomNumber tkn_opening_par D tkn_comma D tkn_closing_par
    L -> tkn_float
    M -> id C
    N -> H O
    N -> e
    O -> tkn_comma H O
    O -> e
    P -> D
    P -> Get next input
    Q -> A
    Q -> e
    R -> C
    R -> tkn_opening_par N tkn_closing_par
    S -> tkn_str to output Q
    S -> D to output T Q
    T -> with D decimal places
    T -> e
    U -> float
    U -> integer
    V -> array tkn_opening_par W
    V -> e
    W -> tkn_question_mark tkn_closing_par
    W -> D tkn_closing_par
    X -> id B
    X -> SeedRandomNumbers tkn_opening_par D tkn_closing_par
    X -> Put S
    X -> U V id
    X -> for id C tkn_assign D tkn_semicolon Y tkn_semicolon id C tkn_assign D X Z
    X -> while Y X Z
    X -> if Y X AM Z
    Y -> AB AA
    Z -> X
    Z -> e
    AA -> AJ AB AA
    AA -> e
    AB -> AD AC
    AC -> AK AD AC
    AC -> e
    AD -> not tkn_opening_par Y tkn_closing_par
    AD -> AE
    AE -> I AG AF
    AF -> J AG AF
    AF -> e
    AG -> AI AH
    AH -> K AI AH
    AH -> e
    AI -> L
    AI -> tkn_opening_par Y tkn_closing_par
    AJ -> tkn_equal
    AJ -> tkn_deq
    AK -> tkn_geq
    AK -> tkn_leq
    AK -> tkn_less
    AK -> tkn_greater
    AL -> C
    AL -> tkn_opening_par N tkn_closing_par
    AM -> elseif Y X AM
    AM -> AN
    AN -> else X
    AN -> e
    AO -> U id AP
    AO -> e
    AP -> tkn_comma U id AP
    AP -> e
    AQ -> U V id
    AQ -> nothing
    AR -> Function AS
    AS -> id tkn_opening_par AO tkn_closing_par returns AQ A AR
    AS -> Main tkn_opening_par tkn_closing_par returns nothing A"""
    # gramatica = sys.stdin.read() #Con writefile
    reglas = gramatica.replace("\t", " ").split("\n")
    simbolos = set()
    for regla in reglas:
        simbolo = regla.split("->")[0].strip()
        if simbolo not in simbolos:
            simbolos.add(simbolo)
            noTerminales.append(NonTerminal(simbolo))

    for regla in reglas:
        if not regla: break
        derecha = regla.split("->")[1].strip().split(" ")
        produccion = []
        for parte in derecha:
            if parte.isupper():
                index = getIndex(parte)
                if index > -1: produccion.append(noTerminales[index])
            elif parte:
                produccion.append(parte)

        noTerminales[getIndex(regla.split("->")[0].strip())].rules.append(
            Rule(noTerminales[getIndex(regla.split("->")[0].strip())], produccion))

    return noTerminales

def matching(token):
    global next
    if len(next) < 1: return False
    #print("Matching:", token, next[0])
    if token == "$" and next[0] == "e": return True
    temp = next.pop(0)
    if token != temp: next.insert(0, temp)
    return token == temp

def update(token):
    global next
    if len(next)<1: return
    actual = next.pop(0)
    match = False
    posibles = set()

    if type(actual) is not NonTerminal:
        next.insert(0, actual)
        #print("Update:", token, next)
        return

    while type(actual) is NonTerminal:
        for regla in actual.rules:
            posibles = posibles.union(regla.predict)

        if token not in posibles:
            #print("ERROOOOOOOR. SE ESPERABA:", actual, posibles, ". SE ENCONTRO:", token)
            return (actual, posibles)

        else:
            for opcion in actual.rules:
                if token in opcion.predict:
                    next = opcion.production + next
                    #print("Update:", token, next, posibles)
                    if len(next) > 1 and next[0] == "e":
                        next.pop(0)
                    else:
                        break

        if len(next)<1: return (actual, posibles)
        actual = next.pop(0)

    next.insert(0, actual)

def analizarGramatica():
    global next

    for rule in gramatica.rules:
        rule.nonTerminal.getFirsts()
        rule.nonTerminal.getFollows()
        rule.getPredict()

    next = [gramatica.no_terminals[getIndex("INICIAL", gramatica.no_terminals)]]
    update(str(tokens[0]).split(",")[0][1:])

    tokens.append(" $")

    for token in tokens:
        token = str(token)
        cleanToken = token.split(",")[0][1:]
        updated = update(cleanToken)
        if type(updated) is tuple:
            #print("Token error", token)
            lugar = "<" + ":".join(token.split(",")[-2:])
            if cleanToken in inv_tokens.keys():
                nombre = inv_tokens[cleanToken]
            elif cleanToken in ["tkn_str", "tkn_float", "tkn_integer", "id"]:
                nombre = token.split(",")[1]
            else:
                nombre = cleanToken
            esperados = ", ".join(['"' + inv_tokens[i] + '"' if i in inv_tokens.keys() else '"'+i+'"' for i in sorted(updated[1], key=lambda v: v.upper())])
            if cleanToken == "$":
                lugar = "<"+str(totalLineas[1]+1)+":1>"
                print(f'{lugar} Error sintactico: se encontro {nombre}; se esperaba: {esperados}.')
            else:
                print(f'{lugar} Error sintactico: se encontro: "{nombre}"; se esperaba: {esperados}.')
            return
        if not matching(cleanToken):
            #print("ERROR 1", token, tokens[-2], next)
            lugar = "<"+":".join(token.split(",")[-2:])
            if cleanToken in inv_tokens.keys():
                nombre = inv_tokens[cleanToken]
                if cleanToken != "$":
                    nombre = ': "'+nombre+'"'
                else:
                    nombre = " "+nombre
                    lugar = "<"+str(totalLineas[1]+1)+":1>"
            elif cleanToken in ["tkn_str", "tkn_float", "tkn_integer", "id"]:
                nombre = ': "'+token.split(",")[1]+'"'
            else:
                nombre = ': "'+cleanToken+'"'
            expected = next[0]
            if next[0] in inv_tokens.keys(): expected = inv_tokens[next[0]]
            print(f'{lugar} Error sintactico: se encontro{nombre}; se esperaba: "{expected}".')
            return

    print("El analisis sintactico ha finalizado exitosamente.")

gramatica = Grammar(getGrammar())
tokens = lexer()
analizarGramatica()