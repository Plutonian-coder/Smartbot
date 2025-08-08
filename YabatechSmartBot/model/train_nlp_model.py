# model/train_nlp_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle
from src.config import FAQ_DATA_PATH, NLP_MODEL_PATH

def train_model():
    """
    A sample function to train a simple NLP model based on the FAQ data.
    This model will predict an 'Intent' based on user input.
    """
    try:
        # Load data
        df = pd.read_csv(FAQ_DATA_PATH)

        # Ensure data is clean (no missing values in training columns)
        df.dropna(subset=['Intent', 'Keywords'], inplace=True)

        # Features (X) and Labels (y)
        X = df['Keywords'] # Using keywords for simplicity, could also use 'Intent' text
        y = df['Intent']

        # Create a simple text classification pipeline
        # 1. TfidfVectorizer: Converts text to a matrix of TF-IDF features.
        # 2. MultinomialNB: A Naive Bayes classifier suitable for text classification.
        model_pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', MultinomialNB())
        ])

        print("Training model...")
        # Train the model
        model_pipeline.fit(X, y)

        print(f"Model training complete. Saving model to {NLP_MODEL_PATH}")

        # Save the trained model to a file
        with open(NLP_MODEL_PATH, 'wb') as f:
            pickle.dump(model_pipeline, f)

        print("Model saved successfully.")

    except FileNotFoundError:
        print(f"Error: FAQ data file not found at {FAQ_DATA_PATH}")
    except Exception as e:
        print(f"An error occurred during model training: {e}")

if __name__ == '__main__':
    train_model()
