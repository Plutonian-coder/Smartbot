import streamlit as st
from PIL import Image
import os

# Set page configuration
st.set_page_config(
    page_title="Yabatech FAQ Bot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def main():
    # Construct absolute paths for assets
    dir_path = os.path.dirname(os.path.realpath(__file__))
    logo_path = os.path.join(dir_path, '..', 'assets', 'logo.png')
    image_path = os.path.join(dir_path, '..', 'assets', 'yabatech.jpg')

    # App title and description
    st.title("Yabatech FAQ Bot")

    # Display Yabatech logo
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=100)

    st.markdown("### Your Smart FAQ Assistant for Yabatech")

    # Display Yabatech image
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, use_column_width=True)

    st.markdown(
        """
        <div style="text-align: center; margin-top: 2rem;">
            <p>Get instant answers to your questions about Yabatech. Powered by AI, designed for students.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # "Start Chatting" button
    if st.button("Start Chatting"):
        # To navigate to the chat page, we can't directly call a function from another page.
        # Instead, we rely on Streamlit's multipage app structure.
        # The user will need to click on the "Chat" page in the sidebar.
        st.success("Please navigate to the Chat page from the sidebar to start chatting!")

if __name__ == "__main__":
    main()
