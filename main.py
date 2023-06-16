import sqlite3
import config
import all_views
import streamlit as st
from Controllers.SysStack import SysStack
from Views.LoginView import login_view

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

    system = SysStack()
    frame = "login_view"
    system.control(frame)
    print(system.see_stack())

    while system.peek() != None and system.peek() != 'exit':
        print(system.peek())
        frame = all_views.views[system.peek()]
        next_frame = frame()
        system.control(next_frame)

    st.stop()

main()

# to recreate the database:
# sqlite3 [db name] < prj-tables.sql
# sqlite3 [db name] < project1_data.sql