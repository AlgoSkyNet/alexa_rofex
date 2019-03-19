# -*- coding: utf-8 -*-
"""
Alexa responses for the english version
"""
import config as conf

INIT_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Welcome to ROFEX Skill",
        'card_output': "Please, tell me an instrument and I'll give you the last price "
                       "available for the contract. "
                       "If you need help asking me questions just say 'HELP'",
        'speech_output': "<speak>Welcome to ROFEX Skill. "
                         "<s>Please, tell me an instrument and I'll give you the last price "
                         "available for the contract.</s> "
                         "<s>If you need help just say 'HELP'</s></speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Bienvenido al Skill de ROFEX",
        'card_output': "Por favor, dime un instrumento y te diré el último precio disponible para ese contrato. "
                       "Si necesitas ayuda solo dí la palabra 'AYUDA'",
        'speech_output': "<speak>Bienvenido al Skill de ROFEX. "
                         "<s>Por favor, dime un instrumento y te diré el último precio disponible para ese contrato.</s> "
                         "<s>Si necesitas ayuda solo dí 'AYUDA'.</s></speak>",
        'reprompt_text': "Si deseas terminar la conversación solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

DEFAULT_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Default Response",
        'card_output': "Sorry, I didn't get that. Please repeat it.",
        'speech_output': "Sorry, I didn't get that. Please repeat it.",
        'reprompt_text': "Could you repeat it please?",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Respuesta Genérica",
        'card_output': "Perdón, no entendí lo que dijiste. ¿Podrías repetirlo por favor?",
        'speech_output': "Perdón, no entendí lo que dijiste. ¿Podrías repetirlo por favor?",
        'reprompt_text': "¿Podrías repetirlo por favor?",
        'should_end_session': False
    }
}

ASK_INSTRUMENT_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Tell me the Instrument",
        'card_output': "Please, tell me the instrument you want to know.",
        'speech_output': "<speak>Please, tell me the instrument you want to know.</speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'.",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Hasta luego",
        'card_output': "Por favor, dime el instrumento que desas saber.",
        'speech_output': "<speak>Por favor, dime el instrumento que deseas saber.</speak>",
        'reprompt_text': "Si deseas terminar la conversación solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

END_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Bye Bye",
        'card_output': "Thank you! Have a nice day.",
        'speech_output': "Thank you! Have a nice day.",
        'reprompt_text': "",
        'should_end_session': True
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Hasta luego",
        'card_output': "Gracias! Que tengas un lindo día.",
        'speech_output': "Gracias! Que tengas un lindo día.",
        'reprompt_text': "",
        'should_end_session': True
    }
}

LANGUAGE_NOT_SUPPORTED = {
    'session_attributes': {},
    'card_title': "Language Not Supported",
    'card_output': "Sorry, I do not recognize this language: {0}.",
    'speech_output': "<speak>Sorry, I don't recognize this language: {0}.</speak>",
    'reprompt_text': "",
    'should_end_session': True
}

ERROR_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "An Error Occurred",
        'card_output': "Sorry, I couldn't process your request. Please, try again.",
        'speech_output': "<speak><s>Sorry, an error has occurred and I couldn't process your request.</s> "
                         "Please, ask me again.</speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Ocurrió un Error",
        'card_output': "Lo siento, no pude procesar tu consulta. Por favor, inténtalo de nuevo.",
        'speech_output': "<speak><s>Lo siento, ocurrió un error y no pude procesar tu consulta.</s> "
                         "Por favor, inténtalo de nuevo.</speak>",
        'reprompt_text': "Si quieres terminar la conversación solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

LAST_PRICE_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "ROFEX Price",
        'card_output': "",
        'speech_output': "",
        'reprompt_text': "",
        'should_end_session': False
    },
    conf.Language.ES: {
        'session_attributes': {},
        'card_title': "Precios ROFEX",
        'card_output': "",
        'speech_output': "",
        'reprompt_text': "",
        'should_end_session': False
    }
}

LAST_PRICE_OK_RESPONSE = {
    conf.Language.EN : {
        'card_output': "The price for {0} future {1} contract is {2}. "
                       "Can I help you with another instrument?",
        'speech_output': '<speak><s>The price for {0} future {1} contract is {2}.</s> '
                         '<break time="1s"/>Can I help you with another instrument?</speak>',
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'"
    },
    conf.Language.ES: {
        'card_output': "El precio para el futuro de {0} posición {1} es {2}. "
                       "¿Puedo ayudarte con otro instrumento?",
        'speech_output': '<speak><s>El precio para el futuro de {0} posición {1} es {2}.</s> '
                         '<break time="1s"/>¿Puedo ayudarte con otro instrumento?</speak>',
        'reprompt_text': "Si deseas terminar la conversación solo dí 'Adiós Alexa'."
    }
}

