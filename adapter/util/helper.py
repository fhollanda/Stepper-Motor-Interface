# encoding: utf-8

ERROR = {
	'REQUEST_EXCEPTION': u"Ocorreu um erro na conexão com o servidor, verifique os cabos ou o funcionamento dos equipamentos (err: x001)",
	'MOTOR_EXCEPTION': u"Ocorreu um erro na conexão com o motor. (err: x002)",
	'SCOPE_EXCEPTION': u"Ocorreu um erro na conexão com o osciloscópio. (err: x003)",
	'GENERIC_REQUEST_EXCEPTION': u"Há alguma falha no funcionamento do adaptador. Verifique os logs (err: x004)",
	'CREATE_FILE_EXCEPTION': u"Por algum motivo o arquivo não pôde ser criado. Verifique os logs (err: x005)",
	'GENERIC_HTTP_ERROR': u"Ocorreu um erro: {}",
	'UNAVAILABLE_SERVICE': u"Algum dos serviços necessários se encontra indisponível, verifique os logs para descobrir a causa (err: x503)",
	'NOT_FOUND': u"O recurso ou serviço procurado não foi encontrado (err: x404)",
	'UNPROCESSABLE_ENTITY': u"Não foi possível processar essa requisição. Consulte o manual e refaça a operação (err: x422)"
}

REQUIRED_FIELD = u"O campo {} deve ser preenchido"

MOVE = {
	'motor_number': REQUIRED_FIELD.format(u"que informa o número do motor").encode('utf-8'),
	'direction': REQUIRED_FIELD.format(u"direção").encode('utf-8'),
	'steps': REQUIRED_FIELD.format(u"passos"),
	'acquisition_rate': REQUIRED_FIELD.format(u"informando a quantidade de passos por pontos"),
	'primary_axis': REQUIRED_FIELD.format(u"que informa o eixo principal"),
	'secondary_axis': REQUIRED_FIELD.format(u"que informa o eixo secundário").encode('utf-8'),
	'acquisition_offset_rate': REQUIRED_FIELD.format(u"com o deslocamento do eixo secundário").encode('utf-8'),
	'secondary_axis_step_size': REQUIRED_FIELD.format(u"com o tamanho do deslocamento").encode('utf-8')
}

FIELDS = u"Houve um erro com os campos necessários para realizar essa requisição" 

ABORT_FLAG = u"O programa foi abortado pelo usuário"

DEFAULT_CAPTURE_NAME = u"Unnamed"