import getpass

def login_screen(): #DONE
    '''
    Casper
    1. Provide both options for customers and editors to login
    2. Detect whether it's a customer or editor?
    3. Unregistered customers should be able to sign up
    '''
    global connection, cursor

    authorized = False
    user = None
    # Loop till successful login
    while authorized == False:
        # Loop till user identify as user or customer or user exit
        begin = False
        while begin == False:
            print("Enter 0 to exit the program")
            print("Enter 1 to login as a customer")
            print("Enter 2 to login as an editor")
            print("Enter 3 to sign up as a customer")
            choice = input("Enter your choice: ")
            if choice == '0':
                quit()
            elif choice == '1' or choice == '2':
                begin = True
            elif choice == '3':
                sign_up()   # sign up new customer account
            else:
                print("Invalid input")

        user_id = input("Enter your ID: ")
        password = getpass.getpass("Enter your password: ")

        if choice == '1':       # login as customer
            cursor.execute("SELECT cid FROM customers WHERE cid=:id AND pwd=:pass",
                            {"id":user_id, "pass":password})
            user = cursor.fetchone()
            if user != None:
                authorized = True
        elif choice == '2':     # login as editor
            cursor.execute("SELECT eid FROM editors WHERE eid=:id AND pwd=:pass",
                            {"id":user_id, "pass":password})
            user = cursor.fetchone()
            if user != None:
                authorized = True

        if authorized == False:
            print("Invalid ID or password")
    
    print("Login successfully! Welcome user " + user[0])

    return user[0], choice

def sign_up(): #DONE
    '''
    Casper
    This is a helper function for login_screen
    This function is for registering new accounts
    '''
    global connection, cursor

    reg_status = False
    # Loop until user wants to go back or account registed succesfully
    while reg_status == False:
        print("Enter 0 to go back")
        print("Enter 1 to register as a customer")
        choice = input("Enter your choice: ")

        if choice != '0' and choice != '1':
            print("Invalid input")
        elif choice == '0':
            return
        elif choice == '1':
            valid = False
            # Loop until the ID is valid
            while valid == False:
                user_id = input("Enter your ID: ")
                # Search to find duplicate id in customers
                cursor.execute("SELECT cid FROM customers WHERE cid=:id",
                                {"id":user_id})
                user1 = cursor.fetchone()
                # Search to find duplicate id in editors
                cursor.execute("SELECT eid FROM editors WHERE eid=:id",
                                {"id":user_id})
                user2 = cursor.fetchone()

                if len(user_id) <= 4 and user1 == None and user2 == None:
                    valid = True
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")
                    cursor.execute("INSERT INTO customers VALUES (:id, :name, :pass)",
                                    {"id":user_id, "name":name, "pass":password})
                    connection.commit()
                    print("Customer " + user_id + " registered successfully")
                    reg_status = True
                elif len(user_id) > 4:
                    print("Please use 4 characters or less")
                elif user1 != None or user2 != None:
                    print("The ID has been taken! PLease choose a different ID")