import abc
import logging


class AlexaBaseHandler(object):
    """
    Base class for a Alexa Skill Set.  Concrete implementations
    are expected to implement the abstract methods.

    See the following for Alexa details:
    https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/handling-requests-sent-by-alexa
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        logging.basicConfig()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    @abc.abstractmethod
    def on_launch(self, launch_request, session):
        """
        Implement the LaunchRequest.  Called when the user issues a:
        Alexa, open <invocation name>
        :param launch_request:
        :param session:
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
    def on_intent(self, intent_request, session):
        """
        Implement the IntentRequest
        :param intent_request:
        :param session:
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_session_ended(self, session_end_request, session):
        """
        Implement the SessionEndRequest
        :param session_end_request:
        :param session:
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_processing_error(self, event, context, exc):
        """
        If an unexpected error occurs during the process_request method
        this handler will be invoked to give the concrete handler
        an opportunity to respond gracefully

        :param exc exception instance
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
        self.logger.info(event)
        try:
            response = None

            # if its a new session, run the new session code
            if event['session']['new']:
                self.on_session_started({'requestId': event['request']['requestId']}, event['session'])

            # regardless of whether its new, handle the request type
            if event['request']['type'] == "LaunchRequest":
                response = self.on_launch(event['request'], event['session'])
            elif event['request']['type'] == "IntentRequest":
                response = self.on_intent(event['request'], event['session'])
            elif event['request']['type'] == "SessionEndedRequest":
                response = self.on_session_ended(event['request'], event['session'])

        except Exception as exc:
            response = self.on_processing_error(event, context, exc)

        return response

    # --------------- Helpers that build all of the responses ----------------------
    def _build_response(self, response):
        """
        Internal helper method to build the Alexa response message
        :param response: alexa response
        :return: properly formatted Alexa response
        """
        self.logger.info(response)

        return {
            'version': '1.0',
            'sessionAttributes': response['session_attributes'],
            'response': {
                            'outputSpeech': {
                                'type': 'PlainText',
                                'text': response['speech_output']
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
