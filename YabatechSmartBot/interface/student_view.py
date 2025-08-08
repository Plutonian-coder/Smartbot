# interface/student_view.py

import streamlit as st
import pandas as pd
from src.config import STUDENT_DATA_PATH

def show_student_view():
    """
    Displays the student data view.
    Allows users to search and filter student information.
    """
    st.title("Student Information")

    try:
        df = pd.read_csv(STUDENT_DATA_PATH)

        st.write("Here you can search for students by name, department, or level.")

        # Search functionality
        search_term = st.text_input("Search by name, department, or level")

        if search_term:
            # A simple search across all columns
            result_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        else:
            result_df = df

        st.dataframe(result_df)

    except FileNotFoundError:
        st.error(f"Could not find the student data file at: {STUDENT_DATA_PATH}")
    except Exception as e:
        st.error(f"An error occurred while loading the student data: {e}")
