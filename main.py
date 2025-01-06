# Importing TextBlob
from textblob import TextBlob


# Function to analyze sentiment of a sentence
def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    # Get sentiment (polarity and subjectivity)
    sentiment = blob.sentiment
    return sentiment


# Sample text; Modify as needed for a simple sentence
sentence = "Have a great day!"

# Analyze the sentiment of the sentence
sentiment = analyze_sentiment(sentence)

# Print the sentiment result
print(f"Sentiment of the sentence: {sentence}")
print(
    f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
#hit "RUN" to return a score with Subjectivity and Polarity 
