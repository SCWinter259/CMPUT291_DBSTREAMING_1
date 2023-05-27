import cache
from Models.Customer import Customer
from Models.Editor import Editor
from Controllers.QueryFunctions import *
# This view should contain login and sign up
def login_view() -> str:
    '''
    As a view, this function takes in the Cache object.
    This function takes user input, validate the input, update the cache, 
    and returns the string representing the appropriate function
    '''
    print("Welcome to DB_Streaming 1")
    print("Please enter the number of your choice:")
    print("0. Stop the program")
    print("1. Log in")
    print("2. Register a new customer account")
    
    # take the user input and validate
    choice = input("Enter your choice: ")
    choices = ["0", "1", "2"]
    while choice not in choices:
        choice = input("Invalid option. Please enter a valid option: ")

    if choice == "0":
        return "exit"
    elif choice == "1":
        uid = input("Enter your id: ")
        pwd = input("Enter your password: ")
        cache.user = find_user(uid, pwd)
        if cache.user == None:
            print("Your id and//or password is incorrect!")
            return "login_view"
        elif type(cache.user) is Customer:
            #TODO: set the session into the cache
            return "movie_search_view"
        elif type(cache.user) is Editor:
            return "general_editor_view"
    elif choice == "2":
        return "register_view"