import json
import requests

def emotion_detector(text_to_analyze):
    # URL do serviço Watson NLP fornecido no ambiente do laboratório da IBM
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Cabeçalho exigido pela API da IBM com o ID do modelo
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Formato do JSON que a API espera receber
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Fazendo a requisição POST para a API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Se a resposta for bem-sucedida (Status 200)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        
        # Extraindo o dicionário de emoções do retorno da API
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Isolando os scores de cada emoção
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        
        # Descobrindo qual emoção tem a maior nota (o score mais alto)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Formatando o dicionário final exatamente como o Coursera exige
        result = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        # Caso ocorra algum erro na API (fallback de segurança)
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    return result
