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
    
    while(stack.see_stack() != None):
        stack.control(frame)
        print(stack.see_stack())
        frame = executioner(frame, cache_obj)

main()