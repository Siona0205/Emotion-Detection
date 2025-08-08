from transformers import pipeline

# Load the pretrained emotion classification model
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def predict_emotion(text):
    """
    Predict the emotion from input text.
    Returns:
        - emotion label (string)
        - confidence score (float)
    """
    result = emotion_classifier(text)
    label = result[0]['label']
    score = round(result[0]['score'], 2)
    return label, score

# Optional test
if __name__ == "__main__":
    emotion, confidence = predict_emotion("I feel hopeless and anxious")
    print(f"Emotion: {emotion}, Confidence: {confidence}")
