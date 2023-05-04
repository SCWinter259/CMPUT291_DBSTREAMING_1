import sqlite3
from Controllers import config
from Controllers.SysStack import SysStack
from Controllers.Cache import Cache
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
    cache = Cache()
    #TODO: try to finish this part to test our system design
    system.control()

main()

# to recreate the database:
# sqlite3 [db name] < prj-tables.sql
# sqlite3 [db name] < project1_data.sql