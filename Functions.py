import getpass
import config
#from main import connection, cursor
from Customer import Customer
from Editor import Editor
from Movie import Movie
from MoviePeople import MoviePeople
from Session import Session
from Cache import Cache

def executioner(func_name, cache_obj):
    '''
    Find the function name, execute the function. Find in arguments to see if the
    function takes parameter or not. If yes, it takes the cache object.
    '''
    functions = {
        "begin": begin,
        "login": login,
        "register": register,
        None: None
    }

    arguments = {
        "begin": False,
        "login": True,
        "register": False,
        None: None
    }

    if arguments[func_name] == True:
        print("debug 1")
        return functions[func_name](cache_obj)
    else:
        print("debug 2")
        return functions[func_name]()

def begin():
    '''
    First screen: user choose to login or register
    '''
    print("Enter 0 to exit")
    print("Enter 1 to login")
    print("Enter 2 to register")
    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting the program")
        exit()
    elif choice == "1":
        return "login"
    elif choice == "2":
        return "register"
    else:
        print("Invalid choice")
        return "begin"

def login(cache_obj):
    '''
    Second screen 1: promt user to login
    '''
    print("Login to your account")
    user_id = input("Please enter your ID: ")
    password = getpass.getpass("Enter your password: ")
    customer = find_customer(user_id, password)
    editor = find_editor(user_id, password)
    if customer != None:
        print("Welcome " + customer.get_name())
        cache_obj.set_user(customer)
        # TODO: return next function name
        return None
    elif editor != None:
        print("Welcome editor" + editor.get_eid())
        cache_obj.set_user(editor)
        # TODO: return next function name
        return None
    else:
        print("Sorry, we could not find such account")
        return "begin"

def register():
    '''
    Second screen 2: promt user to register
    '''
    pass

def login_screen():
    '''
    This function controls the login screen
    Return a customer object when logged in as customer, 
    an editor object when logged in as editor
    Return None if no one logged in (fail to authenticate or just registered)
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