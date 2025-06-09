import unittest
from EmotionDector import emotion_detection  

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        statement = "I am glad this happened"
        expected_emotion = "joy"
        self.assertEqual(emotion_detection.emotion_detector(statement), expected_emotion)

    def test_anger(self):
        statement = "I am really mad about this"
        expected_emotion = "anger"
        self.assertEqual(emotion_detection.emotion_detector(statement), expected_emotion)

    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        expected_emotion = "disgust"
        self.assertEqual(emotion_detection.emotion_detector(statement), expected_emotion)

    def test_sadness(self):
        statement = "I am so sad about this"
        expected_emotion = "sadness"
        self.assertEqual(emotion_detection.emotion_detector(statement), expected_emotion)

    def test_fear(self):
        statement = "I am really afraid that this will happen"
        expected_emotion = "fear"
        self.assertEqual(emotion_detection.emotion_detector(statement), expected_emotion)

if __name__ == '__main__':
    unittest.main()