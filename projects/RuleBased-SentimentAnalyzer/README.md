# Sentiment Analyzer

A simple tool that analyzes the sentiment (positive/negative) of text using VADER, optimized for reviews, comments, and social media content.

## Overview

- **Purpose:** Analyze sentiment in English text without requiring training data
- **Method:** VADER (Valence Aware Dictionary and sEntiment Reasoner)
- **Input:** General English text (reviews, comments, emails)
- **Output:** Positive/Negative sentiment classification

## Project Structure

```
src/
├── text_cleaner.py     # Text normalization
├── sentiment_model.py  # VADER classifier
└── main.py            # Main pipeline
```

## Quick Start

1. **Setup Environment:**
   ```
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

2. **Run the Analyzer:**
   ```
   python src/main.py
   ```

## Dependencies

- nltk
- scikit-learn
- pandas

## License

MIT License