# main.py

from text_cleaner import TextCleaner
from sentiment_model import SentimentClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def main():
    # Load team emails dataset
    data = pd.read_csv('data/team_emails.csv')

    # Use the 'body' column for sentiment analysis
    email_bodies = data['body'].tolist()

    # Initialize sentiment classifier (VADER-based, no training needed)
    sentiment_classifier = SentimentClassifier()

    # Clean the email bodies (optional, but can help VADER)
    text_cleaner = TextCleaner()
    cleaned_bodies = text_cleaner.clean_texts(email_bodies)

    # Predict sentiment for each email body
    predictions = sentiment_classifier.predict(cleaned_bodies)

    # Output predictions alongside sender and subject
    print("Sentiment Analysis Results for Team Emails:")
    for sender, subject, body, sentiment in zip(data['sender'], data['subject'], data['body'], predictions):
        sentiment_label = 'Positive' if sentiment == 1 else 'Negative'
        print(f"From: {sender} | Subject: {subject}\n  Sentiment: {sentiment_label}\n  Body: {body}\n")

if __name__ == "__main__":
    main()