# interface/ui_router.py

import streamlit as st
from interface.login_view import show_login_view
from interface.faq_view import show_faq_view
from interface.student_view import show_student_view
from interface.staff_view import show_staff_view
from src.config import LOGO_PATH, APP_TITLE

class UIRouter:
    """
    Handles page routing and navigation for the Streamlit application.
    """

    def __init__(self):
        # Initialize session state variables if they don't exist
        if 'page' not in st.session_state:
            st.session_state['page'] = 'login'
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False

    def render_sidebar(self):
        """Renders the navigation sidebar."""
        with st.sidebar:
            # st.image(LOGO_PATH, width=100) # Uncomment when you have a logo
            st.title(APP_TITLE)

            if st.session_state['logged_in']:
                st.button("Chatbot / FAQ", on_click=self.navigate_to, args=('faq',))
                st.button("Student Info", on_click=self.navigate_to, args=('student',))
                st.button("Staff Info", on_click=self.navigate_to, args=('staff',))
                st.button("Logout", on_click=self.logout)

    def render_page(self):
        """Renders the currently selected page."""
        self.render_sidebar()

        if not st.session_state['logged_in']:
            show_login_view()
        else:
            page = st.session_state['page']
            if page == 'faq':
                show_faq_view()
            elif page == 'student':
                show_student_view()
            elif page == 'staff':
                show_staff_view()
            else:
                show_faq_view() # Default to FAQ page

    def navigate_to(self, page_name):
        """Callback function to switch pages."""
        st.session_state['page'] = page_name

    def logout(self):
        """Logs the user out and returns to the login page."""
        st.session_state['logged_in'] = False
        st.session_state['page'] = 'login'
        # No need for experimental_rerun here, Streamlit handles the state change
