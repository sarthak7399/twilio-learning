from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import logging
import base64
from pydub import AudioSegment
from io import BytesIO

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.websocket("/audio-stream")
async def audio_stream(websocket: WebSocket):
    await websocket.accept()
    logging.info("WebSocket connection accepted")

    audio_data = b''  # Initialize an empty byte string to hold the audio data

    try:
        while True:
            message = await websocket.receive()
            logging.info(f"Received message: {message}")

            if 'text' in message:
                text_message = message['text']
                logging.info(f"Received text message: {text_message}")
                audio_data += handle_text_message(text_message)
            elif 'ping' in message:
                logging.info("Received ping")
                await websocket.send_pong()
            elif 'pong' in message:
                logging.info("Received pong")
            elif 'type' in message and message['type'] == 'websocket.disconnect':
                logging.info("WebSocket connection disconnected")
                break
            else:
                logging.warning("Received unknown message type")
    except WebSocketDisconnect:
        logging.info("WebSocket connection closed by client")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        if audio_data:
            save_audio_to_mp3(audio_data)

def handle_text_message(message):
    import json
    data = json.loads(message)
    audio_data = b''
    if data.get('event') == 'media':
        payload = data['media']['payload']
        audio_data = base64.b64decode(payload)
    elif data.get('event') == 'stop':
        logging.info("Received stop event")
    return audio_data

        
def save_audio_to_mp3(audio_data):
    # Check if audio_data is not empty
    if audio_data:
        audio_segment = AudioSegment(
            data=BytesIO(audio_data).read(),
            sample_width=2,  # Adjusted sample width
            frame_rate=8000,  # Adjusted frame rate
            channels=1  # Adjusted channels
        )
        audio_segment.export("output.mp3", format="mp3")
        logging.info("Audio saved as output.mp3")
    else:
        logging.warning("No audio data to save")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
