# modules/sentiment.py

from textblob import TextBlob
from transformers import pipeline
import json


emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

def Sentiment(prompt: str) -> dict:
    blob = TextBlob(prompt)
    polarity: float = round(blob.sentiment.polarity, 2)  # -1 to 1
    subjectivity: float = round(blob.sentiment.subjectivity, 2)  # 0 to 1

    # Emotion detection
    emotion_result = emotion_model(prompt)[0]
    emotion: list[str] = [e['label'] for e in emotion_result if e['score'] > 0.2]

    # Intensity
    max_score = max(e['score'] for e in emotion_result)
    if max_score > 0.75:
        intensity: str = "high"
    elif max_score > 0.4:
        intensity = "moderate"
    else:
        intensity = "low"

    # Toxicity check
    toxic_words = {"hate", "stupid", "idiot", "kill", "worthless"}
    toxicity: bool = any(w in prompt.lower() for w in toxic_words)

    # Dummy target sentiment
    targets = ["product", "delivery"]
    targeted_sentiment: dict[str, float] = {}
    for target in targets:
        if target in prompt.lower():
            targeted_sentiment[target] = round(blob.sentiment.polarity, 2)

    result = {
        "polarity": polarity,
        "subjectivity": subjectivity,
        "emotion": emotion,
        "intensity": intensity,
        "toxicity": toxicity,
        "targeted_sentiment": targeted_sentiment
    }

    # Convert Python dict to a TypeScript-style string
    ts = "const response: SentimentResponse = " + json.dumps(result, indent=2).replace("true", "true").replace("false", "false") + ";"
    return ts
