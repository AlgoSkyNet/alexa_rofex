"""
Alexa responses for the english version
"""


INIT_RESPONSE = {
    'session_attributes': {},
    'card_title': "Welcome to ROFEX skill",
    'card_output': "Which Rofex product do you want to consult?",
    'speech_output': "Welcome to Rofex Skill. Which Rofex product do you want to consult?",
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    'reprompt_text': "Sorry, I didn't get that, could you repeat it please.",
    'should_end_session': False
}
DEFAULT_RESPONSE = {
    'session_attributes': {},
    'card_title': "Default Response",
    'card_output': "Sorry, I didn't get that. Please repeat it.",
    'speech_output': "Sorry, I didn't get that. Please repeat it.",
    'reprompt_text': "Sorry, I didn't get that, could you repeat it please.",
    'should_end_session': False
}

END_RESPONSE = {
    'session_attributes': {},
    'card_title': "Bye Bye",
    'card_output': "Thank you! Have a nice day.",
    'speech_output': "Thank you! Have a nice day.",
    'reprompt_text': "Do you want to end the conversation?",
    'should_end_session': True
}

HELP_RESPONSE = {
    'session_attributes': {},
    'card_title': "Help!",
    'card_output': "Hi, you could ask me the price of a rofex product just saying the name of the product and the month of a valid position",
    'speech_output': "Hi, you could ask me the price of a rofex product just saying the name of the product and the month of a valid position",
    'reprompt_text': "Do you want to end the conversation? Just say goodbye.",
    'should_end_session': False
}

ERROR_RESPONSE = {
    'session_attributes': {},
    'card_title': "An Error Occurred",
    'card_output': "Sorry, I couldn't process your request. Please, try again.",
    'speech_output': "Sorry, an error has occurred and I couldn't process your request. "
                     "Please, try again.",
    'reprompt_text': "Sorry, I didn't get that, could you repeat it please.",
    'should_end_session': False
}

LAST_PRICE_RESPONSE = {
    'session_attributes': {},
    'card_title': "Rofex Price",
    'card_output': "",
    'speech_output': "",
    'reprompt_text': "",
    'should_end_session': False
}

LAST_PRICE_OK_RESPONSE = {
    'card_output': "Last price for {0} future {1} contract is {2}.",
    'speech_output': "Last price for {0} future {1} contract is {2}.",
    'reprompt_text': "Please ask me again."
}

SETTLE_PRICE_OK_RESPONSE = {
    'card_output': "There is no last price available for {0} future {1} contract, "
                   "although, the settlement price for this contract is {2}.",
    'speech_output': "There is no last price available for {0} future {1} contract, "
                     "although, the settlement price for this contract is {2}.",
    'reprompt_text': "Please ask me again."
}

LAST_PRICE_ERROR_RESPONSE = {
    'card_output': "Sorry, {0} is not a valid product. Please ask me again.",
    'speech_output': "Sorry, {0} is not a valid product. Please ask me again.",
    'reprompt_text': "Please ask me again later or try with another product."
}

LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE = {
    'card_output': "I could not find a valid contract for {0} future. Please try with another product.",
    'speech_output': "I could not find a valid contract for {0} future. Please try with another product.",
    'reprompt_text': "Please try with another product."
}

LAST_PRICE_MD_NOT_FOUND_RESPONSE = {
    'card_output': "Sorry, there have been no operations for this product yet. Please, ask me again later.",
    'speech_output': "Sorry, there have been no operations for this product yet. Please, ask me again later.",
    'reprompt_text': "Please ask me again later or try with another product."
}