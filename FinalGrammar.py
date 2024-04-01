grammar={
	"S": [
		['Statement', 'A'],
	],
	"A": [
		['S'],
		['e'],
	],
	"Statement": [
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
	"Valor": [
		['string'],
		['id'],
		['Num'],
		['Expresion_Parentesis'],
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