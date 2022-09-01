import getpass
import config
#from main import connection, cursor
from Customer import Customer
from Editor import Editor
from Movie import Movie
from MoviePeople import MoviePeople
from Session import Session
from Cache import Cache

# functions that control the program on the whole
def executioner(func_name, cache_obj):
    '''
    Find the function name, execute the function. Find in arguments to see if the
    function takes parameter or not. If yes, it takes the cache object.
    '''
    functions = {
        "begin": begin,
        "login": login,
        "register": register,
        "customer screen": customer_screen,
        "editor screen": editor_screen,
        None: None
    }

    arguments = {
        "begin": False,
        "login": True,
        "register": False,
        "customer screen": True,
        "editor screen": True,
        None: None
    }

    if arguments[func_name] == True:
        return functions[func_name](cache_obj)
    else:
        return functions[func_name]()

# frame functions
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
        # start the session
        # TODO: return next function name
        return "customer screen"
    elif editor != None:
        print("Welcome editor" + editor.get_eid())
        cache_obj.set_user(editor)
        # TODO: return next function name
        return "editor screen"
    else:
        print("Sorry, we could not find such account")
        return "begin"

def register():
    '''
    Second screen 2: promt user to register
    '''
    print("Register account")
    user_id = input("Please enter your ID: ")
    password = input("Enter your password: ")
    if find_customer(user_id, None) != None:
        print("This user ID has already existed. Please choose a different one")
        return "register"
    elif len(user_id) > 4:
        print("Your ID cannot exceed 4 characters!")
        return "register"
    else:
        name = input("Please enter your name: ")
        insert_customer(user_id, name, password)
        return "begin"

def customer_screen(cache_obj):
    '''
    First screen for customers when logged in
    '''
    return None

def editor_screen(cache_obj):
    '''
    First screen for editors when logged in
    '''
    return None

# below are support functions
def find_customer(cid, pwd):
    '''
    Find in table "customers" using cid and pwd
    Return customer object if customer exists, None otherwise
    '''
    if pwd != None:     # find customer using both cid and pwd
        config.cursor.execute("SELECT * FROM customers WHERE cid=:id AND pwd=:pass",
                                {"id":cid, "pass":pwd})
    else:       # find customer using only cid
        config.cursor.execute("SELECT * FROM customers WHERE cid=:id",
                            {"id":cid})
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
    if pwd != None:     # find editor using both eid and pwd
        config.cursor.execute("SELECT * FROM editors WHERE eid=:id AND pwd=:pass",
                                {"id":eid, "pass":pwd})
    else:       # find editor using only eid
        config.cursor.execute("SELECT * FROM editors WHERE eid=:id",
                                {"id":eid})
    user = config.cursor.fetchone()
    if user != None:
        editor = Editor()
        editor.set_eid(user[0])
        editor.set_pwd(user[1])
        return editor
    else:
        return None

def insert_customer(cid, name, pwd):
    '''
    A function to add new customer into the database
    Does not return anything
    '''
    config.cursor.execute("INSERT INTO customers VALUES (:id, :name, :pass)",
                                    {"id":cid, "name":name, "pass":pwd})
    config.connection.commit()
    print("Customer " + cid + " registered successfully")