import streamlit as st
import cache
from Controllers.QueryFunctions import (find_movie, watch, end_watch, end_session)

def watch_movie_view() -> str:
    '''
    This view is to show the customer that they are watching a movie.

    This view has a text showing the title of the movie the customer is watching,
    a button to stop watching the movie, and a button to logout.

    When the stop watching button is clicked, the watch would be recorded in the
    watch table, the cached movie will be clear, and the view would return 'movie_search_view'.
    When the logout button is clicked, the view would stop the watch and store it in the
    table (just like the stop watching button), but will also clear the cache, store the
    session, and return 'login_view'.

    You may want to use end_watch(), end_session() functions.
    '''

    mid = cache.user.get_selected_mid()
    movie = find_movie(mid)
    st.title(f'You are watching {movie.get_title()}')

    start_time = watch(cache.session.get_sid(), cache.user.get_cid(), cache.user.get_selected_mid())
    
    if st.button('Stop watching'):
        end_watch(cache.session.get_sid(), cache.user.get_cid(), cache.user.get_selected_mid(), start_time)
        cache.user.set_selected_mid(None)
        cache.view = 'movie_search_view'
        st.experimental_rerun()
    
    if st.button('Logout'):
        end_watch(cache.session.get_sid(), cache.user.get_cid(), cache.user.get_selected_mid(), start_time)
        end_session(cache.session)
        cache.user = None
        cache.session = None
        cache.view = 'login_view'
        st.experimental_rerun()