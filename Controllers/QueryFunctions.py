from Controllers import config
from Models.Customer import Customer
from Models.Editor import Editor
from Models.Session import Session

# This file contains functions that work directly with the database

def find_user(id: str, pwd: str) -> Customer | Editor | None:
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

def register_customer(cid: str, name:str, pwd: str) -> bool:
    '''
    This function registers a customer with given cid and pwd. The registered account must
    not have the same id as any other customer or editor
    Returns True if success, False otherwise
    '''
    if find_customer(cid) == None or find_editor(cid) == None:
        config.cursor.execute("INSERT INTO customers VALUES (:id, :name, :pass)",
                                    {"id":cid, "name":name, "pass":pwd})
        config.connection.commit()
        return True
    else:
        return False

def find_customer(cid: str) -> Customer | None:
    '''
    This function finds the customer given the cid (does not use password)
    Returns Customer object if customer exists, None otherwise
    '''
    config.cursor.execute("SELECT * FROM customers WHERE cid=:id",
                            {"id":cid})
    result = config.cursor.fetchone()

    if result != None:
        user = Customer()
        user.set_cid(user[0])
        user.set_name(user[1])
        user.set_pwd(user[2])
        return user
    else: 
        return None

def find_editor(eid: str) -> Editor | None:
    '''
    This function finds the editor given the eid (does not use password)
    Returns Editor object if customer exists, None otherwise
    '''
    config.cursor.execute("SELECT * FROM editors WHERE eid=:id",
                                {"id":eid})
    result = config.cursor.fetchone()
    
    if result != None:
        user = Editor()
        user.set_eid(user[0])
        user.set_pwd(user[1])
        return user
    else:
        return None

def start_session(customer:Customer) -> Session:
    '''
    This function inserts into the sessions table the appropriate sid, cid, sdate, and duration
    sid would be the largest sid + 1
    cid would be provided by the Customer object
    sdate would be the moment this function is called (current time)
    duration would be inserted as NULL

    We would later have to calculate the duration, so the format we need is "year-month-date hour-minute"
    Since the sdate column in sessions table only takes "year-month-date", the idea is to store the
    longer format into a Session object, then cut down the format and store into the sessions table.
    Therefore, this function also have to update the Session object by inserting the appropriate
    sid, cid, and stime. The other two properties can stay as None.

    Returns the Session object
    '''
    config.cursor.execute("SELECT MAX(sid)+1 FROM sessions")
    sid = config.cursor.fetchone()      # get the appropriate sid

    cid = customer.get_cid()        # get the appropriate cid

    config.cursor.execute("SELECT datetime('now')")
    stime = config.cursor.fetchone()      # get the appropriate stime

    # create Session object
    session = Session()
    session.set_sid(sid)
    session.set_cid(cid)
    session.set_stime(stime)

    stime = stime.split()       # get the time format for the sessions table
    stime = stime[0]

    config.cursor.execute("INSERT INTO sessions VALUES (:session_id, :customer_id, :start_time, NULL)", 
                          {"session_id":sid, "customer_id":cid, "start_time":stime})
    config.connection.commit()
    
    return session


# below this line are scrap functions

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

