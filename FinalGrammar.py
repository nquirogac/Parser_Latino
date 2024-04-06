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
		['Condicional'],
		['Funcion'],
		['Switch'],
		['While'],
	],
	"Accion": [
		['Asignacion'],
		['Impresion'],
	],
	"Bloque": [
		['Accion', 'AAA'],
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
		['Condicional'],
		['While'],
		['I'],
	],
	"Funcion_R": [
		['retornar', 'Valor', 'Expresion_Asignacion'],
		['regresar', 'Valor', 'Expresion_Asignacion'],
		['ret', 'Valor', 'Expresion_Asignacion'],
		['retorno', 'Valor', 'Expresion_Asignacion'],
	],
	"Invocar_Funcion": [
		['opening_par', 'Argumento', 'closing_par'],
	],
	"While": [
		['mientras', 'Condicion', 'S', 'fin'],
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
	"Condicional": [
		['si', 'Condicion', 'Cuerpo_Condicion', 'fin'],
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
		['Condicional'],
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
		['elegir', 'opening_par', 'id', 'closing_par', 'Caso', 'Cuerpo_switch'],
	],
	"Caso": [
		['caso', 'Key', 'colon'],
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
	],
	"Valor_dicc": [
		['Valor'],
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
	],
}