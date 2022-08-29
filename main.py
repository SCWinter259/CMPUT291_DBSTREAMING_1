import sqlite3
from Functions import*

connection = None
cursor = None

def get_path():
    #path = input("Please enter your path: ")
    path = "./test.db"
    return path

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()

def main():
    print("WELCOME TO DBSTREAMING_1!")
    # remember to have a back function
    # exit is only available when not logged in

    # while authorized == False (still in login screen)

    user = None
    while user == None:
        user = login_screen()
    # 2 cases when escaped the login screen
        # Customer case
        # Editor case