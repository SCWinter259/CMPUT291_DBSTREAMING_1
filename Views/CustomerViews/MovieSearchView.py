import streamlit as st
import cache
from Controllers.QueryFunctions import (search, end_session)

def movie_search_view() -> str:
    '''
    This view is for the customer to search for a movie.

    This view has a text field which serves as a search bar, a search button, and a logout
    button.

    All requirements for searching and string matching in this view are taken care of by the
    search engine written in the QueryFunctions file. 

    When the search button is clicked, if there is no result, this view should display a
    message accordingly. If there are results, they should be displayed 5 items at a time,
    along with a button saying 'Show more results'. When this button is clicked, 5 more
    results will be displayed (if there are less than 5 more, display all results that are 
    left to display). This button should only appear if there are more results left.

    Each of the result should be displayed with its title, year, duration, and a button
    saying 'More information'. When this button is clicked, the view should cache
    the chosen movie (into Customer object) and return 'movie_info_view'.

    If the logout button is clicked, the view should clear the cache, log the user out, and
    return 'login_view'.

    You may want to use search(), end_session() functions.
    '''
    st.title('Search for a movie')

    if st.button('Logout'):
        end_session(cache.session)
        cache.user = None
        cache.session = None
        cache.view = 'login_view'
        st.experimental_rerun()

    text = st.text_input(label='Seach for a movie')

    if st.session_state.get('search_button') != True:
        st.session_state.search_button = st.button('Search')

    if st.session_state.get('search_button') == True:
        movie_list = search(text)
        if len(movie_list) == 0: st.write('No results found.')
        else:
            for movie in movie_list:
                st.header(movie.get_title())
                st.write('Release year:', movie.get_year())
                st.write('Duration:', movie.get_runtime())
                if st.button(key=movie.get_mid(), label='More information'):
                    cache.user.set_selected_mid(movie.get_mid())
                    cache.view = 'movie_info_view'
                    st.experimental_rerun()