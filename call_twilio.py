# This FastAPI application is designed to handle incoming voice calls using Twilio's Voice API. The application provides a single endpoint, /voice, which responds to incoming POST requests to greet the caller with a message, record their response, and then hang up. Additionally, Cross-Origin Resource Sharing (CORS) is enabled for all origins, allowing the API to be accessed from any domain.

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from twilio.twiml.voice_response import VoiceResponse, Say, Record, Hangup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/voice")
async def voice(request: Request):
    response = VoiceResponse()
    content="Hello, This is Uday from Surya Hospital. How may I help you?"
    response.say(content, voice='Polly.Emma')
    response.record()
    response.hangup()
    return PlainTextResponse(str(response), media_type="application/xml")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
