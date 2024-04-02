grammar={
	"S": [
		['Statement', 'A'],
	],
	"A": [
		['S'],
		['e'],
	],
	"Statement": [
		['Accion'],
		['Condicion'],
		['Funcion'],
	],
	"Accion": [
		['Asignacion'],
		['Impresion'],
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
		['id', 'Parametros'],
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
		['Valor', 'Argumentos'],
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
		['Accion'],
		['Condicion'],
		['I'],
	],
	"Funcion_R": [
		['retornar', 'Valor', 'Expresion_Asignacion'],
		['regresar', 'Valor', 'Expresion_Asignacion'],
		['ret', 'Valor', 'Expresion_Asignacion'],
	],
	"Invocar_Funcion": [
		['opening_par', 'Argumento', 'closing_par'],
	],
	"Asignacion": [
		['id', 'D'],
	],
	"D": [
		['Asignacion_Unica'],
		['Asignacion_Multiple'],
		['OperadorMod'],
		['Invocar_Funcion'],
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
		['opening_par', 'Valor', 'B', 'closing_par'],
	],
	"C": [
		['comma', 'Valor', 'Expresion_Asignacion'],
	],
	"B": [
		['Operador_Arit', 'Valor', 'Expresion_Asignacion'],
	],
	"E": [
		['Operador_Arit', 'Valor', 'Valor_imprimir'],
	],
	"Condicion": [
		['si'],
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
	],
	"Lista": [
		['opening_bra', 'Element_lista', 'closing_bra'],
	],
	"Element_lista": [
		['Valor', 'Element_lista_final'],
	],
	"Element_lista_final": [
		['comma', 'Element_lista'],
		['e'],
	],
	"Variable": [
		['id', 'F'],
	],
	"F": [
		['opening_bra', 'Num', 'closing_bra'],
		['Invocar_Funcion'],
		['e'],
	],
	"Diccionario": [
		['opening_key', 'Element_dicc', 'closing_key'],
	],
	"Element_dicc": [
		['Key', 'colon', 'Valor', 'Element_dicc_final'],
	],
	"Element_dicc_final": [
		['comma', 'Element_dicc'],
		['e'],
	],
	"Key": [
		['Num'],
		['string'],
	],
	"Tipo": [
		['tipo', 'opening_par', 'Valor', 'closing_par'],
	],
	"Num": [
		['num'],
		['minus', 'num'],
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
}