# coding: utf-8

import connector_pmy_api.pmy_rest_api as api
import configuration.config as config
import configuration.alexa_responses_eng as responses
from datetime import datetime

from alexa_handlers.AlexaBaseHandler import AlexaBaseHandler


class AlexaForRFXHandler(AlexaBaseHandler):
    """
    Concrete implementation of the AlexaBaseHandler for the ROFEX Skill.
    """

    def __init__(self):
        super(self.__class__, self).__init__()
        self.restClient = api.RestClient(config.Primary_API.USER, config.Primary_API.PASS, config.Primary_API.ENVIRONMENT)
        is_login = self.restClient.login()

    def on_launch(self, launch_request, session):
        return self._init_response()

    def on_session_started(self, session_started_request, session):
        self.logger.info("On session started:")
        self.logger.info("on_intent requestId=" + session_started_request['requestId'] +
                         ", sessionId=" + session['sessionId'])

    def on_intent(self, intent_request, session):
        """ Called when the user specifies an intent for this skill """

        self.logger.info("on_intent requestId=" + intent_request['requestId'] +
                     ", sessionId=" + session['sessionId'])

        intent = intent_request['intent']
        intent_name = intent_request['intent']['name']

        # Dispatch to your skill's intent handlers

        # Custom Intents
        if intent_name == "LastPriceIntent":
            return self.last_price_response(intent)
        if intent_name == "CloseIntent":
            return self.on_session_ended(intent, session)

        # Required Intents
        if intent_name == "AMAZON.CancelIntent":
            return self.on_cancel_intent()
        if intent_name == "AMAZON.HelpIntent":
            return self.on_help_intent()
        if intent_name == "AMAZON.StopIntent":
            return self.on_stop_intent()

        return self._default_response()

    def on_cancel_intent(self):
        return self._end_response()

    def on_help_intent(self):
        return self._help_response()

    def on_stop_intent(self):
        return self._end_response()

    def on_session_ended(self, session_end_request, session):
        return self._end_response()

    def on_processing_error(self, event, context, exc):
        self.logger.error("on processing error \n" + str(exc))
        return self._error_response()

    def _default_response(self, msg):
        return self._build_response(responses.DEFAULT_RESPONSE)

    def _init_response(self):
        return self._build_response(responses.INIT_RESPONSE)

    def _end_response(self):
        return self._build_response(responses.END_RESPONSE)

    def _help_response(self):
        return self._build_response(responses.HELP_RESPONSE)

    def _error_response(self):
        return self._build_response(responses.ERROR_RESPONSE)

    def last_price_response(self, intent):

        response = responses.LAST_PRICE_RESPONSE

        if 'Product' in intent['slots']:

            self.logger.info(intent)
            product = intent['slots']['Product']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
            product_value = intent['slots']['Product']['value']
            self.logger.info("Product + " + str(product_value))

            if 'Month' in intent['slots'] and self.keys_exists(intent['slots']['Month'], 'resolutions'):
                month = intent['slots']['Month']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
                instrument = self._get_instrument(product, month)
            else:
                instrument = self._get_instrument(product)

            self.logger.info("Instrument: " + str(instrument))

            api_response = self.restClient.market_data(instrument['ticker'], 'LA,SE')

            self.logger.info("API Response: " + str(api_response))

            if api_response['status'] == 'ERROR':
                response['card_output'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE['card_output'].format(product_value)
                response['speech_output'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE['speech_output'].format(product_value)
                response['reprompt_text'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE['reprompt_text']
            else:
                last_price_response = api_response['marketData']['LA']
                settlement_price_response = api_response['marketData']['SE']
                if last_price_response:
                    response['card_output'] = responses.LAST_PRICE_OK_RESPONSE['card_output'].format(
                        product_value, instrument['month'], str(last_price_response['price']))
                    response['speech_output'] = responses.LAST_PRICE_OK_RESPONSE['speech_output'].format(
                        product_value, instrument['month'], str(last_price_response['price']))
                    response['reprompt_text'] = responses.LAST_PRICE_OK_RESPONSE['reprompt_text']
                elif settlement_price_response:
                    response['card_output'] = responses.SETTLE_PRICE_OK_RESPONSE['card_output'].format(
                        product_value, instrument['month'], str(settlement_price_response['price']))
                    response['speech_output'] = responses.SETTLE_PRICE_OK_RESPONSE['speech_output'].format(
                        product_value, instrument['month'], str(settlement_price_response['price']))
                    response['reprompt_text'] = responses.SETTLE_PRICE_OK_RESPONSE['reprompt_text']
                else:
                    response['card_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE['card_output']
                    response['speech_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE['speech_output']
                    response['reprompt_text'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE['reprompt_text']

        else:
            response['card_output'] = responses.LAST_PRICE_ERROR_RESPONSE['card_output']
            response['speech_output'] = responses.LAST_PRICE_ERROR_RESPONSE['speech_output']
            response['reprompt_text'] = responses.LAST_PRICE_ERROR_RESPONSE['reprompt_text']

        return self._build_response(response)

    @staticmethod
    def _get_instrument(product_id, month_id=-1):
        instrument = {"ticker": "", "month":""}
        if product_id in config.Instrument.keys():
            if month_id == -1:
                instrument['ticker'] = config.Instrument[product_id]['last_instrument']
                instrument['month'] = config.Instrument[product_id]['last_month']
            else:
                year = str(datetime.now().year)[2:]
                if int(month_id) < datetime.now().month:
                    year = str(datetime.now().year + 1)[2:]
                instrument['ticker'] = config.Instrument[product_id]['initials'] + config.Month[month_id]['initials'] + year
                instrument['month'] = config.Month[month_id]['text']
        else:
            alexa.logger.info("Instrument not found for product_ id " + product_id)
        return instrument

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

    product = 'dolar'
    t_product_value = 'dolar'
    month = '11'
    alexa.logger.info("Product + " + str(t_product_value))

    instrument = alexa._get_instrument(product, month)
    alexa.logger.info("Instrument + " + instrument['ticker'])
    api_response = alexa.restClient.market_data(instrument['ticker'], 'LA')

    if api_response['status'] == 'ERROR':
        response['speech_output'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE['speech_output'].format(
            t_product_value)
        response['reprompt_text'] = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE['reprompt_text']
    else:
        api_response = api_response['marketData']['LA']
        if api_response:
            response['speech_output'] = responses.LAST_PRICE_OK_RESPONSE['speech_output'].format(t_product_value,
                                                                                                 instrument['month'],
                                                                                                  str(api_response['price']))
            response['reprompt_text'] = responses.LAST_PRICE_OK_RESPONSE['reprompt_text']
        else:
            response['speech_output'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE['speech_output']
            response['reprompt_text'] = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE['reprompt_text']

    print(response['speech_output'])
