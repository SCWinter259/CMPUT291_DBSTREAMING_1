import streamlit as st
from Controllers.QueryFunctions import *

def test_view() -> str:
    '''
    Casper
    This view is for test writes.
    '''
    # TESTING MOVIE SEARCH VIEW  

    # text = st.text_input(label="Search for a movie")

    # if st.button("Search"):
    #     results = search(text)
    #     if len(results) == 0:
    #         st.write("Sorry, we found no result.")
    #     else:
    #         for movie in results:
    #             st.subheader(movie.get_title())
    #             st.write(movie.get_year())
    #             st.write(movie.get_runtime())

    # TESTING FIND CAST QUERY FUNCTION
    cast = find_cast(10)
    for [member, role] in cast:
        st.subheader(member.get_name())
        st.write(member.get_birthYear())
        st.write(role)