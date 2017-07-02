# encoding: utf-8

TITLE = {
	'CALIPER':	u"Calibrar motor",
	'CAPTURES': u"Capturas salvas",
	'COPYRIGHT':	u"Informações de Copyright",
	'MOVE':		u"Realizar varredura",
	'MOVE1D': u"Varredura com uma dimensão",
	'MOVE2D': u"Varredura com duas dimensões",
	'MOVE3D': u"Varredura com três dimensões",
	'HELP': u"Ajuda - "
}

HELP = {
	'CALIPER':	u"Aqui deveria ficar o texto explicando como deve funcionar a calibragem",
	'CAPTURES': u"Aqui deveria ficar o texto explicando como deve funcionar a tela com as capturas salvas",
	'MOVE':	u"Aqui deveria ficar o texto explicando como deve funcionar a varredura, com divisão para 1, 2 ou 3 eixos"
}

MENU = {
	'ABORT': u"ABORTAR",
	'CALIPER':	u"CALIBRAR",
	'CAPTURES': u"CAPTURAS SALVAS",
	'CONFIG':	u"CONFIGURAÇÕES",
	'COPYRIGHT':	u"COPYRIGHT",
	'MOVE': u"VARREDURA",
		'MOVE_1D': u"VARREDURA 1D",
		'MOVE_2D': u"VARREDURA 2D",
		'MOVE_3D': u"VARREDURA 3D",
	'HELP':	u"AJUDA"
}

FIELDS = {
	#SCAN FIELDS
	'SCAN_NAME': u'Nome da captura',
	'SCAN_NAME_INFO': u"Se não for dado um nome a essa captura, ela será nomeada \"Unnamed\" e poderá ser identificada pelo seu uuid (identificador único)",
	'SCAN_LEGEND': u'Dados da varredura a ser realizada',
	'AXIS': u'Eixo primário',
		'X': u'Eixo X',
		'Y': u'Eixo Y',
		'Z': u'Eixo Z',
	'DIRECTION': u'Direção',
		'FORWARD': u'Para frente',
		'REVERSE': u'Para trás',
	'DIRECTION_INFO': u"A direção é relativa a posição do equipamento",
	'STEPS': u'Passos',
	'ACQUISTION_RATE': u'Taxa de aquisição',
	'ACQUISTION_RATE_INFO': u'Quantidade de passos necessários para realizar cada captura',
	'SECONDARY_AXIS': u'Eixo secundário',
	'TOTAL_STEPS_SECONDARY': u'Quant. total de passos deslocamento',
	'TOTAL_STEPS_SECONDARY_INFO': u'Tamanho total do deslocamento no eixo secundário',
	'SIZE_STEPS_SECONDARY': u'Quant. passos por deslocamento',
	'SIZE_STEPS_SECONDARY_INFO': u'Tamanho do deslocamento no eixo secundário a cada iteração',
	'SCAN_BUTTON': u'Realizar varredura',

	#SCOPE CONFIG FIELDS
	'CONFIG_SCOPE_LEGEND': u'Configurações do osciloscópio',
	'CONFIG_INFO': u'Se nenhum dos campos for modificado, o local de captura no ecrã do osciloscópio permanecerá sem alterações ao se realizar uma varredura',
	'CHANNEL': u'Canal para aquisição',
	'FREQUENCY': u'Frequência',
	'CYCLES': u'Quantidade de ciclos',
	'AVERAGING': u'Quantidade de médias',
	'V_SCALE': u'Escala de voltagem',
	'T_SCALE': u'Escala de tempo',
	'SET_CONFIG_BUTTON': u'Enviar configurações',

	#CAPTURES
	'DATE_CREATED': u'Captura realizada em: ',
	'REMOVE': u'Remover'
}

ERROR = {
	'REQUEST_EXCEPTION': u"Ocorreu algum erro na conexão: {0}",
	'EXCEPTION': u"Ocorreu um erro que a aplicação não pôde tratar normalmente. <br/> Existe a possibilidade de algum serviço estar fora do ar. <br/> Verifique os cabos de conexão, os logs das aplicações e tente novamente<br/> HTTP Status: 500. <br/> <strong>Motivo do erro:</strong> <br/> {0}",
	'SCAN_EXCEPTION': u"Ocorreu um erro durante a varredura, verifique os logs das demais aplicações para descobrir a causa",
	'SET_CONFIG_EXCEPTION': u"Ocorreu um erro na hora de enviar os parâmetros para o osciloscópio",
	'DELETE_CAPTURE_EXCEPTION': u"Ocorreu um erro ao deletar o arquivo <{}>",
	'REQUIRED_FIELD': u"Por favor, preencha o(s) campo(s) indicado(s):"
}

FLASH = 		'flash'
FLASH_ERROR = 	'error'
RANDOM_ERROR = 	u"Apenas testando a box de erro"
SET_CONFIG_OK = u"Configurações enviadas com sucesso para o osciloscópio"
SCAN_OK = u"A captura \"{0}\" relativa ao arquivo <{1}> já está disponível na aba de capturas salvas"
ABORT_OK = u"Foi enviado o comando para abortar a operação e o status retornado foi <strong>{0}</strong>, aperte o botão de retornar no navegador para recomeçar o procedimento"
DELETE_CAPTURE_OK = u"Arquivo com identificador único <{}> apagado"