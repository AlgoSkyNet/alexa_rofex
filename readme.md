<h1>ROFEX SKILL for ALEXA<h1>

<h2>Intro</h2>

This project contains the code for the lambda AWS function used by the Rofex Skill. Also in alexa_skill_model folder you could find the model of this Skill.

The Skill provide the user with the ability to ask prices for Rofex's products. The Intent that trigger the price response is the LastPriceIntent.

<h2>Configuration</h2>

The configuration variables are set in the configuration/config.py module.

You need to have a valid Primary API user/pass. This is used to authenticate and request prices to the API.

<h2>How it work</h2>
The main entry point for the AWS Lambda function is the lambda_handler function in the main.py module.

In the alexa_handler folder you could find the Base Class for the Alexa Handler. The only implementation of is the AlexaForRFXHandler that contain all the logic to process user's request to the Rofex Skill.

The modules in connector_pmy_api folder are use to establish the connection to Primary API and request market data.