LAST_PRICE_OK_RESPONSE_SPOT = {
    conf.Language.EN : {
        'card_output': "Last price for {0} is {1}. "
                       "Can I help you with another instrument?",
        'speech_output': "<speak><s>Last price for {0} is {1}.</s> "
                         "<break time='1s'/>Can I help you with another instrument?</speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'"
    },
    conf.Language.ES: {
        'card_output': "El último precio para el {0} es {1}. "
                       "¿Quieres consultarme otro instrumento?",
        'speech_output': "<speak><s>El último precio para el {0} es {1}.</s> "
                         "<break time='1s'/>¿Quieres consultarme otro instrumento?</speak>",
        'reprompt_text': "Si deseas terminar la conversación solo dí 'Adiós Alexa'."
    }
}

ENTRY_PRICE_OK_RESPONSE = {
    conf.Language.EN : {
        'card_output': "{0} for {1} future {2} contract is {3}. Want to try it again?",
        'speech_output': "<speak><s>{0} for {1} future {2} contract is {3}.</s> "
                         "<break time='1s'/>Can I help you with another instrument?</speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'"
    },
    conf.Language.ES: {
        'card_output': "El {0} para el futuro de {1} posición {2} es {3}. "
                       "¿Quieres consultarme otro instrumento?",
        'speech_output': "<speak><s>El {0} para el futuro de {1} posición {2} es {3}.</s> "
                         "<break time='1s'/>¿Quieres consultarme otro instrumento?</speak>",
        'reprompt_text': "Si deseas terminar la conversación solo dí 'Adiós Alexa'."
    }
}

LAST_PRICE_ERROR_RESPONSE = {
    conf.Language.EN : {
        'card_output': "Sorry, this is not a valid instrument. Please ask me again.",
        'speech_output': "<speak><s>Sorry, this is not a valid instrument.</s> Please, try with another instrument.</speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'"
    },
    conf.Language.ES: {
        'card_output': "Perdón, ese no es un instrumento válido. Por favor, intenta con otro instrumento.",
        'speech_output': "<speak><s>Perdón, ese no es un instrumento válido.</s> Por favor, intenta con otro instrumento.</speak>",
        'reprompt_text': "Si quieres terminar la conversación solo dí 'Adiós Alexa'."
    }
}

LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE = {
    conf.Language.EN : {
        'card_output': "I could not find a valid instrument for {0} future {1} contract. "
                       "The most recent position for this instrument is {2}. "
                       "Please try again with this position.",
        'speech_output': "<speak><s>I could not find a valid instrument for {0} future {1} contract.</s> "
                         "<s>The most recent position for this instrument is {2}</s>. "
                         "<s>Please try again with this position.</s></speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'"
    },
    conf.Language.ES: {
        'card_output': "El futuro de {0} no posee una posición abierta para el mes de {1}. "
                       "La posición más reciente para este instrumento es {2}. "
                       "Por favor, intenta de vuelta con dicha posición.",
        'speech_output': "<speak><s>El futuro de {0} no posee una posición abierta para el mes de {1}.</s> "
                         "<s>La posición más reciente para este instrumento es {2}.</s> "
                         "<s>Por favor, intenta de vuelta con dicha posición.</s></speak>",
        'reprompt_text': "Si quieres terminar la conversación solo dí 'Adiós Alexa'."
    }
}


LAST_PRICE_MD_NOT_FOUND_RESPONSE = {
    conf.Language.EN : {
        'card_output': "Sorry, there are no data available for {0} future {1} contract. "
                       "Please, try again with another instrument.",
        'speech_output': "<speak>Sorry, there are no data available for {0} future {1} contract. "
                         "Please, try again with another instrument.</speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'"
    },
    conf.Language.ES: {
        'card_output': "Perdón, en estos momentos no hay datos disponible para el futuro de {0} posición {1}. "
                       "¿Quieres consultarme otro instrumento?",
        'speech_output': "<speak><s>Perdón, no hay datos disponible para este futuro todavía.</s> "
                         "¿Quieres consultarme otro instrumento?</speak>",
        'reprompt_text': "Si quieres terminar la conversación solo dí 'Adiós Alexa'."
    }
}

