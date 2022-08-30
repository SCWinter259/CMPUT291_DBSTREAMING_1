import sqlite3
import config
from Functions import*
from Customer import Customer
from Editor import Editor
from Movie import Movie
from MoviePeople import MoviePeople
from Session import Session

def get_path():
    #path = input("Please enter your path: ")
    path = "./test.db"
    return path

def connect(path):
    config.connection = sqlite3.connect(path)
    config.cursor = config.connection.cursor()
    config.cursor.execute(' PRAGMA foreign_keys=ON; ')
    config.connection.commit()

def main():
    path = get_path()
    connect(path)
    
    print("WELCOME TO DBSTREAMING_1!")
    # remember to have a back function
    # exit is only available when not logged in

    # while authorized == False (still in login screen)

    user = None
    while user == None:
        user = login_screen()
    # if user is customer
    if user.is_customer() == True:
        # TODO: start a session
        pass
    # if user is editor
    else:
        pass

    # try defining stage_code, indicating where the back() function might bring the user to
    # 1. 

main()