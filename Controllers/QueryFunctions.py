from Controllers import config
from Models.Customer import Customer
from Models.Editor import Editor
from typing import Union

# This file contains functions that work directly with the database

def find_user(id: str, pwd: str) -> Union[Customer, Editor, None]:
    '''
    This function finds the user, given the id and password. It should be able to tell
    if this is a customer or an editor, and return the appropriate object (Customer or Editor)
    '''
    # Checks if such customer exists. Return Customer object is yes
    config.cursor.execute("SELECT * FROM customers WHERE cid=:id AND pwd=:pass",
                                {"id":id, "pass":pwd})
    result = config.cursor.fetchone()

    if result != None:
        user = Customer()
        user.set_cid(user[0])
        user.set_name(user[1])
        user.set_pwd(user[2])
        return user
    
    # If such customer does not exist, checks if such editor exists. Return Editor object if yes
    config.cursor.execute("SELECT * FROM editors WHERE eid=:id AND pwd=:pass",
                                {"id":id, "pass":pwd})
    result = config.cursor.fetchone()
    
    if result != None:
        user = Editor()
        user.set_eid(user[0])
        user.set_pwd(user[1])
        return user
    
    # Return None if no such editor and customer exists 
    return None

def register_customer(cid: str, pwd: str) -> bool:
    '''
    This function registers a customer with given cid and pwd. The registered account must
    not have the same id as any other customer or editor
    Returns True if success, False otherwise
    '''

# below this line are scrap functions

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

def search_engine(word):
    '''
    Takes a keyword as input. Search for an mid with that keyword in
    title, cast member name, or cast member role
    Returns a list of mids
    '''
    mid_list = []
    # search in title
    config.cursor.execute('''SELECT mid FROM movies
                                WHERE title LIKE :word COLLATE NOCASE''',
                                {"word": word})
    results = config.cursor.fetchall()
    for result in results:
        mid_list.append(result[0])
    # search in cast member names
    config.cursor.execute('''SELECT mid FROM casts c, moviePeople m
                                WHERE c.pid = m.pid
                                AND m.name LIKE :word COLLATE NOCASE''',
                                {"word": word})
    results = config.cursor.fetchall()
    for result in results:
        mid_list.append(result[0])
    # search in cast member role
    config.cursor.execute('''SELECT mid FROM casts
                                WHERE role LIKE :word COLLATE NOCASE''',
                                {"word": word})
    results = config.cursor.fetchall()
    for result in results:
        mid_list.append(result[0])

    return mid_list

def find_movie(mid):
    '''
    Find a movie based on provided mid.
    Returns a Movie object if Movie exists, None otherwise
    '''
    config.cursor.execute('''SELECT * FROM movies WHERE mid = :mid''',
                                {"mid": mid})
    info = config.cursor.fetchone()
    if info != None:
        movie = Movie()
        movie.set_mid(info[0])
        movie.set_title(info[1])
        movie.set_year(info[2])
        movie.set_runtime(info[3])
        return movie
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

def start(self):
        '''
        starts a session given the cid. Store the session's information
        into the database with a duration of NULL
        '''
        # mark the starting time
        config.cursor.execute('''SELECT datetime('now')''')
        self.set_stime(config.cursor.fetchone())
        # mark the starting date
        config.cursor.execute('''SELECT date('now')''')
        self.set_sdate(config.cursor.fetchone()[0])
        # create a new session id
        config.cursor.execute('''SELECT MAX(sid) FROM sessions''')
        self.set_sid(config.cursor.fetchone()[0] + 1)

        config.cursor.execute('''INSERT INTO sessions VALUES(:sid, :cid, :sdate, NULL)''',
                                    {"sid": self.sid, "cid": self.cid, "sdate": self.sdate})

        config.connection.commit()

