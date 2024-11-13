import requests
import json

def emotion_detector(text_to_analyse):
    # Check for blank input
    if not text_to_analyse.strip():  # Ensures input isn't just whitespace
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json=myobj, headers=header)

        # Handle status_code 400 explicitly
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        # Handle other non-200 responses
        if response.status_code != 200:
            return {"error": f"Failed to fetch data: {response.status_code}"}

        # Parse the JSON response
        formatted_response = json.loads(response.text)

        # Extract emotions and their scores
        try:
            emotion_data = formatted_response['emotionPredictions'][0]['emotion']
            emotions = {
                "anger": emotion_data.get("anger", 0),
                "disgust": emotion_data.get("disgust", 0),
                "fear": emotion_data.get("fear", 0),
                "joy": emotion_data.get("joy", 0),
                "sadness": emotion_data.get("sadness", 0),
            }

            # Determine the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)
            emotions["dominant_emotion"] = dominant_emotion

            return emotions

        except (KeyError, IndexError):
            # Handle unexpected response format
            return {"error": "Unexpected API response format"}

    except Exception as e:
        # Handle other exceptions (e.g., network errors)
        return {"error": f"An error occurred: {str(e)}"}
