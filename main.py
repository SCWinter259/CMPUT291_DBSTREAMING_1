import sqlite3
import config
import all_views
import cache

def get_path():
    path = "./data/test.db"
    return path

def connect(path):
    config.connection = sqlite3.connect(path)
    config.cursor = config.connection.cursor()
    config.cursor.execute(' PRAGMA foreign_keys=ON; ')
    config.connection.commit()

def main():
    path = get_path()
    connect(path)    

    frame = cache.view
    
    all_views.views[frame]()

main()