grammar={
	"S": [
		['Statement', 'S'],
		['Statement'],
	],
	"Statement": [
		['Asignacion'],
		['ExpresionImpresion'],
	],
	"Asignacion": [
		['id', 'assign', 'Expresion'],
	],
	"ExpresionImpresion": [
		['escribir', 'opening_par', 'Expresion', 'closing_par'],
	],
	"Expresion": [
		['Valor', 'B'],
	],
	"B": [
		['OperadorA', 'Expresion'],
		['e'],
	],
	"Valor": [
		['string'],
		['id'],
		['num'],
	],
	"OperadorA": [
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
}