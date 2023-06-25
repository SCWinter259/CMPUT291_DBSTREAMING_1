import streamlit as st
from Controllers.QueryFunctions import *

def register_view() -> str:
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