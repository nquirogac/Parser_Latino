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
	],
	"Accion": [
		['Asignacion'],
		['Impresion'],
	],
	"Asignacion": [
		['id', 'D'],
	],
	"D": [
		['Asignacion_Unica'],
		['Asignacion_Multiple'],
		['OperadorMod'],
	],
	"Asignacion_Unica": [
		['OperadorAsignar', 'Valor', 'Expresion_Asignacion'],
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
		['e'],
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