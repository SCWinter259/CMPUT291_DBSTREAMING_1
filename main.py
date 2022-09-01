import sqlite3
from Cache import Cache
import config
from Functions import*
from SysStack import SysStack
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

    stack = SysStack()
    frame = "begin"
    cache_obj = Cache()
    stack.control(frame)
    
    while(stack.peek() != None):
        print(stack.see_stack())
        frame = executioner(frame, cache_obj)
        # ask user if they want to go back
        # we have to guarantee that a logged in user can't simply go back. They have to logout.
        if len(stack.see_stack()) > 3:
            decision = input("Do you want to go back? Enter 'y' to go back, any other character to continue: ")
            if decision == "y":
                stack.remove()
                frame = stack.peek()
        stack.control(frame)
    print("None returned. No next frame.")

main()

# to recreate the database:
# sqilte3 [db name] < prj-tables.sql
# sqlite3 [db name] < project1_data.sql