# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from bisect import bisect_left

from alexa_handlers.AlexaBaseHandler import AlexaBaseHandler
import configuration.config as config
import connector_pmy_api.pmy_rest_api as api
import configuration.alexa_responses as responses


class AlexaForRFXHandler(AlexaBaseHandler):
    """
    Concrete implementation of the AlexaBaseHandler for the ROFEX Skill.
    """

    def __init__(self):
        super(self.__class__, self).__init__()
        self.restClient = api.RestClient(config.PrimaryAPI.USER, config.PrimaryAPI.PASS, config.PrimaryAPI.ENVIRONMENT)
        is_login = self.restClient.login()

    def on_session_started(self, session_started_request, session):
        logging.debug("In on_session_started.")
        logging.debug("on_intent requestId=" + session_started_request['requestId'] +
                         ", sessionId=" + session['sessionId'])

    def on_launch(self, launch_request, session, lan):
        logging.debug("In on_launch.")
        return AlexaForRFXHandler._init_response(lan)

    def on_language_not_supported(self, lan):
        logging.debug("In on_language_not_supported.")
        return AlexaForRFXHandler._language_not_supported_response(lan)

    def on_session_ended(self, session_end_request, session, lan):
        logging.debug("In on_session_ended.")
        return AlexaForRFXHandler._end_response(lan)

    def on_processing_error(self, event, context, exc, lan):
        logging.error("In on_processing_error: " + str(exc))
        return AlexaForRFXHandler._error_response(lan)

    def on_inst_data_intent(self, lan):
        logging.debug("In on_inst_data_intent.")
        return AlexaForRFXHandler._inst_data_response(lan)

    def on_question_intent(self, lan):
        logging.debug("In on_question_intent.")
        return AlexaForRFXHandler._question_response(lan)

    def on_help_intent(self, intent, session, lan):
        logging.debug("In on_help_intent.")
        return self._help_response(intent, lan)

    def on_intent(self, intent_request, session, lan):
        """ Called when the user specifies an intent for this skill """

        logging.debug("on_intent requestId=" + intent_request['requestId'] +
                     ", sessionId=" + session['sessionId'])

        intent = intent_request['intent']
        intent_name = intent_request['intent']['name']

        # Dispatch to your skill's intent handlers

        # Custom Intents
        if intent_name == "LastPriceIntent":
            return self._last_price_response(intent, lan)
        if intent_name == "ProductListIntent":
            return self._product_list_response(lan)
        if intent_name == "CloseIntent":
            return self.on_session_ended(intent, session, lan)
        if intent_name == "HelpIntent":
            return self.on_help_intent(intent, session, lan)
        if intent_name == "InstrumentDataIntent":
            return self.on_inst_data_intent(lan)
        if intent_name == "QuestionIntent":
            return self.on_question_intent(lan)

        # Amazon Default Intents
        if intent_name == "YesNoIntent":
            return self._yes_no_response(intent, lan)
        if intent_name == "AMAZON.FallbackIntent":
            return self._default_response(lan)

        return self._default_response(lan)

    @staticmethod
    def _language_not_supported_response(lan):
        return AlexaBaseHandler._build_response(responses.LANGUAGE_NOT_SUPPORTED.format(lan))

    @staticmethod
    def _default_response(lan):
        return AlexaForRFXHandler._build_response(responses.DEFAULT_RESPONSE[lan])

    @staticmethod
    def _init_response(lan):
        return AlexaForRFXHandler._build_response(responses.INIT_RESPONSE[lan], True)

    @staticmethod
    def _end_response(lan):
        return AlexaForRFXHandler._build_response(responses.END_RESPONSE[lan])

    @staticmethod
    def _error_response(lan):
        return AlexaForRFXHandler._build_response(responses.ERROR_RESPONSE[lan], True)

    @staticmethod
    def _product_list_response(lan):
        return AlexaForRFXHandler._build_response(responses.INSTRUMENT_LIST_RESPONSE[lan], True)

    @staticmethod
    def _ask_instrument_response(lan):
        return AlexaForRFXHandler._build_response(responses.ASK_INSTRUMENT_RESPONSE[lan], True)

    def _help_response(self, intent, lan):
        if AlexaForRFXHandler.keys_exists(intent, 'slots', 'Product', 'resolutions',
                                          'resolutionsPerAuthority', 0, 'values', 0, 'value', 'id'):
            product_id = intent['slots']['Product']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
            if 'related' in config.Instrument[product_id]:
                related = []
                for related_inst in config.Instrument[product_id]['related']:
                    related.append(config.Instrument[related_inst]['name'][lan])
                response = responses.HELP_RELATED_INST_RESPONSE[lan]
                response['card_output'] = responses.HELP_RELATED_INST_RESPONSE[lan]['card_output'].format(config.Instrument[product_id]['name'][lan], ', '.join(related))
                response['speech_output'] = responses.HELP_RELATED_INST_RESPONSE[lan]['speech_output'].format(config.Instrument[product_id]['name'][lan], ', '.join(related))
            else:
                response = responses.HELP_INSTRUMENT_RESPONSE[lan]
                response['card_output'] = responses.HELP_INSTRUMENT_RESPONSE[lan]['card_output'].format(config.Instrument[product_id]['name'][lan])
                response['speech_output'] = responses.HELP_INSTRUMENT_RESPONSE[lan]['speech_output'].format(config.Instrument[product_id]['name'][lan])
        else:
            response = responses.HELP_RESPONSE[lan]

        return AlexaBaseHandler._build_response(response, True)

    @staticmethod
    def _question_response(lan):
        return AlexaForRFXHandler._build_response(responses.QUESTION_RESPONSE[lan], True)

    @staticmethod
    def _inst_data_response(lan):
        return AlexaForRFXHandler._build_response(responses.ENTRY_LIST_RESPONSE[lan], True)

    def _yes_no_response(self, intent, lan):
        yes_no = intent['slots']['YesNo']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
        if yes_no == "no":
            return AlexaForRFXHandler._build_response(responses.END_RESPONSE[lan])
        elif yes_no == "yes":
            return AlexaForRFXHandler._build_response(responses.ASK_INSTRUMENT_RESPONSE[lan], True)
        else:
            return AlexaForRFXHandler._build_response(responses.DEFAULT_RESPONSE[lan])

    def _last_price_response(self, intent, lan):

        response = responses.LAST_PRICE_RESPONSE[lan]

        # Check Product in Slot
        if 'Product' in intent['slots'] and AlexaForRFXHandler.keys_exists(intent['slots'], 'Product', 'resolutions', 'resolutionsPerAuthority', 0, 'values'):

            logging.debug(intent)
            product = intent['slots']['Product']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
            product_value = intent['slots']['Product']['value']
            logging.info("Product + " + str(product_value))

            if product.__contains__("spot"):

                api_response = self.restClient.market_data(config.Instrument[product]['initials'], 'IV')

                if api_response['marketData']['IV']:
                    response['card_output'] = responses.LAST_PRICE_OK_RESPONSE_SPOT[lan]['card_output'].format(
                                                                config.Instrument[product]['name'][lan],
                                                                str(api_response['marketData']['IV']))
                    response['speech_output'] = responses.LAST_PRICE_OK_RESPONSE_SPOT[lan]['speech_output'].format(
                                                                config.Instrument[product]['name'][lan],
                                                                str(api_response['marketData']['IV']))
                    response['reprompt_text'] = responses.LAST_PRICE_OK_RESPONSE_SPOT[lan]['reprompt_text']

                else:
                    response['card_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['card_output']
                    response['speech_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['speech_output']
                    response['reprompt_text'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['reprompt_text']
            else:
                if 'Month' in intent['slots'] and self.keys_exists(intent['slots']['Month'], 'resolutions'):
                    month = intent['slots']['Month']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
                    instrument = self._get_instrument(product, lan, month)
                else:
                    instrument = self._get_instrument(product, lan)

                logging.debug("Instrument: " + str(instrument))

                is_default_response = True
                entry_symbol = config.Entries['default']['symbol']

                # Check Market Data Entry
                if AlexaForRFXHandler.keys_exists(intent['slots'], 'Entry', 'resolutions', 'resolutionsPerAuthority', 0, 'values'):
                    entry = intent['slots']['Entry']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
                    is_default_response = False
                    entry_symbol = config.Entries[entry]['symbol']

                api_response = self.restClient.market_data(instrument['ticker'], entry_symbol)

                if api_response['status'] == 'ERROR':
                    response['card_output'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE[lan]['card_output'].format(instrument['prod'],
                                                                                                                            instrument['month'],
                                                                                                                            config.Month[str(AlexaForRFXHandler.find_closest_month(product))]['text'][lan])
                    response['speech_output'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE[lan]['speech_output'].format(instrument['prod'],
                                                                                                                                instrument['month'],
                                                                                                                                config.Month[str(AlexaForRFXHandler.find_closest_month(product))]['text'][lan])
                    response['reprompt_text'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE[lan]['reprompt_text']
                elif is_default_response:
                    price = api_response['marketData']['LA'] if api_response['marketData']['LA'] else api_response['marketData']['SE']
                    if price:
                        response['card_output'] = responses.LAST_PRICE_OK_RESPONSE[lan]['card_output'].format(
                            instrument['prod'], instrument['month'], str(price['price']))
                        response['speech_output'] = responses.LAST_PRICE_OK_RESPONSE[lan]['speech_output'].format(
                            instrument['prod'], instrument['month'], str(price['price']))
                        response['reprompt_text'] = responses.LAST_PRICE_OK_RESPONSE[lan]['reprompt_text']
                    else:
                        response['card_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['card_output'].format(instrument['prod'],
                                                  instrument['month'], config.Month[str(AlexaForRFXHandler.find_closest_month(product))]['text'][lan])
                        response['speech_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['speech_output'].format(instrument['prod'],
                                                    instrument['month'], config.Month[str(AlexaForRFXHandler.find_closest_month(product))]['text'][lan])
                        response['reprompt_text'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['reprompt_text']
                else:
                    price = api_response['marketData'][entry_symbol]
                    if price is not None:
                        price = price if not isinstance(price, dict) else price[config.Entries[entry]['side']]
                        response['card_output'] = responses.ENTRY_PRICE_OK_RESPONSE[lan]['card_output'].format(config.Entries[entry]['text'][lan],
                            instrument['prod'], instrument['month'], str(price))
                        response['speech_output'] = responses.ENTRY_PRICE_OK_RESPONSE[lan]['speech_output'].format(
                            config.Entries[entry]['text'][lan], instrument['prod'], instrument['month'], str(price))
                        response['reprompt_text'] = responses.ENTRY_PRICE_OK_RESPONSE[lan]['reprompt_text']
                    else:
                        response['card_output'] = responses.ENTRY_PRICE_MD_NOT_FOUND_RESPONSE[lan]['card_output'].format(config.Entries[entry]['text'][lan])
                        response['speech_output'] = responses.ENTRY_PRICE_MD_NOT_FOUND_RESPONSE[lan]['speech_output'].format(config.Entries[entry]['text'][lan])
                        response['reprompt_text'] = responses.ENTRY_PRICE_MD_NOT_FOUND_RESPONSE[lan]['reprompt_text']
        else: # No Product specified
            response['card_output'] = responses.LAST_PRICE_ERROR_RESPONSE[lan]['card_output']
            response['speech_output'] = responses.LAST_PRICE_ERROR_RESPONSE[lan]['speech_output']
            response['reprompt_text'] = responses.LAST_PRICE_ERROR_RESPONSE[lan]['reprompt_text']

        return AlexaBaseHandler._build_response(response, True)

    def _get_instrument(self, product_id, lan, month_id=-1):
        instrument = {"ticker": "", "month":""}
        if product_id in config.Instrument.keys():
            if month_id == -1:
                month_id = str(AlexaForRFXHandler.find_closest_month(product_id))
            year = str(datetime.now().year)[2:]
            if int(month_id) < datetime.now().month:
                year = str(datetime.now().year + 1)[2:]
            instrument['ticker'] = config.Instrument[product_id]['initials'] + config.Month[month_id]['initials'] + year
            instrument['month'] = config.Month[month_id]['text'][lan]
            instrument['prod'] = config.Instrument[product_id]['name'][lan]
        else:
            logging.debug("Instrument not found for product_ id " + product_id)
        return instrument

    @staticmethod
    def find_closest_month(product_id):
        close = bisect_left(config.Instrument[product_id]['trade_months'], datetime.now().month)
        if close == len(config.Instrument[product_id]['trade_months']):
            close = 0
        return config.Instrument[product_id]['trade_months'][close]

    @staticmethod
    def keys_exists(element, *keys):
        '''
        Check if *keys (nested) exists in `element` (dict).
        '''
        if type(element) is not dict:
            raise AttributeError('keys_exists() expects dict as first argument.')
        if len(keys) == 0:
            raise AttributeError('keys_exists() expects at least two arguments, one given.')

        _element = element
        for key in keys:
            try:
                _element = _element[key]
            except KeyError:
                return False
            except IndexError:
                return False
            except TypeError:
                return False
        return True
