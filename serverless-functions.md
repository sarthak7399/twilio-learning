# Twilio WebSocket Integration Testing

This README outlines the steps to test the integration of Twilio with your custom backend server using WebSockets.

## Prerequisites

1. Twilio Account with an active phone number.
2. Backend server capable of handling WebSocket connections.
3. ngrok or similar tool if running the server locally.

## Backend Server Setup

### Install Dependencies

Ensure you have Flask and Flask-Sockets installed:

```bash
pip install flask flask-sockets
```

### Backend Server Code

View serverless-functions.py

### Run the Backend Server

```bash
python serverless-functions.py
```

If running locally, use ngrok to expose it to the internet:

```bash
ngrok http 5000
```

Note the public URL provided by ngrok `(e.g., https://abc123.ngrok.io)`.

## Twilio Function Setup

### Create a Twilio Function

1. Log in to your Twilio Console.
2. Navigate to the "Functions" section under "Runtime".
3. Click "Create a Function" and choose the "Blank" template.
4. Use the following code:

```bash
exports.handler = function(context, event, callback) {
  const twiml = new Twilio.twiml.VoiceResponse();
  twiml.start().stream({
    url: 'wss://abc123.ngrok.io/media'
  });
  twiml.say('Connecting to the WebSocket server.');
  callback(null, twiml);
};
```

Replace 'wss://abc123.ngrok.io/media' with your ngrok public URL.

### Deploy the Function

Save and deploy your function. Note the URL provided by Twilio for this function.

## Configure Your Twilio Phone Number

1. Navigate to the "Phone Numbers" section in the Twilio Console.
2. Select your phone number.
3. Under the "Voice & Fax" tab, set the "A CALL COMES IN" field to "Function" and select your deployed function.
4. Save the configuration.

## Test the Setup

1. Make a call to your Twilio number.
2. Monitor your backend server logs for incoming connections and messages.
