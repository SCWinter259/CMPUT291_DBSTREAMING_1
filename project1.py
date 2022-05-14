import sqlite3
from login import login_screen
from search import search
from watch import start_watch, end_watch
from session import start_session, end_session

connection = None
cursor = None

def get_path(): #DONE
    path = input("Please enter your path: ")
    #path = "./project1.db"
    return path

def connect(path): #DONE
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()

def follow(cid, mid): #DONE
    '''
    Casper
    This is a detached function from search
    This function will insert data into follows table
    if the data is not duplicated
    '''
    global connection, cursor

    stop = False
    while stop == False:
        name = input("Enter the name of the cast member you want to follow: ")
        cursor.execute('''SELECT m.name 
                            FROM moviePeople m, casts c
                            WHERE m.pid = c.pid
                            AND c.mid =:mid''', 
                            {"mid":mid})
        all_cast = cursor.fetchall()
        
        for i in range(len(all_cast)):
            if all_cast[i][0] == name:
                stop = True
                break
        if stop == False:
            print("The person is not part of the cast member!")
    
    # find pid of movie person
    cursor.execute('''SELECT pid FROM moviePeople 
                        WHERE name =:name''',
                        {"name":name})
    person_id = cursor.fetchone()

    cursor.execute('''SELECT * FROM follows
                        WHERE cid =:cid AND pid =:pid''',
                        {"cid":cid, "pid":person_id[0]})
    followed = cursor.fetchall()
    if len(followed) == 0:
        cursor.execute('''INSERT INTO follows VALUES (:cid, :person_id)''',
                            {"cid":cid, "person_id":person_id[0]})
        connection.commit()
        print("Followed " + name + '!')
    else:
        print("You have already followed this person!")

def add_movie(): 
    '''
    Daniel
    This Function lets the editor add movies into the database. 
    The function uses SQL queries to find elements needed in the 
    database and queries are used to add  elements to the database.
    Parameter: None
    Return: None
    '''
    global connection, cursor

def update_recommendation():
    '''
    Daniel
    This Function will let the editor search and make 
    changes to the recommended list in the database.
    Parameter: None
    Return: None
    '''
    global connection, cursor

def main():
    path = get_path()
    connect(path)

    uid, choice = login_screen()

    # devide into different cases for customer and editor
    if choice == '1':   # customer
        logged_out = False
        while logged_out == False:
            session_start_time, sid = start_session(uid)
            session_status = True
            while session_status == True:
                mid = search()
                while 1:
                    print("Enter 1 to watch movie")
                    print("Enter 2 to follow a cast member")
                    customer_choice = input("Enter your option: ")
                    if customer_choice == '1':
                        movie_start_time = start_watch()
                        end_movie = input("Enter anything to end the movie: ")
                        if mid != None:
                            end_watch(sid, uid, mid, movie_start_time)
                        break
                    elif customer_choice == '2':
                        if mid != None:
                            follow(uid, mid)
                        break
                    else:
                        print("Invalid Input")
                while 1:
                    print("Enter 1 to end session")
                    print("Enter 2 to continue searching")
                    customer_choice = input("Enter your option: ")
                    if customer_choice == '1':
                        end_session(sid, mid, session_start_time)
                        session_status = False
                        break
                    elif customer_choice == '2':
                        break
                    else:
                        print("Invalid Input")
            customer_choice = input("Enter 0 to exit, any other key to continue: ")
            if customer_choice == '0':
                logged_out = True
    elif choice == '2':     # editor
        while 1:
            print("Enter 1 for adding movie")
            print("Enter 2 for updating recommendations")
            editor_choice = input("Enter your option: ")
            if editor_choice == '1':
                add_movie()
                break
            elif editor_choice == '2':
                update_recommendation()
                break
            else:
                print("Invalid Input")

    connection.commit()
    connection.close()

    # No hardcoding database name
    # Option to logout at any time
    # Option to exit program directly (plan: let it sit in the login screen)
    # Counter SQL injection

main()