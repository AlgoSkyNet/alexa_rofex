import abc
import logging
import configuration.config as config


class AlexaBaseHandler(object):
    """
    Base class for a Alexa Skill Set.
    Concrete implementations are expected to implement the abstract methods.

    See the following for Alexa details:
    https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/handling-requests-sent-by-alexa
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        logging.debug("init AlexaBaseHandler")

    @abc.abstractmethod
    def on_launch(self, launch_request, session, lan):
        """
        Implement the LaunchRequest.  Called when the user issues a:
        Alexa, open <invocation name>
        :param launch_request:
        :param session:
        :param lan: request language
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_session_started(self, session_started_request, session):
        """
        Called if the user session is new.
        :param session_started_request:
        :param session:
        """
        pass

    @abc.abstractmethod
    def on_intent(self, intent_request, session, lan):
        """
        Implement the IntentRequest
        :param intent_request:
        :param session:
        :param lan: request language
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_session_ended(self, session_end_request, session, lan):
        """
        Implement the SessionEndRequest
        :param session_end_request:
        :param session:
        :param lan: request language
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_processing_error(self, event, context, exc, lan):
        """
        If an unexpected error occurs during the process_request method
        this handler will be invoked to give the concrete handler
        an opportunity to respond gracefully

        :param exc exception instance
        :param lan: request language
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_language_not_supported(self, lan):
        """
        If the language of the request is not supported
        this handler will respond appropriately

        :param lan language not supported
        :return: the output of _build_response
        """
        pass

    def process_request(self, event, context):
        """
        Method to process the input Alexa request and
        dispatch to the appropriate on_ handler
        :param event:
        :param context:
        :return: response from the on_ handler
        """

        logging.info("Alexa Event: " + str(event))

        try:
            response = None

            # if its a new session, run the new session code
            if event['session']['new']:
                self.on_session_started({'requestId': event['request']['requestId']}, event['session'])

            # Check the language of the request
            lan = event['request']['locale']
            if lan.__contains__("es"):
                lan = config.Language.ES
            elif lan.__contains__("en"):
                lan = config.Language.EN
            else:
                # IF THE LANGUAGE IS NOT SUPPORTED
                response = self.on_language_not_supported(lan)

            # regardless of whether its new, handle the request type
            if event['request']['type'] == "LaunchRequest":
                response = self.on_launch(event['request'], event['session'], lan)
            elif event['request']['type'] == "IntentRequest":
                response = self.on_intent(event['request'], event['session'], lan)
            elif event['request']['type'] == "SessionEndedRequest":
                response = self.on_session_ended(event['request'], event['session'], lan)

        except Exception as exc:
            response = self.on_processing_error(event, context, exc, lan)

        logging.info(response)
        return response

    # --------------- Helpers that build all of the responses ----------------------
    @staticmethod
    def _build_response(response, ssml=False):
        """
        Internal helper method to build the Alexa response message
        :param response: alexa response
        :param ssml: True if response is "SSML" format
        :return: properly formatted Alexa response
        """

        return {
            'version': '1.0',
            'sessionAttributes': response['session_attributes'],
            'response': {
                            'outputSpeech': {
                                'type': 'PlainText',
                                'text': response['speech_output']
                            } if not ssml else {
                                'type': 'SSML',
                                'ssml': response['speech_output']
                            },
                            'card': {
                                'type': 'Simple',
                                'title': response['card_title'],
                                'content': response['card_output']
                            },
                            'reprompt': {
                                'outputSpeech': {
                                    'type': 'PlainText',
                                    'text': response['reprompt_text']
                                }
                            },
                            'shouldEndSession': response['should_end_session']
                        }
                }
