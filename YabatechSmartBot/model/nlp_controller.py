# model/nlp_controller.py

import pickle
import pandas as pd
import os
from src.config import NLP_MODEL_PATH, FAQ_DATA_PATH

# Load the trained model and FAQ data once when the module is imported
model = None
try:
    # Check if the model file exists and is not empty
    if os.path.exists(NLP_MODEL_PATH) and os.path.getsize(NLP_MODEL_PATH) > 0:
        with open(NLP_MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
    else:
        print(f"Warning: Model file not found or is empty at {NLP_MODEL_PATH}.")
        print("Please run train_nlp_model.py to create the model file.")
except (FileNotFoundError, EOFError) as e:
    print(f"Warning: Could not load model file. Error: {e}")
    print("Please run train_nlp_model.py to create the model file.")

try:
    faq_df = pd.read_csv(FAQ_DATA_PATH).set_index('Intent')
except FileNotFoundError:
    faq_df = None
    print(f"Warning: FAQ data not found at {FAQ_DATA_PATH}.")


def get_bot_response(user_query):
    """
    Generates a response to a user's query.

    Args:
        user_query (str): The question from the user.

    Returns:
        str: The chatbot's response.
    """
    if not model or faq_df is None:
        return "I'm sorry, my knowledge base is currently unavailable. Please contact an administrator."

    try:
        # Use the trained model to predict the intent of the user's query
        predicted_intent = model.predict([user_query])[0]

        # Retrieve the corresponding response from the FAQ dataframe
        response = faq_df.loc[predicted_intent, 'Response']

        return response

    except KeyError:
        # If the predicted intent is not found in the FAQ (which shouldn't happen if trained correctly)
        return "I'm not sure how to answer that. Could you try rephrasing your question?"
    except Exception as e:
        print(f"An error occurred while generating a response: {e}")
        return "I'm sorry, I encountered an error. Please try again later."

if __name__ == '__main__':
    # Example usage
    test_query = "how to pay fees"
    response = get_bot_response(test_query)
    print(f"Query: '{test_query}'")
    print(f"Response: '{response}'")

    test_query_2 = "how do I apply?"
    response_2 = get_bot_response(test_query_2)
    print(f"\nQuery: '{test_query_2}'")
    print(f"Response: '{response_2}'")
