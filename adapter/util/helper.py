# encoding: utf-8

ERROR = {
	'REQUEST_EXCEPTION': u"Ocorreu um erro na conexão com o servidor. Tente novamente ou verifique o funcionamento do motor (err: x001)",
	'GENERIC_REQUEST_EXCEPTION': u"Há alguma falha no funcionamento do adaptador. Verifique os logs (err: x002)",
	'GENERIC_HTTP_ERROR': u"Ocorreu um erro: {}",
	'UNAVAILABLE_SERVICE': u"O serviço se encontra indisponível, tente novamente mais tarde (err: x503)",
	'NOT_FOUND': u"O recurso ou serviço procurado não foi encontrado (err: x404)",
	'UNPROCESSABLE_ENTITY': u"Não foi possível processar essa requisição. Consulte o manual e refaça a operação (err: x422)"
}

REQUIRED_FIELD = u"O campo {} deve ser preenchido"

MOVE = {
	'motor_number': REQUIRED_FIELD.format(u"que informa o número do motor").encode('utf-8'),
	'direction': REQUIRED_FIELD.format(u"direção").encode('utf-8'),
	'steps': REQUIRED_FIELD.format(u"passos"),
	'acquisition_rate': REQUIRED_FIELD.format(u"informando a quantidade de passos por pontos")
}