from typing import Union
import config
from Controllers.HelperFunctions import (
    _chop, _search_title, _search_member_name, _search_member_role, has_watched, _check_watch)
from Models.Customer import Customer
from Models.Editor import Editor
from Models.Session import Session
from Models.Movie import Movie
from Models.MoviePeople import MoviePeople

# This file contains functions that work directly with the database
# We try to import config only in this file (to avoid circulating imports)
# cache is imported in View files

# below, some of the functions take in, say, Customer, while some others only
# take in the cid. Generally, if the function only needs one attribute from the object,
# the function would only take in that one attribute.

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

    if result != None: return Customer(cid=result[0], name=result[1], pwd=result[2])
    
    # If such customer does not exist, checks if such editor exists. Return Editor object if yes
    config.cursor.execute(
        "SELECT * FROM editors WHERE eid=:id AND pwd=:pass",
        {"id":id, "pass":pwd}
    )
    result = config.cursor.fetchone()
    
    if result != None: return Editor(eid=result[0], pwd=[1])
    
    # Return None if no such editor and customer exists 
    return None

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

    if result != None: return Customer(cid=result[0], name=result[1], pwd=result[2])
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

    if result != None: return Editor(eid=result[0], pwd=result[1])
    return None

def find_movie(mid: int) -> Union[Movie, None]:
    '''
    This function finds the movie given the mid.
    Returns Movie object if movie exists, None otherwise
    '''
    config.cursor.execute(
        "SELECT * FROM movies WHERE mid=:mid",
        {"mid":mid}
    )
    result = config.cursor.fetchone()

    if result != None: return Movie(mid=result[0], title=result[1], year=result[2], runtime=result[3])
    return None

def register_customer(cid: str, name:str, pwd: str) -> None:
    '''
    This function registers a customer with given cid and pwd.
    Returns None
    '''
    config.cursor.execute(
        "INSERT INTO customers VALUES (:id, :name, :pass)",
        {"id":cid, "name":name, "pass":pwd}
    )
    config.connection.commit()

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
    session = Session(sid=sid[0], cid=cid, stime=stime[0])

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

    mid_list = list(zip(all_mid, all_count))
    mid_list.sort(key=lambda index: index[1], reverse=True)        # sort the zipped list by count, descending order

    # print(mid_list)

    movie_list = []
    for item in mid_list:
        mid = item[0]
        config.cursor.execute(
            '''SELECT mid, title, year, runtime FROM movies WHERE mid=:mid''',
            {"mid": mid}
        )
        result = config.cursor.fetchone()

        movie = Movie(mid=result[0], title=result[1], year=result[2], runtime=result[3])
        
        movie_list.append(movie)

    return movie_list

def find_cast(mid: int) -> list[MoviePeople, str]:
    '''
    This function takes in a Movie object and finds the cast of that movie.
    Returns a list of [MoviePeople, role] lists.
    '''
    cast = []

    # find in casts table for all pids and roles of that mid
    config.cursor.execute(
        '''SELECT pid, role FROM casts WHERE mid=:mid''',
        {"mid": mid}
    )
    all_pid_role = config.cursor.fetchall()     # we get a tuple of (pid, role,) for that mid

    # for each pid, we find the full information about that member
    for i in range(len(all_pid_role)):
        pid = all_pid_role[i][0]
        role = all_pid_role[i][1]
        config.cursor.execute(
            '''SELECT name, birthYear FROM moviePeople WHERE pid=:pid''',
            {"pid": pid}
        )
        info = config.cursor.fetchone()
        name = info[0]
        birth_year = info[1]

        cast_member = MoviePeople(pid=pid, name=name, birthYear=birth_year)

        cast.append([cast_member, role])

    return cast

def count_customer_watched(movie: Movie) -> int:
    '''
    This function counts the number of customers who have watched 
    the movie (given Movie object).
    Returns the number of customers who have watched the movie.
    '''
    # find all customers
    count = 0

    config.cursor.execute(
        '''SELECT cid FROM customers'''
    )

    results = config.cursor.fetchall()

    for (cid,) in results:
        if has_watched(cid=cid, mid=movie.get_mid(), runtime=movie.get_runtime()):
            count += 1

    return count

def follow(cid: str, pid: str) -> None:
    '''
    If the customer has already followed the cast member, this
    function would return False and not change anything.
    Else, this function add the given cid and pid to the follows table,
    signalling that the given customer follows the given cast member
    and return True.
    '''
    config.cursor.execute(
        '''SELECT * FROM follows WHERE cid=:cid and pid=:pid''',
        {"cid": cid, "pid": pid}
    )
    result = config.cursor.fetchone()

    if result != None: return False
    else:
        config.cursor.execute(
            '''INSERT INTO follows VALUES (:cid, :pid)''',
            {"cid": cid, "pid": pid}
        )
        config.connection.commit()
        return True

def watch(sid: int, cid: str, mid: int) -> str:
    '''
    This function helps the customer to start watching a movie.
    If the user already watched the movie in that session, then no value
    is inserted.
    We would write into the watch table the current session id and
    customer id (taken from cache file), the mid of the movie being watched,
    and duration as NULL.
    This function returns the start time of the watch, which is a string
    '''
    if _check_watch(sid=sid, cid=cid, mid=mid) == 'No entry found':    # if the movie has not been watched in that session
        config.cursor.execute(
            '''INSERT INTO watch VALUES (:sid, :cid, :mid, NULL)''',
            {"sid": sid, "cid": cid, "mid": mid}
        )
        config.connection.commit()

    config.cursor.execute("SELECT datetime('now')")
    stime = config.cursor.fetchone()      # get the appropriate stime

    return stime[0]

def end_watch(sid: int, cid: str, mid: int, stime: str) -> None:
    '''
    This function would end the customer's movie watch by replacing the NULL value
    in the duration column of the watch table with the actual duration that the 
    customer has watched the movie.
    Returns None
    '''
    # get the duration
    config.cursor.execute(
        '''SELECT strftime('%M', 'now') - strftime('%M', :stime)''',
        {'stime': stime}
    )
    duration = config.cursor.fetchone()
    duration = duration[0]

    # if in the same session and with the same movie, the user has watched
    # for some time, we shall add the duration
    recorded_duration = _check_watch(sid=sid, cid=cid, mid=mid)
    if type(recorded_duration) == int: duration += recorded_duration

    # update the duration column
    config.cursor.execute(
        '''UPDATE watch SET duration=:duration 
        WHERE sid=:sid AND cid=:cid AND mid=:mid''',
        {"sid": sid, "cid": cid, "mid": mid, "duration": duration}
    )
    config.connection.commit()

def end_session(session: Session) -> None:
    '''
    This function ends the customer session by recording the session duration into
    the sessions table. This function is to be called when the customer logout.
    Returns None.
    '''
    sid = session.get_sid()
    cid = session.get_cid()
    stime = session.get_stime()

    # get the duration in minutes
    config.cursor.execute(
        '''SELECT strftime('%M', 'now') - strftime('%M', :stime)''',
        {'stime': stime}
    )
    duration = config.cursor.fetchone()
    duration = duration[0]

    sdate = stime.split()       # get the time format for the sessions table
    sdate = sdate[0]

    # update the duration column
    config.cursor.execute(
        '''UPDATE sessions SET duration=:duration 
        WHERE sid=:sid AND cid=:cid AND sdate=:sdate''',
        {"sid": sid, "cid": cid, "sdate": sdate, "duration": duration}
    )
    config.connection.commit()