"""
SentimentClassifier using VADER from NLTK.
No training required. Suitable for general English sentiment analysis.
"""

from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentClassifier:
    def __init__(self):
        """
        Initialize the VADER sentiment intensity analyzer.
        Downloads the VADER lexicon if not already present.
        """
        import nltk
        try:
            nltk.data.find('sentiment/vader_lexicon.zip')
        except LookupError:
            nltk.download('vader_lexicon')
        self.analyzer = SentimentIntensityAnalyzer()

    def predict(self, texts):
        """
        Predict sentiment for a list of texts using VADER.

        Parameters:
        texts (list of str): List of input sentences.

        Returns:
        list of int: Predicted sentiment labels (1 for positive, 0 for negative).
        """
        results = []
        for text in texts:
            score = self.analyzer.polarity_scores(text)['compound']
            results.append(1 if score >= 0 else 0)
        return results