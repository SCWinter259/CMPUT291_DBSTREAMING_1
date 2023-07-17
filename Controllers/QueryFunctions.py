from typing import Union
import config
from Models.Customer import Customer
from Models.Editor import Editor
from Models.Session import Session
from Models.Movie import Movie
from Models.MoviePeople import MoviePeople

# This file contains functions that work directly with the database

def find_user(id: str, pwd: str) -> Union[Customer, Editor, None]:
    '''
    This function finds the user, given the id and password. It should be able to tell
    if this is a customer or an editor, and return the appropriate object (Customer or Editor)
    '''
    # Checks if such customer exists. Return Customer object is yes
    config.cursor.execute(
        "SELECT * FROM customers WHERE cid=:id AND pwd=:pass",
        {"id":id, "pass":pwd}
    )
    result = config.cursor.fetchone()

    if result != None:
        user = Customer()
        user.set_cid(result[0])
        user.set_name(result[1])
        user.set_pwd(result[2])
        return user
    
    # If such customer does not exist, checks if such editor exists. Return Editor object if yes
    config.cursor.execute(
        "SELECT * FROM editors WHERE eid=:id AND pwd=:pass",
        {"id":id, "pass":pwd}
    )
    result = config.cursor.fetchone()
    
    if result != None:
        user = Editor()
        user.set_eid(result[0])
        user.set_pwd(result[1])
        return user
    
    # Return None if no such editor and customer exists 
    return None

def register_customer(cid: str, name:str, pwd: str) -> bool:
    '''
    This function registers a customer with given cid and pwd.
    This function has no return
    '''
    config.cursor.execute(
        "INSERT INTO customers VALUES (:id, :name, :pass)",
        {"id":cid, "name":name, "pass":pwd}
    )
    config.connection.commit()

def find_customer(cid: str) -> Union[Customer, None]:
    '''
    This function finds the customer given the cid (does not use password)
    Returns Customer object if customer exists, None otherwise
    '''
    config.cursor.execute(
        "SELECT * FROM customers WHERE cid=:id",
        {"id":cid}
    )
    result = config.cursor.fetchone()

    if result != None:
        user = Customer()
        user.set_cid(user.get_cid())
        user.set_name(user.get_name())
        user.set_pwd(user.get_pwd())
        return user
    else: 
        return None

def find_editor(eid: str) -> Union[Editor, None]:
    '''
    This function finds the editor given the eid (does not use password)
    Returns Editor object if customer exists, None otherwise
    '''
    config.cursor.execute(
        "SELECT * FROM editors WHERE eid=:id",
        {"id":eid}
    )
    result = config.cursor.fetchone()
    
    if result != None:
        user = Editor()
        user.set_eid(user.get_eid())
        user.set_pwd(user.get_pwd())
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
    session.set_sid(sid[0])
    session.set_cid(cid)
    session.set_stime(stime[0])

    stime = stime[0].split()       # get the time format for the sessions table
    stime = stime[0]

    config.cursor.execute(
        "INSERT INTO sessions VALUES (:session_id, :customer_id, :start_time, NULL)", 
        {"session_id":session.get_sid(), "customer_id":session.get_cid(), "start_time":stime}
    )
    config.connection.commit()
    
    return session

