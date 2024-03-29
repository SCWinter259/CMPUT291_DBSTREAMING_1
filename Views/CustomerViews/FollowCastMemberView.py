import streamlit as st
import cache
from Controllers.QueryFunctions import (find_movie, find_cast, follow, end_session)

def follow_cast_member_view() -> None:
    '''
    This view is for the user to choose a cast member to follow.

    This view has a back button, a logout button, and for each
    cast member, there is a follow button for each cast member.

    Follow button should be labeled "follow xxx" with xxx being the
    name of the cast member. When the follow button is clicked, there
    should be a notification that the user has successfully followed
    the cast member, or that the user has already followed the cast
    member.

    When the back button is clicked, the view returns 'movie_info_view'.
    When the logout button is clicked, the view reset the cache, log the user out,
    and returns 'login_view'.

    You may want to use follow() and streamlit toast component (for the
    follow notification).
    '''

    st.title('Follow cast member')
    
    mid = cache.user.get_selected_mid()
    movie = find_movie(mid)
    st.header(f'Movie title: {movie.get_title()}')

    st.subheader('Choose a cast member to follow')
    movie_people_lists = find_cast(mid)
    for movie_people_list in movie_people_lists:
        movie_people, role = movie_people_list
        if st.button(key=movie_people.get_pid(), label=f'Follow {movie_people.get_name()}'):
            if follow(cache.user.get_cid(), movie_people.get_pid()):
                st.toast(f'You have successfully followed {movie_people.get_name()}!')
            else:
                st.toast(f'You have already followed {movie_people.get_name()}!')

    if st.button('Back'): 
        cache.view = 'movie_info_view'
        st.experimental_rerun()

    if st.button('Logout'):
        end_session(cache.session)
        cache.user = None
        cache.session = None
        st.session_state.search_button = False
        cache.view = 'login_view'
        st.experimental_rerun()