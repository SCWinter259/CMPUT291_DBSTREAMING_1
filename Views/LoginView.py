import streamlit as st
import cache
from Controllers.QueryFunctions import (find_user, start_session)
import time
# This view should contain login and sign up
def login_view() -> None:
    '''
    This view is for a customer login.

    Requirements for a user to login:
    - The entered ID should be an ID either in customers or editors table.
    - The entered password should be matching with the given ID.

    This view has a text field for ID, a text field for password, a button for login, and
    a button for registering a new customer account.

    If the user chooses to register a new customer account, the view will return "register_view".
    If the login button is clicked, and the entered credentials are invalid, a warning
    should be shown. If the credentials are valid, a session should be started in the sessions
    table, a Session object and a Customer or Editor object should be cached. The view
    would return "movie_search_view" if the user is a customer, and 'general_editor_view' 
    if the user is an editor.

    You may want to use find_user() and start_session() functions.
    '''
    st.title('Welcome to DB Streaming 1!')

    uid = st.text_input(label='ID')
    pwd = st.text_input(label='Password', type='password')

    uid = uid.strip()
    pwd = pwd.strip()

    if st.button('Login'):
        user = find_user(uid, pwd)
        cache.user = user
        if user == None: 
            st.warning('Incorrect ID or password')     # failed login
            time.sleep(1)
        elif user.is_customer():
            session = start_session(cache.user)
            cache.session = session
            cache.view = 'movie_search_view'
        else:
            cache.view = 'general_editor_view'
        st.experimental_rerun()

    if st.button('Register a new customer account'): 
        cache.view = 'register_view'
        st.experimental_rerun()