ENTRY_PRICE_MD_NOT_FOUND_RESPONSE = {
    conf.Language.EN : {
        'card_output': "Sorry, {0} is not available for this instrument now. "
                       "Please, try again with another data or instrument.",
        'speech_output': "<speak><s>Sorry, {0} is not available for this instrument now.</s> "
                         "<s>Please, try again with another data or instrument.</s></speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'"
    },
    conf.Language.ES: {
        'card_output': "Perdón, en este momento no hay {0} disponible para este instrumento. "
                       "Por favor, intentalo de nuevo con otro dato o instrumento.",
        'speech_output': "<speak><s>Perdón, en este momento no hay {0} disponible para este instrumento.</s> "
                         "<s>Por favor, intentalo de nuevo con otro dato o instrumento.</s></speak>",
        'reprompt_text': "Si quieres terminar la conversación solo dí 'Adiós Alexa'."
    }
}




###############################################################################################
###############################################################################################

# 1 - Help Possibilities
HELP_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Help!",
        'card_output': "If you want to know how to ask the price of an instrument, "
                       "say 'Question' and I'll help you. "
                       "Also, I can tell you the list of valid instruments, just say 'Instruments', "
                       "and to know the list of available data of an "
                       "instruments, say 'Instruments Data'. Want to try it?",
        'speech_output': "<speak>If you want to know how to ask the price of an instrument, say "
                         "<s><prosody volume='x-loud'>'Question'</prosody></s> "
                         "and I'll help you. Also, I can tell you the list of valid instruments, just say "
                         "<s><prosody volume='x-loud'>'Instruments'</prosody></s>, "
                         "and to know the list of available data of an instrument, say "
                         "<s><prosody volume='x-loud'>'Instruments Data'</prosody></s>. "
                         "<break time='1s'/>Want to try it?</speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "AYUDA!",
        'card_output': "Si quieres saber como preguntarme el precio de un instrumento, "
                       "dime 'Preguntar' y te ayudaré. "
                       "También te puedo decir la lista de instrumentos válidos, "
                       "solo dí 'Instrumentos', "
                       "y para conocer la lista de datos disponibles sobre "
                       "un instrumento, dí 'Datos Instrumentos'. "
                       "¿Quieres intentarlo?",
        'speech_output': "<speak>Si quieres saber como preguntarme el precio de un instrumento, dime "
                         "<s><prosody volume='x-loud'>'Preguntar'</prosody></s>"
                         " y te ayudaré. También te puedo decir la lista de instrumentos válidos, solo dí "
                         "<s><prosody volume='x-loud'>'Instrumentos'</prosody></s>"
                         ", y para conocer la lista de datos disponibles sobre un instrumento, dí "
                         "<s><prosody volume='x-loud'>'Datos Instrumentos'</prosody></s>. "
                         "<break time='1s'/>¿Quieres intentarlo?</speak>",
        'reprompt_text': "Si deseas terminar la conversación solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

# 1.1 - Question Response
QUESTION_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "How to ask me?",
        'card_output': "To know the price of an instrument just tell me "
                       "the instrument's name and, optionally, "
                       "the month of the contract. Additionally, "
                       "you could specify the market data you want to know. "
                       "Want to try it?",
        'speech_output': "<speak><s>To know the price of an instrument just tell me "
                         "the instrument's name and, optionally, "
                         "the month of the contract.</s> <s>Additionally, "
                         "you could specify the market data you want to know.</s> "
                         "<break time='1s'/>Want to try it?</speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Como preguntar?",
        'card_output': "Para saber el precio de un instrumento solo tienes que "
                       "decirme el nombre del instrumento y, opcionalmente, "
                       "el mes del contrato. Adicionalmente, puedes especificar "
                       "el dato de mercado que deseas saber. "
                       "¿Quieres intentarlo?",
        'speech_output': "<speak><s>Para saber el precio de un instrumento solo tienes que "
                         "decirme el nombre del instrumento y, opcionalmente, "
                         "el mes del contrato.</s> <s>Adicionalmente, puedes especificar "
                         "el dato de mercado que deseas saber.</s> "
                         "<break time='1s'/>¿Quieres intentarlo?</speak>",
        'reprompt_text': "Si deseas terminar la conversación solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

