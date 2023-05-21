import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()


# Define a function for sentiment analysis
def analyze_sentiment(text):
    # Analyze the sentiment of the text
    sentiment = sia.polarity_scores(text)

    # Determine the sentiment label based on the compound score
    if sentiment['compound'] >= 0.05:
        sentiment_label = 'Positive'
    elif sentiment['compound'] <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    # Return the sentiment label
    return sentiment_label


# Test the sentiment analysis function for the sample text
sampleText = "I love this product! It works amazingly well."
sentiment = analyze_sentiment(sampleText)
print("Sample Text: I love this product! It works amazingly well.")
print("Sentiment:", sentiment)

# Test the sentiment analysis function for the user input text
inputText = input("\nEnter a text: ")
sentiment = analyze_sentiment(inputText)
print("Sentiment:", sentiment)
