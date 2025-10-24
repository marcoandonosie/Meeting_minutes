import os
#import requests

def transcribe_audio(file_path):
    '''
    api_key = os.getenv("ELEVENLABS_API_KEY")
    url = "https://api.elevenlabs.io/v1/speech-to-text"
    
    with open(file_path, "rb") as f:
        response = requests.post(
            url,
            headers={"xi-api-key": api_key},
            files={"file": f}
        )
    response.raise_for_status()
    return response.json().get("text", "")
'''
    with open("examples/real_transcript.txt", "r", encoding="utf-8") as f:
        transcript = f.read()
        return transcript