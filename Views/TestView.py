import streamlit as st
from Controllers.QueryFunctions import *

def test_view() -> str:
    '''
    Casper
    This view is for test writes.
    Currently testing query functions for movie search view
    '''
    text = st.text_input(label="Search for a movie")

    if st.button("Search"):
        results = search(text)
        if len(results) == 0:
            st.write("Sorry, we found no result.")
        else:
            for movie in results:
                st.subheader(movie.get_title())
                st.write(movie.get_year())
                st.write(movie.get_runtime())