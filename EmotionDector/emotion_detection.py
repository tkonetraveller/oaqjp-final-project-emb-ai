import requests
import json
from flask import jsonify

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        return format_response(response.text)
    else:
        return f"Error: {response.status_code}, {response.text}"

def format_response(response_text):
    data = json.loads(response_text)
    emotions = data['emotionPredictions'][0]['emotion']
    print(data)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return 
    return (dominant_emotion)