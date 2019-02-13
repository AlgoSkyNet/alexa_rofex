# -*- coding: utf-8 -*-

import connector_pmy_api.pmy_rest_api as api
import configuration.config as config
import configuration.alexa_responses as responses
from datetime import datetime
from bisect import bisect_left
from alexa_handlers.AlexaBaseHandler import AlexaBaseHandler


class AlexaForRFXHandler(AlexaBaseHandler):
    """
    Concrete implementation of the AlexaBaseHandler for the ROFEX Skill.
    """

    def __init__(self):
        super(self.__class__, self).__init__()
        self.restClient = api.RestClient(config.Primary_API.USER, config.Primary_API.PASS, config.Primary_API.ENVIRONMENT)
        is_login = self.restClient.login()

    def on_launch(self, launch_request, session, lan):
        return self._init_response(lan)

    def on_session_started(self, session_started_request, session):
        self.logger.info("On session started:")
        self.logger.info("on_intent requestId=" + session_started_request['requestId'] +
                         ", sessionId=" + session['sessionId'])

    def on_intent(self, intent_request, session, lan):
        """ Called when the user specifies an intent for this skill """

        self.logger.info("on_intent requestId=" + intent_request['requestId'] +
                     ", sessionId=" + session['sessionId'])

        intent = intent_request['intent']
        intent_name = intent_request['intent']['name']

        # Dispatch to your skill's intent handlers

        # Custom Intents
        if intent_name == "LastPriceIntent":
            return self.last_price_response(intent, lan)
        if intent_name == "ProductListIntent":
            return self.product_list_response(lan)
        if intent_name == "CloseIntent":
            return self.on_session_ended(intent, session, lan)

        # Amazon Default Intents
        if intent_name == "AMAZON.HelpIntent":
            return self.on_help_intent(lan)
        if intent_name == "AMAZON.FallbackIntent":
            return self._default_response(lan)

        return self._default_response(lan)

    def on_language_not_supported(self, lan):
        return self._language_not_supported_response(lan)

    def on_help_intent(self, lan):
        return self._help_response(lan)

    def on_session_ended(self, session_end_request, session, lan):
        return self._end_response(lan)

    def on_processing_error(self, event, context, exc, lan):
        self.logger.error("on_processing_error: " + str(exc))
        return self._error_response(lan)

    def _language_not_supported_response(self, lan):
        return self._build_response(responses.LANGUAGE_NOT_SUPPORTED.format(lan))

    def _default_response(self, lan):
        return self._build_response(responses.DEFAULT_RESPONSE[lan])

    def _init_response(self, lan):
        return self._build_response(responses.INIT_RESPONSE[lan], True)

    def _end_response(self, lan):
        return self._build_response(responses.END_RESPONSE[lan])

    def _help_response(self, lan):
        return self._build_response(responses.HELP_RESPONSE[lan], True)

    def _error_response(self, lan):
        return self._build_response(responses.ERROR_RESPONSE[lan], True)

    def product_list_response(self, lan):
        return self._build_response(responses.LIST_RESPONSE[lan], True)

    def last_price_response(self, intent, lan):

        response = responses.LAST_PRICE_RESPONSE[lan]

        if 'Product' in intent['slots'] and AlexaForRFXHandler.keys_exists(intent['slots']['Product']['resolutions']['resolutionsPerAuthority'][0], 'values'):

            self.logger.info(intent)
            product = intent['slots']['Product']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
            product_value = intent['slots']['Product']['value']
            self.logger.info("Product + " + str(product_value))

            if 'Month' in intent['slots'] and self.keys_exists(intent['slots']['Month'], 'resolutions'):
                month = intent['slots']['Month']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
                instrument = self._get_instrument(product, lan, month)
            else:
                instrument = self._get_instrument(product, lan)

            self.logger.info("Instrument: " + str(instrument))

            api_response = self.restClient.market_data(instrument['ticker'], 'LA,SE')

            self.logger.info("API Response: " + str(api_response))

            if api_response['status'] == 'ERROR':
                response['card_output'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE[lan]['card_output'].format(instrument['prod'], instrument['month'], config.Month[str(self.find_closest_month(product))]['text'][lan])
                response['speech_output'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE[lan]['speech_output'].format(instrument['prod'], instrument['month'], config.Month[str(self.find_closest_month(product))]['text'][lan])
                response['reprompt_text'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE[lan]['reprompt_text']
            else:
                last_price_response = api_response['marketData']['LA']
                settlement_price_response = api_response['marketData']['SE']
                if last_price_response:
                    response['card_output'] = responses.LAST_PRICE_OK_RESPONSE[lan]['card_output'].format(
                        instrument['prod'], instrument['month'], str(last_price_response['price']))
                    response['speech_output'] = responses.LAST_PRICE_OK_RESPONSE[lan]['speech_output'].format(
                        instrument['prod'], instrument['month'], str(last_price_response['price']))
                    response['reprompt_text'] = responses.LAST_PRICE_OK_RESPONSE[lan]['reprompt_text']
                elif settlement_price_response:
                    response['card_output'] = responses.SETTLE_PRICE_OK_RESPONSE[lan]['card_output'].format(
                        instrument['prod'], instrument['month'], str(settlement_price_response['price']))
                    response['speech_output'] = responses.SETTLE_PRICE_OK_RESPONSE[lan]['speech_output'].format(
                        instrument['prod'], instrument['month'], str(settlement_price_response['price']))
                    response['reprompt_text'] = responses.SETTLE_PRICE_OK_RESPONSE[lan]['reprompt_text']
                else:
                    response['card_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['card_output']
                    response['speech_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['speech_output']
                    response['reprompt_text'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['reprompt_text']

        else:
            response['card_output'] = responses.LAST_PRICE_ERROR_RESPONSE[lan]['card_output']
            response['speech_output'] = responses.LAST_PRICE_ERROR_RESPONSE[lan]['speech_output']
            response['reprompt_text'] = responses.LAST_PRICE_ERROR_RESPONSE[lan]['reprompt_text']

        return self._build_response(response, True)

    def _get_instrument(self, product_id, lan, month_id=-1):
        instrument = {"ticker": "", "month":""}
        if product_id in config.Instrument.keys():
            if month_id == -1:
                month_id = str(self.find_closest_month(product_id))
            year = str(datetime.now().year)[2:]
            if int(month_id) < datetime.now().month:
                year = str(datetime.now().year + 1)[2:]
            instrument['ticker'] = config.Instrument[product_id]['initials'] + config.Month[month_id]['initials'] + year
            instrument['month'] = config.Month[month_id]['text'][lan]
            instrument['prod'] = config.Instrument[product_id]['name'][lan]
        else:
            self.logger.info("Instrument not found for product_ id " + product_id)
        return instrument

    def find_closest_month(self, product_id):
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
        return True

if __name__ == "__main__":

    # Create
    alexa = AlexaForRFXHandler()

    response = responses.LAST_PRICE_RESPONSE

    lan = config.Language.ES
    pro = 'rfx20'
    t_product_value = 'rofex 20'
    month = '11'
    alexa.logger.info("Product + " + str(t_product_value))

    instrument = alexa._get_instrument(pro, lan)
    alexa.logger.info("Instrument + " + instrument['ticker'])
    api_response = alexa.restClient.market_data(instrument['ticker'], 'LA')

    if api_response['status'] == 'ERROR':
        response['speech_output'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE[lan]['speech_output'].format(
            instrument['prod'])
        response['reprompt_text'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE[lan]['reprompt_text']
    else:
        api_response = api_response['marketData']['LA']
        if api_response:
            response['speech_output'] = responses.LAST_PRICE_OK_RESPONSE[lan]['speech_output'].format(instrument['prod'],
                                                                                                    instrument['month'],
                                                                                                    str(api_response['price']))
            response['reprompt_text'] = responses.LAST_PRICE_OK_RESPONSE[lan]['reprompt_text']
        else:
            response['speech_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['speech_output']
            response['reprompt_text'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]['reprompt_text']

    print(response['speech_output'])
