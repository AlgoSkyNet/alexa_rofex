<h1>ROFEX SKILL for ALEXA</h1>

version : 1.1.0

#### Intro

This project contains the code for a lambda AWS function used by ROFEX Skill. 

Also, in _`alexa_skill_model`_ folder you could find the JSON model of each Language of the Skill.

The Skill provide the user with the ability to ask prices for ROFEX instruments. The Intent that trigger the price response is the LastPriceIntent.

#### Configuration

Configuration variables are set in the _`configuration/config.py`_ module.

As this is intent to be used in a Lambda Function, the parameters are set as Environment Variables of the function. 
 
You need to have valid Primary API credential in order to authenticate and request prices to the API. 

#### How it work
The main entry point for the AWS Lambda function is the `lambda_handler` function in the _`main.py`_ module.

In the `_alexa_handler_` folder you could find the Base Class for the Alexa Handler. The only implementation of is the AlexaForRFXHandler that contain all the logic to process user's request to the Rofex Skill.

The modules in _`connector_pmy_api`_ folder are use to establish the connection to Primary API and request market data.

#### Support
Developer: Primary S.A.

Contact: mpi@primary.com.ar