def search(text: str) -> list[Movie]:
    '''
    This function searches for movies based on the given text.

    The customer should be able to provide one or more unique keywords, 
    and the system should retrieve all movies that have any of those keywords in title, 
    cast member name or cast member role. For each match, at least the title, the year, 
    and the duration should be displayed, and the result should be ordered based on the 
    number of matching keywords with movies matching the largest number of 
    keywords listed on top.

    Returns a list of Movie objects sorted in the required order.
    '''
    # get the list of keywords
    # keep in mind that the order of keywords will be random
    # because we use set to remove duplication
    keywords = list(set(_chop(text)))
    keywords = [word.lower() for word in keywords]       

    all_mid = []        # for the mids (unique)
    all_count = []      # for the number of matches for each mid 

    for keyword in keywords:
        mid_title_list = _search_title(keyword)
        mid_role_list = _search_member_role(keyword)
        mid_name_list = _search_member_name(keyword)
        
        # if mid already exists in all_mid, update the count. If not append new mid and new count
        for [mid, count] in mid_title_list:
            if mid in all_mid:
                all_count[all_mid.index(mid)] += count
            else:
                all_mid.append(mid)
                all_count.append(count)

        for [mid, count] in mid_role_list:
            if mid in all_mid:
                all_count[all_mid.index(mid)] += count
            else:
                all_mid.append(mid)
                all_count.append(count)

        for [mid, count] in mid_name_list:
            if mid in all_mid:
                all_count[all_mid.index(mid)] += count
            else:
                all_mid.append(mid)
                all_count.append(count)

    mid_list = zip(all_mid, all_count)
    mid_list.sort(key=lambda index: index[1], reversed=True)        # sort the zipped list by count, descending order

    movie_list = []
    for item in mid_list:
        mid = item[0]
        config.cursor.execute(
            '''SELECT mid, title, year, runtime FROM movies WHERE mid=:mid''',
            {"mid": mid}
        )
        result = config.cursor.fetchone()

        movie = Movie()
        movie.set_mid(result[0])
        movie.set_title(result[1])
        movie.set_year(result[2])
        movie.set_runtime(result[3])
        
        movie_list.append(movie)

    return movie_list

# support functions
def _chop(text: str) -> list[str]:
    '''
    Takes in a string, return the list of words in that strings,
    after getting rid of all white spaces, comma, colon, semi-colon, and question marks
    '''
    text = text.replace(',', ' ')
    text = text.replace(':', ' ')
    text = text.replace(';', ' ')
    text = text.replace('?', ' ')

    return text.split(' ')

def _search_title(word: str) -> list[str, int]:
    '''
    This function searches for movies with title containing
    the given keyword.
    Returns a list of [mid, number of repetitions]
    '''
    mid_list = []
    config.cursor.execute(
        '''SELECT mid, title FROM movies WHERE title LIKE :word COLLATE NOCASE''',
        {"word": word}
    )
    results = config.cursor.fetchall()      # got a list of (mid, title)

    # count the number of repetition of the keyword in the title
    for (mid, title) in results:
        title_list_split = _chop(title)
        count = title_list_split.count(word)
        mid_list.append([mid, count])       # append appropriate data into the list

    return mid_list

def _search_member_role(word: str) -> list[str, int]:
    '''
    This function searches for movies with a role containing
    the given keyword.
    Returns a list of [mid, number of repetitions]
    '''
    mid_list = []
    config.cursor.execute(
        '''SELECT mid, role FROM casts WHERE role LIKE :word COLLATE NOCASE''',
        {"word": word}
    )
    results = config.cursor.fetchall()      # got a list of (mid, role)

    # count the number of repetition of the keyword in the role
    for (mid, role) in results:
        title_list_split = _chop(role)
        count = title_list_split.count(word)
        mid_list.append([mid, count])       # append appropriate data into the list

    return mid_list

def _search_member_name(word: str) -> list[str, int]:
    '''
    This function searches for movies with a member whose
    name contains the given keyword.
    Returns a list of [mid, number of repetitions]
    '''
    mid_list = []
    config.cursor.execute(
        '''SELECT pid, name FROM moviePeople WHERE name LIKE :word COLLATE NOCASE''',
        {"word": word}
    )
    results = config.cursor.fetchall()      # got a list of (pid, name)

    # count the number of repetition of the keyword in the name
    pid_list = []
    for (pid, name) in results:
        title_list_split = _chop(name)
        count = title_list_split.count(word)
        pid_list.append([pid, count])       # append appropriate data into the list

    for [pid, count] in pid_list:           # for each pid, find the mid
        config.cursor.execute(
            '''SELECT mid FROM casts WHERE pid=:pid''',
            {"pid": pid}
        )
        all_mid = config.cursor.fetchall()
        for mid in all_mid:         # does the mid exist in mid_list yet?
            found = False
            for i in range(len(mid_list)):
                if mid_list[i][0] == mid:       # if yes, increase count
                    found = True
                    mid_list[i][1] += count
                    break
            if not found:           # if not, append new sub list
                mid_list.append([mid, count])

    return mid_list


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