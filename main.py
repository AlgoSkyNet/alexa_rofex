import logging
from alexa_handlers.AlexaForRFXHandler import AlexaForRFXHandler

"""
Main entry point for the Lambda function.
"""

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    logging.info("Executing main lambda_handler for AlexaForRFXHandler class")

    alexa = AlexaForRFXHandler()
    alexa_response = alexa.process_request(event, context)

    return alexa_response



