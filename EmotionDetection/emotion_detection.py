import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)
    
    print(response)
    
    anger_score = 0
    disgust_score = 0
    fear_score = 0
    joy_score = 0
    sadness_score = 0
    dominant_emotion = 'none'  

    if response.status_code == 200:
        # Convertir respuesta a JSON
        formatted_response = json.loads(response.text)

        
        # Extraer puntajes
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        print(emotions)

        anger_score = emotions.get("anger", 0)
        disgust_score = emotions.get("disgust", 0)
        fear_score = emotions.get("fear", 0)
        joy_score = emotions.get("joy", 0)
        sadness_score = emotions.get("sadness", 0)

        # Determinar emoción dominante
        scores = {
            'Anger': anger_score,
            'Disgust': disgust_score,
            'Fear': fear_score,
            'Joy': joy_score,
            'Sadness': sadness_score
        }

        dominant_emotion = max(scores, key=scores.get)

    elif response.status_code == 500:
        anger_score = 0
        disgust_score = 0
        fear_score = 0
        joy_score = 0
        sadness_score = 0
        dominant_emotion = 'none'   

    elif response.status_code == 400:
        anger_score = 0
        disgust_score = 0
        fear_score = 0
        joy_score = 0
        sadness_score = 0
        dominant_emotion = 'none'   

    else:
        anger_score = 0
        disgust_score = 0
        fear_score = 0
        joy_score = 0
        sadness_score = 0
        dominant_emotion = 'none'   

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }


