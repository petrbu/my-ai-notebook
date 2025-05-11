class FeatureExtractor:
    def __init__(self):
        from sklearn.feature_extraction.text import TfidfVectorizer
        self.vectorizer = TfidfVectorizer()

    def fit(self, X_train):
        """Fit the TF-IDF vectorizer on the training data."""
        self.vectorizer.fit(X_train)

    def transform(self, X):
        """Transform the input data into TF-IDF feature vectors."""
        return self.vectorizer.transform(X)

    def fit_transform(self, X_train):
        """Fit the vectorizer and transform the training data in one step."""
        return self.vectorizer.fit_transform(X_train)