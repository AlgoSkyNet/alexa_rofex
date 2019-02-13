# -*- coding: utf-8 -*-
"""
Alexa responses for the english version
"""
import config as conf

INIT_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Welcome to Rofex skill",
        'card_output': "Which Rofex instrument do you want to consult? "
                       "If you need help asking me questions just say 'HELP'",
        'speech_output': "<speak>Welcome to Rofex Skill. "
                         "<s>Which Rofex instrument do you want to consult?</s> "
                         "<s>If you need help asking me questions just say 'HELP'</s></speak>",
        'reprompt_text': "Sorry, I didn't get that, could you repeat it please.",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Bienvenidos al Skill de Rofex",
        'card_output': "¿Que instrumento deseas consultar? "
                       "Si necesitas ayuda solo dí la palabra 'AYUDA'",
        'speech_output': "<speak>Bienvenidos al Skill de Rofex. "
                         "<s>¿Que instrumento deseas consultar?</s> "
                         "<s>Si necesitas ayuda solo dí 'AYUDA'</s></speak>",
        'reprompt_text': "Perdón, no entendí, ¿Podrías repetirlo por favor?.",
        'should_end_session': False
    }
}

DEFAULT_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Default Response",
        'card_output': "Sorry, I didn't get that. Please repeat it.",
        'speech_output': "Sorry, I didn't get that. Please repeat it.",
        'reprompt_text': "Could you repeat it please.",
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

HELP_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Help!",
        'card_output': "If you want to know the last price of a Rofex future contract, "
                       "just tell me the instrument's name and, "
                       "optionally, the month of the contract. Also, "
                       "if you need the list of valid Rofex instruments, said the word "
                       "'Instruments' and I'll tell you. Want to try it?",
        'speech_output': "<speak>If you want to know the last price of Rofex future contract, "
                         "<s>just tell me the instrument's name</s>, "
                         "and optionally, the month of the contract. "
                         "<break time='1s'/><s>Also, if you need the list of valid Rofex instruments, "
                         "said the word 'Instruments' and I'll tell you.</s> "
                         "<break time='1s'/>Want to try it?</speak>",
        'reprompt_text': "Do you want to end the conversation? Just say goodbye.",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "AYUDA!",
        'card_output': "Si quieres saber el último precio de un futuro en Rofex solo tienes que "
                       "decirme el nombre del instrumento, y opcionalmente, "
                       "el mes del contrato. También te puedo decir los instrumentos que me puedes "
                       "consultar, solo dí la palabra 'Instrumento' y te ayudaré. "
                       "¿Quieres intentarlo?",
        'speech_output': "<speak>Si quieres saber el último precio de un futuro en Rofex, "
                         "<s>solo tienes que decirme el nombre del instrumento</s>, "
                         "y opcionalmente, el mes del contrato. "
                         "<break time='1s'/><s>También puedo decirirte los instrumentos que me puedes consultar, "
                         "solo dí la palabra 'Instrumentos' y te ayudaré.</s> "
                         "<break time='1s'/>¿Quieres intentarlo?</speak>",
        'reprompt_text': "¿Quieres finalizar la conversación? Solo dí 'Adiós Alexa'.",
        'should_end_session': False
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

LIST_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "List of valid Rofex Instruments",
        'card_output': "You can ask me for the following instruments: "
                       "Dollar: for dollar futures. "
                       "Rofex Index: for Rofex index futures. "
                       "Gold: for gold futures. "
                       "Oil: for oil futures. "
                       "Soy: for soy futures. "
                       "\nWant to try it?",
        'speech_output': "<speak>You can ask me for the following instruments: "
                         "<s>Dollar: for dollar futures.</s> "
                         "<s>Rofex Index: for Rofex index futures.</s> "
                         "<s>Gold: for gold futures.</s> "
                         "<s>Oil: for oil futures.</s> "
                         "<s>Soy: for soy futures.</s> "
                         "<break time='1s'/><s>Want to try it?</s></speak>",
        'reprompt_text': "Do you want to end the conversation? Just say goodbye.",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Instrumentos Rofex",
        'card_output': "Puede consultarme los siguientes instrumentos: "
                       "Dollar: para futuros de dollar. "
                       "Índice Rofex: para futuros sobre el índice Rofex. "
                       "Oro: para futuros de oro. "
                       "Petróleo: para futuros de petróleo. "
                       "Soja: para futuros sobre soja. "
                       "\n¿Quieres intentarlo?",
        'speech_output': "<speak>Puedes consultarme los siguientes instrumentos: "
                         "<s>Dólar: para futuros de dólar.</s> "
                         "<s>Índice Rofex: para futuros sobre el índice Rofex.</s> "
                         "<s>Oro: para futuros de oro.</s> "
                         "<s>Petróleo: para futuros de petróleo.</s> "
                         "<s>Soja: para futuros sobre soja. </s>"
                         "<break time='1s'/><s>¿Quieres intentarlo?</s></speak>",
        'reprompt_text': "¿Quieres finalizar la conversación? Solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

ERROR_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "An Error Occurred",
        'card_output': "Sorry, I couldn't process your request. Please, try again.",
        'speech_output': "<speak><s>Sorry, an error has occurred and I couldn't process your request.</s>"
                         "Please, ask me again.</speak>",
        'reprompt_text': "Do you want to end the conversation? Just say 'goodbye'.",
        'should_end_session': False
    },
    conf.Language.ES : {
        'session_attributes': {},
        'card_title': "Ocurrió un Error",
        'card_output': "Lo siento, no pude procesar tu consulta. Por favor, intentalo de nuevo.",
        'speech_output': "<speak><s>Lo siento, ocurrió un error y no pude procesar tu consulta.</s>"
                         "Por favor, intentalo de nuevo.</speak>",
        'reprompt_text': "¿Quieres finalizar la conversación? Solo dí 'Adiós Alexa'.",
        'should_end_session': False
    }
}