# 1.2 - Instruments List Response
INSTRUMENT_LIST_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Instruments List",
        'card_output': "You can ask me for the following instruments: "
                       "Dollar: for dollar futures. "
                       "ROFEX Index: for ROFEX 20 Index futures. "
                       "Gold: for gold futures. "
                       "Oil: for oil futures. "
                       "Soybean: for soybean futures. "
                       "Corn: for corn futures. "
                       "Wheat: for wheat futures. "
                       "If you want more details about any instrument "
                       "just say 'Help' and the name of the instrument. "
                       "Want to try it?",
        'speech_output': "<speak><s>You can ask me for the following instruments:</s> "
                         "<s><prosody volume='x-loud'>Dollar</prosody>: for dollar futures.</s> "
                         "<s><prosody volume='x-loud'>ROFEX Index</prosody>: for ROFEX 20 Index futures.</s> "
                         "<s><prosody volume='x-loud'>Gold</prosody>: for gold futures.</s> "
                         "<s><prosody volume='x-loud'>Oil</prosody>: for oil futures.</s> "
                         "<s><prosody volume='x-loud'>Soybean</prosody>: for soybean futures.</s> "
                         "<s><prosody volume='x-loud'>Corn</prosody>: for corn futures.</s> "
                         "<s><prosody volume='x-loud'>Wheat</prosody>: for wheat futures.</s> "
                         "<s>If you want more details about any instrument "
                         "just say <s><prosody volume='x-loud'>'Help'</prosody></s> and the name of the instrument.</s> "
                         "<break time='1s'/><s>Want to try it?</s></speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Lista Instrumentos",
        'card_output': "Puedes consultarme los siguientes instrumentos: "
                       "Dólar: para futuros de dólar. "
                       "Índice ROFEX: para futuros sobre el Índice ROFEX 20. "
                       "Oro: para futuros de oro. "
                       "Petróleo: para futuros de petróleo. "
                       "Soja: para futuros de soja. "
                       "Maíz: para futuros de maíz. "
                       "Trigo: para futuros de trigo. "
                       "Si quieres saber más detalles acerca de algún instrumento "
                       "solo dí 'Ayuda' y el nombre del instrumento. "
                       "¿Quieres intentarlo?",
        'speech_output': "<speak>Puedes consultarme los siguientes instrumentos: "
                         "<s><prosody volume='x-loud'>Dólar</prosody>: para futuros de dólar.</s> "
                         "<s><prosody volume='x-loud'>Índice ROFEX</prosody>: para futuros sobre el Índice ROFEX 20.</s> "
                         "<s><prosody volume='x-loud'>Oro</prosody>: para futuros de oro.</s> "
                         "<s><prosody volume='x-loud'>Petróleo</prosody>: para futuros de petróleo.</s> "
                         "<s><prosody volume='x-loud'>Soja</prosody>: para futuros de soja.</s> "
                         "<s><prosody volume='x-loud'>Maíz</prosody>: para futuros de maíz.</s> "
                         "<s><prosody volume='x-loud'>Trigo</prosody>: para futuros de trigo.</s> "
                         "<s>Si quieres saber más detalles acerca de algún instrumento "
                         "solo dí <prosody volume='x-loud'>'Ayuda'</prosody> y el nombre del instrumento.</s> "
                         "<break time='1s'/><s>¿Quieres intentarlo?</s></speak>",
        'reprompt_text': "Si quieres terminar la conversación solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

# 1.2.1 - Instruments Detailed Response
HELP_RELATED_INST_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Instrument Detail",
        'card_output': "Ok, when you mention the instrument '{0}', I will tell you "
                       "the last price available for the contract. "
                       "Also, let me tell you that there are other {0} "
                       "related instruments, like: {1}. "
                       "Just tell me the instrument full name and I will tell you the price. "
                       "Want to try it?",
        'speech_output': "<speak><s>Ok, when you mention the instrument <prosody volume='x-loud'>'{0}'</prosody>, "
                         "I will tell you the last price available for the contract.</s> "
                         "<s>Also, let me tell you that there are other {0} "
                         "related instruments, like:</s> {1}. "
                         "<s>Just tell me the instrument full name and I will tell you the price.</s> "
                         "<break time='1s'/><s>Want to try it?</s></speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Detalle Instrumento",
        'card_output': "Bien, cuando menciones el instrumento '{0}' te diré el "
                       "último percio disponible para ese contrato. "
                       "También puedes consultar otros instrumentos relacionados con {0} como: {1}. "
                       "Solo dí el nombre del instrumento completo y te diré el precio. "
                       "¿Quieres intentarlo?",
        'speech_output': "<speak><s>Bien, cuando menciones el instrumento <prosody volume='x-loud'>'{0}'</prosody> "
                         "te diré el último percio disponible para ese contrato.</s> "
                         "<s>También puedes consultar otros instrumentos relacionados con {0} como:</s> {1}. "
                         "<s>Solo dí el nombre del instrumento completo y te diré el precio.</s> "
                         "<break time='1s'/><s>¿Quieres intentarlo?</s></speak>",
        'reprompt_text': "Si quieres terminar la conversación solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

