# analytics/usage_stats.py

import pandas as pd
from src.config import CHAT_LOGS_PATH
import datetime

def log_interaction(user_query, bot_response, user_id="anonymous"):
    """
    Logs a single user-chatbot interaction to the chat_logs.csv file.

    Args:
        user_query (str): The query sent by the user.
        bot_response (str): The response from the chatbot.
        user_id (str, optional): A unique identifier for the user. Defaults to "anonymous".
    """
    log_entry = {
        'timestamp': [datetime.datetime.now()],
        'user_id': [user_id],
        'user_query': [user_query],
        'bot_response': [bot_response],
        'feedback_score': [None] # Placeholder for user feedback (e.g., 1 for good, -1 for bad)
    }

    try:
        df = pd.DataFrame(log_entry)
        # Append to the CSV file, creating it if it doesn't exist
        df.to_csv(CHAT_LOGS_PATH, mode='a', header=not pd.io.common.file_exists(CHAT_LOGS_PATH), index=False)
    except Exception as e:
        print(f"Error logging interaction: {e}")

def generate_usage_report():
    """
    Generates a simple usage report from the chat logs.
    """
    try:
        df = pd.read_csv(CHAT_LOGS_PATH)
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        total_interactions = len(df)
        unique_users = df['user_id'].nunique()

        print("--- Usage Statistics ---")
        print(f"Total Interactions: {total_interactions}")
        print(f"Unique Users: {unique_users}")

        if 'feedback_score' in df.columns:
            avg_feedback = df['feedback_score'].mean()
            print(f"Average Feedback Score: {avg_feedback:.2f}")

    except FileNotFoundError:
        print("Chat log file not found. No report can be generated.")
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

if __name__ == '__main__':
    # Example of logging an interaction
    # log_interaction("How do I pay school fees?", "You can pay via the student portal.")

    # Generate a report
    generate_usage_report()
