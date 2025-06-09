from flask import Flask, request, jsonify
from EmotionDector import emotion_detection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    emotion = None
    if request.method == 'POST':
        text_to_analyze = request.form['text']
        emotion = emotion_detection.emotion_detector(text_to_analyze)  # Use the function
    return render_template('index.html', emotion=emotion)


@app.route('/emotion', methods=['POST'])
def detect_emotion():
    text_to_analyze = request.json.get('text')
    emotion = emotion_detection.emotion_detector(text_to_analyze)
    return ({"emotion": emotion})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)