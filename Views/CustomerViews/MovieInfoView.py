import streamlit as st
import cache
from Controllers.QueryFunctions import (find_cast, count_customer_watched, find_movie, end_session)
from Models.Customer import Customer

def movie_info_view() -> str:
    '''
    This view is for the customer to see imformation about the movie.

    This view has a back button, a watch movie button, a follow cast member button,
    a logout button.

    This view has to show the following information:
    - Movie title
    - Release year
    - Duration
    - List of names of cast members and their roles

    When the back button is clicked, the view returns 'movie_search_view'.
    When the watch movie button is clicked, the view caches the movie,
    then returns 'watch_movie_view'.
    When the follow cast member button is clicked, the view caches the cast
    member, then returns 'follow_cast_member_view'.
    When the logout button is clicked, the view reset the cache, log the user out,
    and returns 'login_view'.

    You may want to use find_cast(), count_customer_watched().
    '''
    st.title('Movie Information')

    # This part is for testing
    customer = Customer(cid='c100', name='Youssef Amer', pwd='ANGRY')
    cache.user = customer
    cache.user.set_selected_mid(10)
    # End of test
    mid = cache.user.get_selected_mid()
    movie = find_movie(mid)
    st.header(f'Movie title: {movie.get_title()}')
    for a, b in zip(['Release year', 'Duration', 'Cast members'], 
                    [movie.get_year(), movie.get_runtime(), '']):
        st.write(f'{a}: {b}')
    movie_people_lists = find_cast(mid)
    for movie_people_list in movie_people_lists:
        movie_people, role = movie_people_list
        st.write(f'{movie_people.get_name()}: {role}')

    if st.button('Follow cast member'):
        cache.user.set_sellected_pid(movie_people.get_pid())
        return 'follow_cast_member_view'
        
    st.write('Number of customers who have watched this movie:', str(count_customer_watched(movie)))
        
    if st.button('Watch movie'): return 'watch_movie_view'

    if st.button('Back'): return 'movie_search_view'

    if st.button('Logout'):
        end_session(cache.session)
        cache.user = None
        cache.session = None
        return 'login_view'