import streamlit as st
import cache
from Controllers.QueryFunctions import *
# This view should contain login and sign up
def login_view() -> str:
    '''
    This view shows a text field for ID and a text field for password (for login purposes).
    There is a button for login and a button for register new account.
    If login button is pressed, the entered ID and password would be evaluated.
        If login failed, a warning should be shown.
        If login successfully, the appropriate Customer or Editor object should be cached.
            If the user is a customer, a session should be started and cached, then return "movie_search_view"
            If the user is an editor, return "general_editor_view"
    '''

    st.title('Welcome to DB Streaming 1!')

    uid = st.text_input(label='ID')
    pwd = st.text_input(label='Password', type='password')

    uid = uid.strip()
    pwd = pwd.strip()

    if st.button('Login'):
        user = find_user(uid, pwd)
        if user == None: st.warning('Incorrect ID or password')     # failed login
        else:   # successful login
            cache.user = user
            if cache.user.is_customer():    # if it is customer
                session = start_session(cache.user)
                cache.session = session
                return 'movie_search_view'
            else:       # if it is editor
                return 'general_editor_view'

    if st.button('Register a new customer account'): return 'register_view'