# encoding: utf-8

TITLE = {
	'CALIPER':	u"Calibrar motor",
	'COPYRIGHT':	u"Informações de Copyright",
	'MOVE':		u"Realizar varredura"
}

HELP = {
	'CALIPER':	u"Aqui deveria ficar o texto explicando como deve funcionar a calibragem",
	'MOVE':	u"Aqui deveria ficar o texto explicando como deve funcionar a varredura, com divisão para 1, 2 ou 3 eixos"
}

MENU = {
	'CALIPER':	u"CALIBRAR",
	'CONFIG':	u"CONFIGURAÇÕES",
	'COPYRIGHT':	u"COPYRIGHT",
	'MOVE': u"VARREDURA",
		'MOVE_1D': u"VARREDURA 1D",
		'MOVE_2D': u"VARREDURA 2D",
		'MOVE_3D': u"VARREDURA 3D",
	'HELP':	u"AJUDA"
}

FIELDS = {
	#CAMPOS VARREDURA
	'AXIS': u'Eixo',
		'X': u'Eixo X',
		'Y': u'Eixo y',
		'Z': u'Eixo z',
	'DIRECTION': u'Direção',
		'FORWARD': u'Para frente',
		'REVERSE': u'Para trás',
	'STEPS': u'Passos',
	'ACQUISTION_RATE': u'Passos por pontos',
	'SECONDARY_AXIS': u'Eixo secundário',
	'TOTAL_STEPS_SECONDARY': u'Quant. total deslocamento secundário',
	'SIZE_STEPS_SECONDARY': u'Quant. passos por deslocamento',
	'BUTTON': u'Realizar varredura'
}

ERROR = {
	'EXCEPTION':	u"Ocorreu algum erro: {0}",
	'REQUEST_EXCEPTION':	u"Ocorreu algum erro na conexão: {0}",
	'SCAN_EXCEPTION': u"Ocorreu um erro durante a varredura. Tente novamente ou verifique os logs das demais aplicações para descobrir a causa",
	'REQUIRED_FIELD':	u"Por favor, preencha o(s) campo(s) indicado(s)"
}

FLASH = 		'flash'
FLASH_ERROR = 	'error'
RANDOM_ERROR = 	u"Apenas testando a box de erro"