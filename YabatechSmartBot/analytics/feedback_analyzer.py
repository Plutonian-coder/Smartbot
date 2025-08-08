# analytics/feedback_analyzer.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text using VADER.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing the sentiment scores (pos, neu, neg, compound).
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    return sentiment_scores

def get_sentiment_label(text):
    """
    Provides a simple sentiment label (Positive, Negative, Neutral) for a text.

    Args:
        text (str): The text to classify.

    Returns:
        str: The sentiment label.
    """
    scores = analyze_sentiment(text)
    # The compound score is a metric that calculates the sum of all lexicon ratings
    # which have been standardized to be between -1 (most extreme negative) and +1 (most extreme positive).
    if scores['compound'] >= 0.05:
        return "Positive"
    elif scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if __name__ == '__main__':
    # Example usage
    sample_feedback_positive = "This chatbot is amazing and so helpful!"
    sample_feedback_negative = "I couldn't find what I was looking for, it's very frustrating."

    print(f"Feedback: '{sample_feedback_positive}'")
    print(f"Sentiment: {get_sentiment_label(sample_feedback_positive)}")
    print(f"Scores: {analyze_sentiment(sample_feedback_positive)}")

    print("\n" + "-"*20 + "\n")

    print(f"Feedback: '{sample_feedback_negative}'")
    print(f"Sentiment: {get_sentiment_label(sample_feedback_negative)}")
    print(f"Scores: {analyze_sentiment(sample_feedback_negative)}")