# 1.2.2 - Instruments Detailed Response Default
HELP_INSTRUMENT_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Instrument Detail",
        'card_output': "Ok, when you mention the instrument '{0}', I will tell you "
                       "the last price available for the contract. For example, to know the "
                       "price of {0} future June contract, just say '{0} June'. "
                       "Want to try it?",
        'speech_output': "<speak><s>Ok, when you mention the instrument <prosody volume='x-loud'>'{0}'</prosody>, "
                         "I will tell you the last price available for the contract.</s> <s>For example, to know the "
                         "price of {0} future June contract, just say <prosody volume='x-loud'>'{0} June'</prosody>.</s> "
                         "<break time='1s'/><s>Want to try it?</s></speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Detalle Instrumento",
        'card_output': "Bien, cuando menciones el instrumento '{0}' te diré el "
                       "último percio disponible para ese contrato. Por ejemplo, para saber "
                       "el precio del futuro sobre {0} posición Junio, "
                       "solo tienes que decir '{0} Junio'. ¿Quieres intentarlo?",
        'speech_output': "<speak><s>Bien, cuando menciones el instrumento <prosody volume='x-loud'>'{0}'</prosody>"
                         " te diré el último percio disponible para ese contrato.</s> <s>Por ejemplo, para saber "
                         "el precio del futuro sobre {0} posición Junio, solo tienes que decir "
                         "<prosody volume='x-loud'>'{0} Junio'</prosody>.</s>"
                         "<break time='1s'/><s>¿Quieres intentarlo?</s></speak>",
        'reprompt_text': "Si quieres terminar la conversación solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

# 1.3 - Market Data List
ENTRY_LIST_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Market Data List",
        'card_output': "When asking for an instrument you could also "
                       "specify the market data you want to know about. "
                       "Now, the available data are: "
                       "Last Price, Settlement Price, Effective Volume, "
                       "Nominal Volume and Open Interest. "
                       "Want to try it?",
        'speech_output': "<speak><s>When asking for an instrument you could also "
                         "specify the market data you want to know about.</s> "
                         "<s>Now, the available data are:</s> "
                         "<prosody volume='x-loud'>Last Price</prosody>, "
                         "<prosody volume='x-loud'>Settlement Price</prosody>, "
                         "<prosody volume='x-loud'>Effective Volume</prosody>, "
                         "<prosody volume='x-loud'>Nominal Volume</prosody> and "
                         "<prosody volume='x-loud'>Open Interest</prosody>. "
                         "<break time='1s'/><s>Want to try it?</s></speak>",
        'reprompt_text': "If you want to end the conversation just say 'Goodbye'",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Lista Datos de Mercado",
        'card_output': "Al consultar un instrumento también puedes especificar "
                       "el dato de mercado que deseas saber. "
                       "Por ahora, los datos disponibles son: "
                       "Último Precio, Precio de Ajuste, Volumen Efectivo, "
                       "Volumen Nominal e Interés Abierto. "
                       "¿Quieres intentarlo?",
        'speech_output': "<speak><s>Al consultar un instrumento también puedes especificar "
                         "el dato de mercado que deseas saber.</s> "
                         "<s>Por ahora, los datos disponibles son:</s> "
                         "<prosody volume='x-loud'>Último Precio</prosody>, "
                         "<prosody volume='x-loud'>Precio de Ajuste</prosody>, "
                         "<prosody volume='x-loud'>Volumen Efectivo</prosody>, "
                         "<prosody volume='x-loud'>Volumen Nominal</prosody> e "
                         "<prosody volume='x-loud'>Interés Abierto</prosody>. "
                         "<break time='1s'/><s>¿Quieres intentarlo?</s></speak>",
        'reprompt_text': "Si quieres terminar la conversación solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}



