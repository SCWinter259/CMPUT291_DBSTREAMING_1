import getpass

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
            print("Welcome " + customer[1])
            # TODO
        elif editor != None:
            print("Welcome editor" + editor[0])
            # TODO
        else:
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
    Return all customer info if customer exists, None otherwise
    '''
    global connection, cursor

    cursor.execute("SELECT cid FROM customers WHERE cid=:id AND pwd=:pass",
                            {"id":cid, "pass":pwd})
    user = cursor.fetchone()
    if user != None:
        return user
    else:
        return None

def find_editor(eid, pwd):
    '''
    Find in table "editors" using eid and pwd
    Return all editor info if editor exists, None otherwise
    '''
    global connection, cursor

    cursor.execute("SELECT cid FROM customers WHERE cid=:id AND pwd=:pass",
                            {"id":eid, "pass":pwd})
    user = cursor.fetchone()
    if user != None:
        return user
    else:
        return None