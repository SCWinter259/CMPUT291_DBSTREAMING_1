import getpass
import config
#from main import connection, cursor
from Customer import Customer
from Editor import Editor
from Movie import Movie
from MoviePeople import MoviePeople
from Session import Session

def back(stage_code):
    '''
    Changes the stage code of the function it's running in. The function itself has
    to redirect the user according to the stage code
    '''
    return stage_code - 1

def next(stage_code):
    '''
    Similar to back, but increment the stage code
    '''
    return stage_code + 1

def login_screen():
    '''
    This function controls the login screen
    Return a customer object when logged in as customer, 
    an editor object when logged in as editor
    Return None if no one logged in (fail to authenticate or just registered)
    Stage code: 
    1. The promt where user choose to login or register
    2. Either the login part or signup part
    '''
    print("Enter 0 to exit")
    print("Enter 1 to login")
    print("Enter 2 to register")
    choice = input("Enter your choice: ")
    
    if choice == "0":       # Exit the program
        print("Exiting the program")
        exit()
    elif choice == "1":     # login
        print("Login to your account")
        user_id = input("Please enter your ID: ")
        password = getpass.getpass("Enter your password: ")
        customer = find_customer(user_id, password)
        editor = find_editor(user_id, password)
        if customer != None:
            print("Welcome " + customer.get_name())
            return customer
        elif editor != None:
            print("Welcome editor" + editor.get_eid())
            return editor
        else:
            print("Sorry, we could not find such account")
            return None
    elif choice == "2":     # Register
        print("Register account")
        user_id = input("Please enter your ID: ")
        password = input("Enter your password: ")
        # TODO
    else:       # invalid input
        print("Please enter a valid choice")
        return None

def find_customer(cid, pwd):
    '''
    Find in table "customers" using cid and pwd
    Return customer object if customer exists, None otherwise
    '''
    config.cursor.execute("SELECT * FROM customers WHERE cid=:id AND pwd=:pass",
                            {"id":cid, "pass":pwd})
    user = config.cursor.fetchone()
    if user != None:
        customer = Customer()
        customer.set_cid(user[0])
        customer.set_name(user[1])
        customer.set_pwd(user[2])
        return customer
    else:
        return None

def find_editor(eid, pwd):
    '''
    Find in table "editors" using eid and pwd
    Return editor object if editor exists, None otherwise
    '''
    config.cursor.execute("SELECT * FROM editors WHERE eid=:id AND pwd=:pass",
                            {"id":eid, "pass":pwd})
    user = config.cursor.fetchone()
    if user != None:
        editor = Editor()
        editor.set_eid(user[0])
        editor.set_pwd(user[1])
        return editor
    else:
        return None