# Twilio-Learning

## Description

This repository demonstrates the integration of Twilio Media Streams with a FastAPI server. It includes endpoints to handle incoming calls, respond with a text-to-speech message using Twilio's Voice API, record the call, and hang up. Ideal for learning how to use Twilio's APIs with FastAPI for telephony applications.

### Usage

- Ensure you have Python installed.
- Install the required dependencies by running `pip install -r requirements.txt`.
- Set up your Twilio account and obtain the necessary credentials.
- Run the FastAPI server using `uvicorn <filename>:app --reload`.
- Configure your Twilio phone number to use the appropriate webhook URL.
- Test the integration by making a call to your Twilio number.
