# interface/login_view.py

import streamlit as st

def show_login_view():
    """
    Displays the login page.
    In a real application, this would handle user authentication.
    """
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Placeholder for authentication logic
        if username and password:
            st.session_state['logged_in'] = True
            st.session_state['page'] = 'faq'  # Redirect to FAQ page after login
            st.success("Logged in successfully!")
            # This will trigger a re-run, and the router will pick the new page
            st.experimental_rerun()
        else:
            st.error("Please enter both username and password.")

    # In a real app, you might have options for "Forgot Password" or "Sign Up"
    st.info("This is a placeholder login. Any username/password will work.")
