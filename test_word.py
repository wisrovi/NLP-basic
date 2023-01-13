from textblob import TextBlob,Word # pip install textblob
import nltk
nltk.download('punkt')

def sentiment(text):
    blob = TextBlob(text)
    blob_sentiment,blob_subjectivity = blob.sentiment.polarity ,blob.sentiment.subjectivity
    return blob_sentiment, blob_subjectivity

print(sentiment('I hate the person who is reading this'))
print(sentiment('I love my family'))
print(sentiment("I'm sad because I'm alone"))