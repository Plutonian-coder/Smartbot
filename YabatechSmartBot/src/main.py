# src/main.py

import streamlit as st
from interface.ui_router import UIRouter

def main():
    """
    Main function to run the Streamlit application.
    This function initializes the UI router and renders the appropriate page.
    """
    st.set_page_config(page_title="Yabatech SmartBot", page_icon="🤖")

    # Initialize the UI router
    router = UIRouter()

    # Render the current page
    router.render_page()

if __name__ == "__main__":
    main()
