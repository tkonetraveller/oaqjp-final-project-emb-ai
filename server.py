
"""
flask server for emotion detection using a GET endpoint
Handles input validation and returns emtion analysis results.
"""

from flask import Flask, request, render_template
from werkzeug.exceptions import HTTPException
from .EmotionDector import emotion_detection


app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    """
    Handles GET requests for emotion detection.
    Expects a 'textToAnalyze' query parameter and returns the detected emotion.
    Returns 'None' with a 400 status if input is missing.
    """
    try:
        text_to_analyze = request.args.get('textToAnalyze')
        if not text_to_analyze:
            emotion = "None"
            return "Invalid text! Please try again!"

        emotion = emotion_detection.emotion_detector(text_to_analyze)
        return f"Detected Emotion: {emotion}"
    except HTTPException as http_exc:
        if http_exc.code == 400:
            return "None", 400
        return f"HTTP Error: {http_exc.description}", http_exc.code

@app.route('/')
def index():
    """Handles GET requests to index.html"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
