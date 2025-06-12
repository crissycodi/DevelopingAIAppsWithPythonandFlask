from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):

        def test_positive_sentiment(self):
            result = sentiment_analyzer("I love working with Python")
            self.assertIn("SENT_POSITIVE", result)

        def test_negative_sentiment(self):
            result = sentiment_analyzer("I hate working with Python")
            self.assertIn("SENT_NEGATIVE", result)

        def test_neutral_sentiment(self):
            result = sentiment_analyzer("I am neutral on Python")
            self.assertIn("SENT_NEUTRAL", result)

if __name__ == '__main__':
    unittest.main()
