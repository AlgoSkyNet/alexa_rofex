import logging
from configuration.config import LOGGING_LEVEL
from alexa_handlers.AlexaForRFXHandler import AlexaForRFXHandler

"""
Main entry point for the Lambda function.
"""

logging.basicConfig(format='%(asctime)s %(message)s')
logging.getLogger().setLevel(LOGGING_LEVEL)


def lambda_handler(event, context):

    logging.info("Executing main lambda_handler for AlexaForRFXHandler class")

    alexa = AlexaForRFXHandler()
    alexa_response = alexa.process_request(event, context)

    return alexa_response



