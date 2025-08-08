# interface/faq_view.py

import streamlit as st
import pandas as pd
from src.config import FAQ_DATA_PATH
from model.nlp_controller import get_bot_response

def show_faq_view():
    """
    Displays the FAQ and chatbot interface.
    """
    st.title("Frequently Asked Questions & Chat")

    try:
        faq_df = pd.read_csv(FAQ_DATA_PATH)

        # Display FAQs in an expander
        with st.expander("View all FAQs"):
            for _, row in faq_df.iterrows():
                st.markdown(f"**Q: {row['Intent']}**")
                st.markdown(f"A: {row['Response']}")
                st.markdown("---")

    except FileNotFoundError:
        st.warning("FAQ data not found. The chatbot will rely solely on its trained model.")
    except Exception as e:
        st.error(f"An error occurred loading FAQs: {e}")

    # Chatbot interface
    st.markdown("### Ask me anything!")

    user_input = st.text_input("Your question:", key="user_question")

    if user_input:
        # Get response from the NLP controller
        bot_response = get_bot_response(user_input)

        # Display conversation
        st.markdown("**You:**")
        st.info(user_input)
        st.markdown("**Bot:**")
        st.success(bot_response)

        # Placeholder for logging chat history and feedback
        # log_chat(user_input, bot_response)
        # show_feedback_options()
