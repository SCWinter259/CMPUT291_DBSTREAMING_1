import streamlit as st
from Controllers.QueryFunctions import (find_customer, find_editor, register_customer)

def register_view() -> str:
    '''
    This view is for registering a new customer account.

    Requirements for a new customer account:
    - ID should not be a registered ID and should be at most four characters long.
    - ID, password, and username should not be empty.

    This view has a text field for ID, a text field for username, a text field for password,
    and a button to register.

    When customer hits register button, a warning will come up if the user's information
    does not meet the requirements. 

    If registration is successful, a new customer should be added into the database, 
    and the view will return 'login_view'.

    You may want to use find_customer(), find_editor(), and register_customer() functions.
    '''
    st.title('Register new account')

    uid = st.text_input(label='ID')
    name = st.text_input(label='Username')
    pwd = st.text_input(label='Password', type='password')

    uid = uid.strip()
    name = name.strip()
    pwd = pwd.strip()

    if st.button('Register'):
        if find_customer(uid) != None or find_editor(uid) != None: 
            st.warning('Please choose a different ID. This one is already registerd')
        elif len(uid) == 0 or len(name) == 0 or len(pwd) == 0:
            st.warning(
                '''
                Invalid ID, password, or Username!

                A valid ID, password, or Username is one that contains characters, not just white space.
                '''
            )
        else:
            register_customer(uid, name, pwd)
            return "login_view"