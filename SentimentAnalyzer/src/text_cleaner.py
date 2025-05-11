class TextCleaner:
    def clean_texts(self, texts):
        """
        Clean a list of texts using the clean_text method.
        
        Parameters:
        texts (list of str): List of input texts to be cleaned.
        
        Returns:
        list of str: List of cleaned texts.
        """
        return [self.clean_text(text) for text in texts]
    def __init__(self):
        import nltk
        from nltk.corpus import stopwords
        from nltk.stem import WordNetLemmatizer
        
        nltk.download('stopwords')
        nltk.download('wordnet')
        
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):
        """
        Normalize the input text by converting to lowercase,
        removing stopwords, and lemmatizing the words.
        
        Parameters:
        text (str): The input text to be cleaned.
        
        Returns:
        str: The normalized text.
        """
        # Convert to lowercase
        text = text.lower()
        
        # Tokenize the text
        words = text.split()
        
        # Remove stopwords and lemmatize
        cleaned_words = [self.lemmatizer.lemmatize(word) for word in words if word not in self.stop_words]
        
        # Join the cleaned words back into a single string
        return ' '.join(cleaned_words)