import pandas as pd
import os

def get_response(user_input):
    # Construct the absolute path to the CSV file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, '..', 'data', 'faq_sample.csv')

    # Load the FAQ dataset
    faq_df = pd.read_csv(file_path)

    # Simple keyword matching to find a response
    for index, row in faq_df.iterrows():
        if user_input.lower() in row['Intent'].lower():
            return row['Response']

    return "I'm sorry, I don't have an answer for that. Please try asking another question."
