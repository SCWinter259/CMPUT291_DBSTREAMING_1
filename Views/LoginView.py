import streamlit as st
import cache
from Controllers.QueryFunctions import *
# This view should contain login and sign up
def login_view() -> str:
    '''
    As a view, this function takes in the cache
    This function takes user input, validate the input, update the cache, 
    and returns the string representing the appropriate function
    '''

    st.title('Welcome to DB Streaming 1!')

    uid = st.text_input(label='ID')
    pwd = st.text_input(label='Password', type='password')

    uid = uid.strip()
    pwd = pwd.strip()

    if st.button('Login'):
        cache.user = find_user(uid, pwd)
        if cache.user == None: st.warning('Incorrect ID or password')
        else: 
            session = start_session(cache.user)
            cache.session = session
            return 'movie_search_view'

    if st.button('Register a new customer account'): return 'register view'