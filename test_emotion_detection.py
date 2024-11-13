from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result_joy = emotion_detector('I am glad this happened')
        self.assertEqual(result_joy['dominant_emotion'], 'joy')
        
        # Test case for anger
        result_anger = emotion_detector('I am really mad about this')
        self.assertEqual(result_anger['dominant_emotion'], 'anger')
        
        # Test case for disgust
        result_disgust = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_disgust['dominant_emotion'], 'disgust')
        
        # Test case for sadness
        result_sadness = emotion_detector('I am so sad about this')
        self.assertEqual(result_sadness['dominant_emotion'], 'sadness')
        
        # Test case for fear
        result_fear = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_fear['dominant_emotion'], 'fear')

unittest.main()
