grammar={
	"S": [
		['Statement', 'A', 'EOF'],
	],
	"A": [
		['S'],
		['e'],
	],
	"Statement": [
		['Accion'],
		['Funcion'],
	],
	"Accion": [
		['Asignacion'],
		['Impresion'],
		['Impresion_formato'],
		['Limpiar'],
		['Condicional'],
		['Switch'],
		['While'],
		['For'],
		['ForLoop'],
		['DoWhile'],
	],
	"Bloque": [
		['Accion', 'AA'],
	],
	"AA": [
		['Bloque'],
		['e'],
	],
	"Funcion": [
		['funcion', 'Funcion_Sintaxis'],
		['fun', 'Funcion_Sintaxis'],
	],
	"Funcion_Sintaxis": [
		['id', 'opening_par', 'Parametro', 'closing_par', 'Cuerpo_funcion', 'fin'],
	],
	"Parametro": [
		['H'],
		['e'],
	],
	"H": [
		['Valor', 'Parametros'],
	],
	"Parametros": [
		['comma', 'H'],
		['e'],
	],
	"Argumento": [
		['HH'],
		['e'],
	],
	"HH": [
		['Operacion_Arit', 'Argumentos'],
	],
	"Argumentos": [
		['comma', 'HH'],
		['e'],
	],
	"Cuerpo_funcion": [
		['Cuerpo', 'G'],
	],
	"G": [
		['Cuerpo_funcion'],
		['e'],
	],
	"I": [
		['Funcion_R'],
	],
	"Cuerpo": [
		['S'],
		['I'],
	],
	"Funcion_R": [
		['retornar', 'Valor', 'Expresion_Asignacion'],
		['romper'],
		['ret', 'Valor', 'Expresion_Asignacion'],
		['retorno', 'Valor', 'Expresion_Asignacion'],
	],
	"Invocar_Funcion": [
		['opening_par', 'Argumento', 'closing_par'],
	],
	"While": [
		['mientras', 'Condicion', 'S', 'fin'],
	],
	"DoWhile": [
		['repetir', 'Bloque', 'hasta', 'Condicion'],
	],
	"For": [
		['desde', 'opening_par', 'Declaracion_For', 'semicolon', 'Expresion_For', 'semicolon', 'Sentencia_For', 'closing_par', 'Bloque', 'Romper', 'fin'],
	],
	"Declaracion_For": [
		['id', 'assign', 'Num'],
	],
	"Expresion_For": [
		['id', 'Operador_For', 'Valor'],
	],
	"Sentencia_For": [
		['id', 'Senten2'],
	],
	"Senten2": [
		['OperadorMod'],
		['assign', 'Valor', 'Multiples_op'],
	],
	"ForLoop": [
		['para', 'id', 'en', 'Rango', 'Bloque', 'fin'],
	],
	"Rango": [
		['rango', 'opening_par', 'RangoPar', 'closing_par'],
	],
	"RangoPar": [
		['Num', 'T'],
	],
	"T": [
		['comma', 'RangoPar'],
		['e'],
	],
	"Asignacion": [
		['id', 'D'],
	],
	"D": [
		['Asignacion_Unica'],
		['Asignacion_Multiple'],
		['OperadorMod'],
		['Invocar_Funcion'],
		['Asignacion_index'],
		['Metodo'],
	],
	"Asignacion_index": [
		['opening_bra', 'Operacion_Arit', 'closing_bra', 'Asignacion_Unica'],
	],
	"Asignacion_Unica": [
		['OperadorAsignar', 'Asignacion_aux'],
	],
	"Asignacion_aux": [
		['Valor', 'Expresion_Asignacion'],
		['leer', 'opening_par', 'closing_par'],
	],
	"Asignacion_Multiple": [
		['comma', 'Asignacion'],
	],
	"Impresion": [
		['escribir', 'opening_par', 'Valor', 'Valor_imprimir', 'closing_par'],
		['imprimir', 'opening_par', 'Valor', 'Valor_imprimir', 'closing_par'],
		['poner', 'opening_par', 'Valor', 'Valor_imprimir', 'closing_par'],
	],
	"Impresion_formato": [
		['imprimirf', 'opening_par', 'string', 'comma', 'H', 'closing_par'],
	],
	"Limpiar": [
		['limpiar', 'opening_par', 'closing_par'],
	],
	"Expresion_Asignacion": [
		['B'],
		['C'],
		['e'],
	],
	"Valor_imprimir": [
		['E'],
		['e'],
	],
	"Expresion_Parentesis": [
		['opening_par', 'Valor', 'Expresion_Parentesis_Aux'],
	],
	"Expresion_Parentesis_Aux": [
		['Multiples_op', 'closing_par'],
	],
	"C": [
		['comma', 'Valor', 'Expresion_Asignacion'],
	],
	"B": [
		['Operador_Arit', 'Valor', 'Expresion_Asignacion'],
	],
	"Multiples_op": [
		['B2'],
		['e'],
	],
	"B2": [
		['Operador_Arit', 'Valor', 'Multiples_op'],
	],
	"E": [
		['Operador_Arit', 'Valor', 'Valor_imprimir'],
	],
	"Condicional": [
		['si', 'Condicion', 'Cuerpo_Condicion', 'Romper', 'fin'],
	],
	"Condicion": [
		['Valor', 'BB'],
	],
	"BB": [
		['OperadorLog', 'Condicion'],
		['e'],
	],
	"Cuerpo_Condicion": [
		['Cuerpo_Condicion_A', 'GG'],
	],
	"GG": [
		['Cuerpo_Condicion'],
		['e'],
	],
	"Cuerpo_Condicion_A": [
		['Accion', 'Cuerpo_Condicion_B'],
	],
	"Cuerpo_Condicion_B": [
		['Osi'],
		['Sino'],
		['e'],
	],
	"Osi": [
		['osi', 'Condicion', 'Cuerpo_Condicion'],
	],
	"Sino": [
		['sino', 'Cuerpo_Condicion'],
	],
	"Switch": [
		['elegir', 'opening_par', 'id', 'closing_par', 'Caso', 'fin'],
	],
	"Caso": [
		['caso', 'Key', 'colon', 'BloqueS', 'Romper', 'Cuerpo_switch'],
	],
	"BloqueS": [
		['Bloque'],
		['e'],
	],
	"Romper": [
		['romper'],
		['e'],
	],
	"Cuerpo_switch": [
		['Caso'],
		['Defecto'],
		['e'],
	],
	"Defecto": [
		['defecto', 'colon', 'Bloque'],
		['otro', 'colon', 'Bloque'],
	],
	"Valor": [
		['string'],
		['Num'],
		['Expresion_Parentesis'],
		['Lista'],
		['Variable'],
		['nulo'],
		['Diccionario'],
		['Tipo'],
		['ValorBoo'],
		['Convertir_Valor'],
	],
	"Convertir_Valor": [
		['acadena', 'Expresion_Parentesis'],
		['alogico', 'Expresion_Parentesis'],
		['anumero', 'Expresion_Parentesis'],
	],
	"ValorBoo": [
		['verdadero'],
		['falso'],
		['cierto'],
		['not', 'Expresion_Parentesis'],
	],
	"Lista": [
		['opening_bra', 'Posible_comma', 'closing_bra'],
	],
	"Element_lista": [
		['Operacion_Arit', 'J'],
	],
	"J": [
		['Element_lista_final'],
		['e'],
	],
	"Element_lista_final": [
		['comma', 'Posible_comma'],
	],
	"Posible_comma": [
		['Element_lista'],
		['e'],
	],
	"Variable": [
		['id', 'F'],
	],
	"F": [
		['Llamar_elemen_lista'],
		['Invocar_Funcion'],
		['Metodo'],
		['e'],
	],
	"Metodo": [
		['period', 'Variable'],
	],
	"Llamar_elemen_lista": [
		['opening_bra', 'Valor_Asignacion', 'closing_bra', 'FF'],
	],
	"FF": [
		['opening_bra', 'Operacion_Arit', 'closing_bra'],
		['e'],
	],
	"Valor_Asignacion": [
		['Operacion_Arit'],
	],
	"Operacion_Arit": [
		['Valor', 'Operacion_Arit2'],
	],
	"Operacion_Arit2": [
		['Operador_Arit', 'Operacion_Arit'],
		['e'],
	],
	"Diccionario": [
		['opening_key', 'Element_dicc', 'closing_key'],
	],
	"Element_dicc": [
		['Key', 'colon', 'Valor_dicc', 'Element_dicc_final'],
	],
	"Element_dicc_final": [
		['comma', 'Element_dicc'],
		['e'],
	],
	"Key": [
		['Num'],
		['string'],
		['Convertir_Valor'],
	],
	"Valor_dicc": [
		['Operacion_Arit'],
		['Funcion_dicc'],
	],
	"Tipo": [
		['tipo', 'opening_par', 'Valor', 'closing_par'],
	],
	"Funcion_dicc": [
		['funcion', 'Funcion_Sintaxis_dicc'],
		['fun', 'Funcion_Sintaxis_dicc'],
	],
	"Funcion_Sintaxis_dicc": [
		['opening_par', 'Parametro', 'closing_par', 'Cuerpo_funcion', 'fin'],
	],
	"Num": [
		['num'],
		['minus', 'num'],
		['plus', 'num'],
	],
	"Operador_Arit": [
		['and'],
		['concat'],
		['div'],
		['equal'],
		['geq'],
		['leq'],
		['less'],
		['greater'],
		['minus'],
		['mod'],
		['neq'],
		['or'],
		['plus'],
		['power'],
		['regex'],
		['times'],
	],
	"OperadorAsignar": [
		['assign'],
		['mod_assign'],
		['div_assign'],
		['times_assign'],
		['minus_assign'],
		['plus_assign'],
	],
	"OperadorMod": [
		['increment'],
		['decrement'],
	],
	"OperadorLog": [
		['and'],
		['or'],
		['leq'],
		['geq'],
		['equal'],
		['neq'],
		['less'],
		['greater'],
		['regex'],
	],
	"Operador_For": [
		['less'],
		['greater'],
		['leq'],
		['geq'],
	],
}