LAST_PRICE_RESPONSE = {
    conf.Language.EN : {
        'session_attributes': {},
        'card_title': "Rofex Price",
        'card_output': "",
        'speech_output': "",
        'reprompt_text': "",
        'should_end_session': False
    },
    conf.Language.ES: {
        'session_attributes': {},
        'card_title': "Precios Rofex",
        'card_output': "",
        'speech_output': "",
        'reprompt_text': "",
        'should_end_session': False
    }
}

LAST_PRICE_OK_RESPONSE = {
    conf.Language.EN : {
        'card_output': "Last price for {0} future {1} contract is {2}. "
                       "Can I help you with some other contract?",
        'speech_output': '<speak><s>Last price for {0} future {1} contract is {2}</s> '
                         '<break time="1s"/>Can I help you with some other contract?</speak>',
        'reprompt_text': "Do you want to end the conversation?"
    },
    conf.Language.ES: {
        'card_output': "El último precio para el futuro de {0} posición {1} es {2}. "
                       "¿Puedo ayudarte con otro contrato?",
        'speech_output': '<speak><s>El último precio para el futuro de {0} posición {1} es {2}.</s> '
                         '<break time="1s"/>¿Puedo ayudarte con otro contrato?</speak>',
        'reprompt_text': "¿Quieres finalizar la conversación? Solo dí 'Adiós Alexa'."
    }
}

SETTLE_PRICE_OK_RESPONSE = {
    conf.Language.EN : {
        'card_output': "There is no last price available for {0} future {1} contract, "
                       "although, the settlement price for this contract is {2}. "
                       "Can I help you with some other contract?",
        'speech_output': "<speak><s>There is no last price available for {0} future {1} contract, "
                         "although, the settlement price for this contract is {2}</s> "
                         "<break time='1s'/>Can I help you with some other contract?</speak>",
        'reprompt_text': "Please ask me again."
    },
    conf.Language.ES: {
        'card_output': "No hay último precio disponible para el futuro de {0} posición {1}."
                       "El precio de ajuste para ese contrato es {2}. "
                       "¿Quieres consultarme otro instrumento?",
        'speech_output': "<speak><s>No hay último precio disponible para el futuro de {0} posición {1}.</s> "
                         "<s>El precio de ajuste para ese contrato es {2}.</s> "
                         "<break time='1s'/>¿Quieres consultarme otro instrumento?</speak>",
        'reprompt_text': "¿Quieres finalizar la conversación? Solo dí 'Adiós Alexa'."
    }
}

LAST_PRICE_ERROR_RESPONSE = {
    conf.Language.EN : {
        'card_output': "Sorry, this is not a valid Rofex instrument. Please ask me again.",
        'speech_output': "<speak><s>Sorry, this is not a valid Rofex instrument.</s> Please, try with another instrument.</speak>",
        'reprompt_text': "Do you want to end the conversation? Just say goodbye"
    },
    conf.Language.ES: {
        'card_output': "Perdón, ese no es un instrumento Rofex válido. Por favor, intenta con otro instrumento.",
        'speech_output': "<speak><s>Perdón, ese no es un instrumento Rofex válido.</s> Por favor, intenta con otro instrumento.</speak>",
        'reprompt_text': "¿Quieres finalizar la conversación? Solo dí 'Adiós Alexa'."
    }
}

LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE = {
    conf.Language.EN : {
        'card_output': "I could not find a valid contract for {0} future {1} contract. "
                       "The most recent position for this instrument is {2}. "
                       "Please try again with this position.",
        'speech_output': "<speak><s>I could not find a valid contract for {0} future {1} contract.</s> "
                         "<s>The most recent position for this instrument is {2}</s>. "
                         "<s>Please try again with this position.</s></speak>",
        'reprompt_text': "Do you want to end the conversation? Just say goodbye"
    },
    conf.Language.ES: {
        'card_output': "El futuro de {0} no posee una posición abierta para el mes de {1}. "
                       "La posición más reciente para este instrumento es {2}. "
                       "Por favor, intenta de vuelta con dicha posición.",
        'speech_output': "<speak><s>El futuro de {0} no posee una posición abierta para el mes de {1}.</s> "
                         "<s>La posición más reciente para este instrumento es {2}.</s> "
                         "<s>Por favor, intenta de vuelta con dicha posición.</s></speak>",
        'reprompt_text': "¿Quieres finalizar la conversación? Solo dí 'Adiós Alexa'."
    }
}

LAST_PRICE_MD_NOT_FOUND_RESPONSE = {
    conf.Language.EN : {
        'card_output': "Sorry, there have been no operations for this instrument yet. "
                       "Please, ask me again later.",
        'speech_output': "<speak>Sorry, there have been no operations for this instrument yet. "
                         "Please, ask me again later.</speak>",
        'reprompt_text': "Do you want to end the conversation? Just say goodbye"
    },
    conf.Language.ES: {
        'card_output': "Perdón, no hay datos disponible para este futuro todavía. "
                       "¿Quieres consultarme otro instrumento?",
        'speech_output': "<speak><s>Perdón, no hay datos disponible para este futuro todavía.</s> "
                         "¿Quieres consultarme otro instrumento?</speak>",
        'reprompt_text': "¿Quieres finalizar la conversación? Solo dí 'Adiós Alexa'."
    }
}