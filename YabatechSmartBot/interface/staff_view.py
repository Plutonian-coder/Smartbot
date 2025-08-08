# interface/staff_view.py

import streamlit as st
import pandas as pd
from src.config import STAFF_INFO_PATH

def show_staff_view():
    """
    Displays the staff data view.
    Allows users to search and filter staff information.
    """
    st.title("Staff Information")

    try:
        df = pd.read_csv(STAFF_INFO_PATH)

        st.write("Here you can search for staff members by name or department.")

        # Search functionality
        search_term = st.text_input("Search by name, department, or role")

        if search_term:
            # A simple search across all columns
            result_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        else:
            result_df = df

        st.dataframe(result_df)

    except FileNotFoundError:
        st.error(f"Could not find the staff data file at: {STAFF_INFO_PATH}")
    except Exception as e:
        st.error(f"An error occurred while loading the staff data: {e}")
