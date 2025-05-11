# Sentiment Analyzer: Usage Guide

This guide explains how to set up and use the Sentiment Analyzer to classify text as positive or negative.

## Project Structure

```
SentimentAnalyzer
├── src
│   ├── text_cleaner.py       # Text normalization class  
│   ├── feature_extractor.py  # TF-IDF vectorization  
│   ├── sentiment_model.py    # VADER sentiment classifier  
│   └── main.py               # End-to-end pipeline  
├── requirements.txt           # Project dependencies  
├── .gitignore                 # Files to ignore in Git  
├── PROJECT_OVERVIEW.md        # High-level project summary
├── USAGE.md                   # This usage guide
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd SentimentAnalyzer
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Sentiment Analyzer, execute the following command:
```
python src/main.py
```

This will analyze your input text and output whether the sentiment is positive or negative.

## Dependencies

- nltk
- scikit-learn
- pandas

All dependencies are listed in `requirements.txt`.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
