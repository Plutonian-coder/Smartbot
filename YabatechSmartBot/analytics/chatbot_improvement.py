# analytics/chatbot_improvement.py

import pandas as pd
from src.config import CHAT_LOGS_PATH

def analyze_poor_responses():
    """
    Analyzes chat logs to identify conversations with poor sentiment
    or where the chatbot failed to provide a useful response.

    This is a placeholder for a more sophisticated analysis.
    """
    try:
        chat_logs_df = pd.read_csv(CHAT_LOGS_PATH)

        # Example: Filter for logs where user feedback was negative
        # This assumes a 'feedback_score' column exists in chat_logs.csv
        if 'feedback_score' in chat_logs_df.columns:
            poor_responses = chat_logs_df[chat_logs_df['feedback_score'] < 0]

            if not poor_responses.empty:
                print("Found poorly rated responses:")
                print(poor_responses)
                # In a real scenario, you might save this to a file or a dashboard
                return poor_responses
            else:
                print("No poorly rated responses found.")
                return None
        else:
            print("Chat logs do not contain feedback scores for analysis.")
            return None

    except FileNotFoundError:
        print(f"Chat log file not found at {CHAT_LOGS_PATH}")
        return None
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
        return None

if __name__ == '__main__':
    # This allows running the analysis script directly
    analyze_poor_responses()
