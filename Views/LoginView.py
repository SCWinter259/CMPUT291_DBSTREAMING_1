import streamlit as st
import cache
from Models.Customer import Customer
from Models.Editor import Editor
from Controllers.QueryFunctions import *
# This view should contain login and sign up
def login_view() -> str:
    '''
    As a view, this function takes in the cache
    This function takes user input, validate the input, update the cache, 
    and returns the string representing the appropriate function
    '''

    st.title('Welcome to DB Streaming 1!')

    uid = st.text_input('ID:', 'Enter your ID')
    pwd = st.text_input('Password:', 'Enter your password')

    if st.button('Login'):
        cache.user = find_user(uid, pwd)
        if cache.user == None: st.warning('Incorrect ID or password')
        else: 
            session = start_session(cache.user)
            cache.session = session
            return 'movie_search_view'

    if st.button('Register a new customer account'): return 'register view'
    if st.button('Exit program'):
        st.write('Are you sure you want to exit the program?')
        if st.button('Yes'): return 'exit'
        if st.button('Cancel'): return 'login_view'

    # print("Welcome to DB_Streaming 1")
    # print("Please enter the number of your choice:")
    # print("0. Stop the program")
    # print("1. Log in")
    # print("2. Register a new customer account")
    
    # # take the user input and validate
    # choice = input("Enter your choice: ")
    # choices = ["0", "1", "2"]
    # while choice not in choices:
    #     choice = input("Invalid option. Please enter a valid option: ")

    # if choice == "0":
    #     return "exit"
    # elif choice == "1":
    #     uid = input("Enter your id: ")
    #     pwd = input("Enter your password: ")
    #     cache.user = find_user(uid, pwd)
    #     if cache.user == None:
    #         print("Your id and//or password is incorrect!")
    #         return "login_view"
    #     elif type(cache.user) is Customer:
    #         #TODO: set the session into the cache
    #         return "movie_search_view"
    #     elif type(cache.user) is Editor:
    #         return "general_editor_view"
    # elif choice == "2":
    #     return "register_view"