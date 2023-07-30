import sqlite3
import config
import all_views
import streamlit as st
from Controllers.SysStack import SysStack

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

    # UNCOMMENT THIS PART FOR ACTUAL PROGRAM

    # system = SysStack()
    # frame = "login_view"
    # system.control(frame)
    # print(system.see_stack())

    # while system.peek() != None and system.peek() != 'exit':
    #     frame = all_views.views[system.peek()]
    #     next_frame = frame()
    #     system.control(next_frame)

    # END

    # THIS PART IS FOR TESTING!!! COMMENT OUT IF YOU WANT THE ACTUAL PROGRAM

    # frame = "test_view"
    frame = 'movie_search_view'
    frame = all_views.views[frame]
    next_frame = frame()
    print(next_frame)

main()

# to recreate the database:
# sqlite3 [db name] < prj-tables.sql
# sqlite3 [db name] < project1_data.sql