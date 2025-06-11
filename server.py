from flask import Flask, request, jsonify, render_template
from EmotionDector import emotion_detection

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotionDetector():
    emotion = None
    if request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze')
        emotion = emotion_detection.emotion_detector(text_to_analyze)  # Use the function
        system_response = jsonify({"emotion": emotion})
        return render_template('index.html', system_response=system_response)
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)