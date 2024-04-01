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
		['Expresion_Impresion'],
	],
	"Asignacion": [
		['id', 'D'],
	],
	"D": [
		['Asignacion_Unica'],
		['Asignacion_Multiple'],
	],
	"Asignacion_Unica": [
		['OperadorAsignar', 'Expresion'],
	],
	"Asignacion_Multiple": [
		['comma', 'Asignacion'],
	],
	"Expresion_Impresion": [
		['escribir', 'opening_par', 'Expresion', 'closing_par'],
	],
	"Expresion": [
		['Valor', 'B', 'C'],
	],
	"C": [
		['comma', 'Expresion'],
		['e'],
	],
	"B": [
		['Operador_Arit', 'Expresion'],
		['e'],
	],
	"Valor": [
		['string'],
		['id'],
		['Num'],
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
}