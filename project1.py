import sqlite3
import getpass

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

def start_session(cid):
    '''
    Youssef
    This function will automatically start a
    new session whenever called for the given
    customer cid.  It will store the session's
    information into the database with a duration
    of NULL.
    '''
    global connection, cursor
    
    cursor.execute('''SELECT datetime('now');''')
    start_time = cursor.fetchone()
    cursor.execute('''SELECT date('now')''')
    start_date = cursor.fetchone()
    cursor.execute('''SELECT MAX(sid) FROM sessions;''')
    max_sid = cursor.fetchone()
    unique_sid = max_sid[0] + 1

    cursor.execute('''INSERT INTO sessions VALUES (:unique_sid, :cid, :start_date, NULL)''',
                        {"unique_sid":unique_sid, "cid":cid, "start_date":start_date[0]})
    connection.commit()

    return start_time[0], unique_sid

def search(): #DONE
    '''
    Casper
    Customer provides one or more unique keyword(s)
    System retrives all movies with any keyword in title,
    cast member name, cast member role
    Results ordered based on the number of matching
    keywords, from the most to the least
    For each result, display:
    - title
    - year
    - duration
    At most 5 results will be shown at a time,
    letting the user to select a movie or see more matches
    or search again
    When select the movie, information will include:
    - title
    - year
    - duration
    - cast members
    - number of people who have watched it
    - option to select a cast member and follow, or 
    - start watching, or go back
    Additionally, when start watching, one can still 
    go back and search and do everything again until
    the session ends.
    '''
    global connection, cursor

    # TODO: go back function, logout function

    search_string = input("Enter your search: ")
    results = search_engine(search_string)
    results.sort(key=lambda x: x[1], reverse=True)
    movie_id = display_search(results)

    return movie_id

def start_watch(): #DONE
    '''
    Casper
    This is a detached function from search
    This function will return the start time of 
    the movie
    '''
    global connection, cursor

    cursor.execute("SELECT datetime('now');")
    start_time = cursor.fetchone()
    
    return start_time[0]

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
        print("Followed " + name + '!')
    else:
        print("You have already followed this person!")

def display_search(results): #DONE
    '''
    Casper
    This is a helper function for search
    This function takes in the list of search results 
    and display 5 at once
    This function returns the chosen mid
    '''
    global connection, cursor

    total_results = len(results)
    index_count = 0
    display_more = True

    print("Number of results: " + str(total_results))

    if total_results == 0:
        return None

    while display_more == True:
        if total_results >= 5:
            for i in range(5):
                print("--------------------")
                print("No. " + str(index_count + 1))
                display_one_result(results[index_count][0], False)
                index_count = index_count + 1
                total_results = total_results - 1
                display_more = False
        else:
            for i in range(total_results):
                print("--------------------")
                print("No. " + str(index_count + 1))
                display_one_result(results[index_count][0], False)
                index_count = index_count + 1
                total_results = total_results - 1
                display_more = False
        while total_results > 0:
            print("Enter 1 to start selecting a movie")
            print("Enter 2 to display more results")
            route = input("Enter your choice: ")
            if route == '1':
                while 1:
                    pick = input("Enter the movie number: ")
                    if pick.isdecimal() == True and int(pick) <= index_count + 1 and int(pick) > 0:
                        break
                    else:
                        print("Please enter a natural number smaller than " + str(index_count + 2))
                display_one_result(results[int(pick) - 1][0], True)
                return results[int(pick) - 1][0]
            elif route == '2' and total_results > 0:
                display_more = True
                break
            else:
                print("Invalid input")

        if total_results == 0:
            while 1:
                print("Enter 1 to start selecting a movie")
                route = input("Enter your choice: ")
                if route == '1':
                    while 1:
                        pick = input("Enter the movie number: ")
                        if pick.isdecimal() == True and int(pick) <= index_count + 1 and int(pick) > 0:
                            break
                        else:
                            print("Please enter a natural number smaller than " + str(index_count + 2))
                    display_one_result(results[int(pick) - 1][0], True)
                    return results[int(pick) - 1][0]
                else:
                    print("Invalid input")

def display_one_result(mid, choice): #DONE
    '''
    Casper
    This is a helper function for display_search
    This function takes in the movie id and a choice 
    This function displays:
    (regardless of choice)
    - title
    - year
    - duration
    (additionally, if choice is True)
    - cast members
    - number of people who have watched it
    '''
    global connection, cursor

    cursor.execute('''SELECT title, year, runtime
                        FROM movies
                        WHERE mid=:mid''',
                        {"mid":mid})
    row = cursor.fetchone()
    print("title: " + str(row[0]))
    print("year: " + str(row[1]))
    print("runtime: " + str(row[2]))
    if choice == True:
        cursor.execute('''SELECT w.cid
                            FROM watch w, movies m
                            WHERE w.mid = :mid
                            AND w.mid = m.mid
                            GROUP BY w.cid 
                            HAVING SUM(w.duration) > m.runtime/2''',
                            {"mid":mid})
        all_people = cursor.fetchall()
        number = len(all_people)
        print("Number of people who watched the movie: " + str(number))

        cursor.execute('''SELECT m.name 
                            FROM moviePeople m, casts c
                            WHERE m.pid = c.pid
                            AND c.mid =:mid''', 
                            {"mid":mid})
        all_cast = cursor.fetchall()
        print("cast: ")
        for member in all_cast:
            print("-", member[0])

def search_engine(search_string): #DONE
    '''
    Casper
    This is a helper function for search
    This function takes in search_string and
    returns a list in the following format:
    [[mid, the number of matches],...]
    '''
    global connection, cursor

    all_output = []
    keywords = search_string.split()
    for item in keywords:
        item = '%' + item + '%'
        from_title = search_title(item)
        for a in from_title:
            all_output.append(a[0])
        from_name = search_cast_member_name(item)
        for b in from_name:
            all_output.append(b[0])
        from_role = search_cast_member_role(item)
        for c in from_role:
            all_output.append(c[0])

    final_output = []
    for d in all_output:
        duplicate = False
        for element in final_output:
            if d == element[0]:
                element[1] = element[1] + 1
                duplicate = True
                break
        if duplicate == False:
            new_element = [d, 1]
            final_output.append(new_element)
    
    return final_output

def search_title(item): #DONE
    '''
    Casper
    This is a helper function of search_engine
    This function takes in the modified search string
    and return a tuple of mid
    '''
    global connection, cursor

    cursor.execute('''SELECT mid FROM movies 
                    WHERE title LIKE :item COLLATE NOCASE''',
                    {"item":item})
    movie_id = cursor.fetchall()

    return movie_id

def search_cast_member_name(item): #DONE
    '''
    Casper
    This is a helper function of search_engine
    This function takes in the modified search string
    and return a tuple of mid
    '''
    global connection, cursor

    cursor.execute('''SELECT mid FROM casts c, moviePeople m 
                        WHERE c.pid = m.pid
                        AND m.name LIKE :item COLLATE NOCASE''',
                        {"item":item})
    movie_id = cursor.fetchall()
    
    return movie_id

def search_cast_member_role(item): #DONE
    '''
    Casper
    This is a helper function of search_engine
    This function takes in the modified search string
    and return a tuple of mid
    '''
    global connection, cursor

    cursor.execute('''SELECT mid FROM casts
                        WHERE role LIKE :item COLLATE NOCASE''',
                        {"item":item})
    movie_id = cursor.fetchall()

    return movie_id

def end_watch(sid, cid, mid, start_time): #DONE
    '''
    Casper
    This function calculates the amount of time spend watching a movie
    in a session, then insert information into watch.
    '''
    global connection, cursor
    
    cursor.execute('''SELECT strftime('%s','now') - 
                        strftime('%s', :start_time)''',
                        {"start_time":start_time})
    end_time = cursor.fetchone()

    cursor.execute('''SELECT runtime FROM movies WHERE mid=:mid''',
                        {"mid":mid})
    runtime = cursor.fetchone()

    if (end_time[0] / 60) >= runtime[0]:
        time_watched = runtime[0]
    else:
        time_watched = end_time[0] / 60
    
    cursor.execute('''INSERT INTO watch VALUES (:sid, :cid, :mid, :time_watched)''',
                    {"sid":sid, "cid":cid, "mid": mid, "time_watched":time_watched})
    print("Your watch has ended")

def end_session(sid, mid, start_time): #DONE
    '''
    Youssef
    This function end the session with the
    given sid.  It uses the start date of the
    given session in order to calculate the
    duration.  The given mid is used to end
    a movie that is being played (if there is one)
    by calling end_watch().  It will update the
    duration for the session with the given sid.
    '''
    global connection, cursor
    
    cursor.execute('''SELECT strftime('%s','now') - strftime('%s',:start_time)''',
                    {"start_time":start_time})
    duration = cursor.fetchone()

    cursor.execute('''SELECT cid FROM sessions WHERE sid=:sid''',
                    {"sid":sid})
    cid = cursor.fetchone()

    duration_min = duration[0] / 60

    if mid != None:
        end_watch(sid, cid[0], mid, start_time)

    cursor.execute('''UPDATE sessions SET duration=:duration_min WHERE sid=:sid''',
                        {"duration_min":duration_min, "sid":sid})
    connection.commit()

def add_movie(): #DONE
    '''
    Daniel
    This Function lets the editor add movies into the database. 
    The function uses SQL queries to find elements needed in the 
    database and queries are used to add  elements to the database.
    Parameter: None
    Return: None
    '''
    global connection, cursor
    
    x = False
    while (x == False):
        movieId = input("Enter movie unique ID: ")
        try:
            movieId = int(movieId)
            x = True
        except:
            print("Unique movie Id must be an int.")
          
    movieTitle = input("Enter movie title: ")
    
    x = False
    while (x == False):
        movieYear = input("Enter movie year (eg. 2002, 2017...): ")
        try:
            movieYear = int(movieYear)
            x = True
        except:
            print("Movie Year must be an int.")
    
    x = False
    while (x == False):
        movieRtime = int(input("Enter movie runtime in minutes: "))
        try:
            movieRtime = int(movieRtime)
            x = True
        except:
            print("Movie Runtime must be an int.")
    
    insert = [movieId , movieTitle, movieYear, movieRtime]
    cursor.execute("SELECT mid FROM movies WHERE mid =:n", {"n":movieId} )
    r = cursor.fetchone()
    if (r != None):
        print("Unique movie Id already in use")
        while (x == False):
            movieId = input("Enter movie unique ID: ")
            cursor.execute("SELECT mid FROM movies WHERE	mid =:n", {"n":movieId} )	
            r = cursor.fetchone()
            if (r == None):
                x = True
            else:
                print("Unique movie Id already in use") 
        insert = [movieId , movieTitle, movieYear, movieRtime]
    
    while True:
        while True:
            castId = input("Enter cast member Id: ")
            castId = castId.lower()
            if (len(castId) != 4):
                print("Cast Id must be a length of 4 characters")
            else:
                break
        
        cursor.execute("SELECT pid FROM moviePeople WHERE pid =:n", {"n":castId} )
        r = cursor.fetchone()
        if (r != None):
            cursor.execute("SELECT name , birthYear FROM moviePeople WHERE pid =:n", {"n": castId} )
            r = cursor.fetchone()
            print(r)
            choice = input("Do your want to (1) assign role to cast member or (2) reject? ")
            if (choice == '1'):
                role = input("Assign cast member role: ")
                insert2 = [movieId, castId, role ]
                try:
                    cursor.execute("INSERT INTO casts VALUES (?, ?, ?);", insert2)
                    cursor.commit()
                except:
                    print("Cannot assign role to same cast member more than once ")
                    continue
                choice2 = input("Do you want to (1) add another cast member or (2) leave? ")
                if (choice2 == '1'):
                    continue
                elif(choice2 == '2'):
                    cursor.execute("INSERT INTO movies VALUES (?, ?, ?, ?);", insert)
                    cursor.commit()
                    break       
            elif (choice == '2'):
                print("Cast member rejected")
                choice2 = input("Do you want to (1) add a cast member or (2) leave? ")
                if (choice2 == '1'):
                    continue
                elif(choice2 == '2'):
                    break
            else:
                print("Invalid input, Try agian")
                continue

        else:
            choice3 = input("Cast member not found, do you want to (1) create new cast member or (2) No? ")
            if (choice3 == '1'):
                while True:
                    castId = input("Enter new cast member Id: ")
                    castId = castId.lower()
                    cursor.execute("SELECT pid FROM moviePeople WHERE pid =:n", {"n":castId} )
                    r = cursor.fetchone()
                    if (len(castId) != 4):
                        print("Cast Id must be a length of 4 characters")
                    elif (r != None):
                        print("Cast Id already exists")
                    else:
                        break

                castName = input("Enter cast member name: ")
                x = False
                while (x == False):
                    bYear = input("Enter cast member birth year: ")
                    try:
                        bYear = int(bYear)
                        x = True
                    except:
                        print("Birth Year must be an int.")

                insert3 = [castId, castName, bYear]
                cursor.execute("INSERT INTO moviePeople VALUES (?, ?, ?);", insert3)
                cursor.commit()
                print("New cast member created")
                
                choice = input("Do your want to (1) assign role to cast member or (2) reject? ")
                if (choice == '1'):
                    role = input("Assign cast member role: ")
                    insert2 = [movieId, castId, role ]
                    try:
                        cursor.execute("INSERT INTO casts VALUES (?, ?, ?);", insert2)
                        cursor.commit()
                    except:
                        print("Cannot assign role to same cast member more than once ")
                        continue
                    choice2 = input("Do you want to (1) add another cast member or (2) leave? ")
                    if (choice2 == '1'):
                        continue
                    elif(choice2 == '2'):
                        cursor.execute("INSERT INTO movies VALUES (?, ?, ?, ?);", insert)
                        cursor.commit()
                        break       
                elif (choice == '2'):
                    print("Cast member rejected")
                    choice2 = input("Do you want to (1) add a cast member or (2) leave? ")
                    if (choice2 == '1'):
                        continue
                    elif(choice2 == '2'):
                        break
                else:
                    print("Invalid input, Try agian")
                    continue

            elif(choice3 == '2'):
                continue

def update_recommendation():
    '''
    Daniel
    This Function will let the editor search and make 
    changes to the recommended list in the database.
    Parameter: None
    Return: None
    '''
    global connection, cursor
    
    while True:
        choice = input("Please choose (1) Monthly, (2) Annual, (3) All-Time, (4) leave: ")
        if (choice == '1'):
            check = ['01','02','03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
            while True:
                try:
                    month = input("Please enter a month in number form (eg. 01, 07...: ")
                    assert (month in check)
                    break
                except:
                    print("Invalid input")
            year = input("Please enter a year: ")

            r = cursor.execute('''SELECT * FROM recommendations r;''')
            r = cursor.fetchall()
            lst = [list(x) for x in r]

            z = cursor.execute('''SELECT cid FROM customers;''')
            z = cursor.fetchall()
            
            count = 0
            new = []
            for i in range(len(r)):
                new.append([])

            for x in range (len(z)):
                for y in range (len(r)):
                    m1 = cursor.execute('''SELECT COUNT(w.mid) FROM watch w
                    INNER JOIN sessions s ON w.sid = s.sid WHERE w.cid = :n
                    AND w.mid = :t AND strftime('%m',s.sdate) IN (:m)
                    AND strftime('%Y',s.sdate) IN (:y);''', 
                    {"n": z[x][0], "t": r[y][0], "m": month, "y": year} )
                    m1 = cursor.fetchall()
                

                    m2 = cursor.execute('''SELECT COUNT(w.mid) FROM watch w
                    INNER JOIN sessions s ON w.sid = s.sid WHERE w.cid = :n
                    AND w.mid = :t AND strftime('%m',s.sdate) IN (:m)
                    AND strftime('%Y',s.sdate) IN (:y);''', 
                    {"n": z[x][0], "t": r[y][1], "m": month, "y": year} )
                    m2 = cursor.fetchall()
                    
                    
                    count = int((m1[0][0] + m2[0][0]) / 2)
                    if (count < 1):
                        count = 0
                    new[y].append(count)
            
                  
            for x in range (len(new)):
                lst[x].append(sum(new[x]))
            
            lst.sort(key = lambda x: x[3], reverse=True)  
            
            for x in range(len(lst)):
                print(f"M1: {lst[x][0]}, M2: {lst[x][1]}, # of Customers watched: {lst[x][3]}, score: {lst[x][2]}")
            
            while True:
                choice2 = input("Do you want to (1) search a different list, (2) update a pair, or (3) leave? ")
                if (choice2 == '1'):
                    break
                elif(choice2 == '2'):
                    while True:
                        choice3 = input("Do you want to (1) update a score, (2) delete a pair, or (3) add pair? ")
                        if(choice3 == '1'):
                            while True:
                                i1 = input("Enter your m1 movie id: ")
                                r = cursor.execute('''SELECT * FROM recommendations
                                                    WHERE watched = :n''', {"n": i1})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M1 does not exist in lists")
                            while True:
                                i2 = input("Enter your m2 movie id: ")
                                r = cursor.execute('''SELECT * FROM recommendations
                                                WHERE recommended = :n''', {"n": i2})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M2 does not exist in lists")

                            while True:
                                try:
                                    score = float(input("What score would you like to input (0 < score < 1)? "))
                                    assert(0 < score < 1)
                                    break
                                except:
                                    print("Invalid input")
                            
                            cursor.execute('''
                            UPDATE recommendations
                            SET score = :n
                            WHERE watched = :w
                            AND recommended = :r
                             ''', {"n": score, "w": i1, "r": i2})
                            
                            print("Pair updated.")
                            break

                        elif(choice3 == '2'):
                            while True:
                                i1 = input("Enter your m1 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE watched = :n''', {"n": i1})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M1 does not exist in lists")
                            while True:
                                i2 = input("Enter your m2 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE recommended = :n''', {"n": i2})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M2 does not exist in lists")
                            
                            cursor.execute('''
                            DELETE 
                            FROM recommendations
                            WHERE watched = :w
                            AND recommended = :r
                             ''', {"w": i1, "r": i2})
                            
                            print("Pair Deleted.")
                            break
                        elif(choice3 == '3'):
                            while True:
                                i1 = input("Enter your m1 movie id: ")
                                i2 = input("Enter your m2 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE watched = :n
                                AND recommeded = :r''', {"n": i1, "r": i2})
                                r = r.fetchone()
                                if (r != None):
                                    print("Pair already exist in lists")
                                else:
                                    break
                            
                            while True:
                                try:
                                    score = float(input("What score would you like to input (0 < score < 1)? "))
                                    assert(0 < score < 1)
                                    break
                                except:
                                    print("Invalid input")

                            cursor.execute(''' 
                            insert into recommendations values (:w, :r, :s);
                            ''', {"w": i1, "r": i2, "s": score})

                            print("Pair Added.")
                            break      
                        else:
                            print("Invalid input")
                elif(choice2 == '3'):
                    break
                else:
                    print("Invalid input")
                
        elif(choice == '2'):

            year = input("Please enter a year: ")

            r = cursor.execute('''
            SELECT *
            FROM recommendations r;
            ''')
            r = cursor.fetchall()
            lst = [list(x) for x in r]

            z = cursor.execute(''' 
            SELECT cid 
            FROM customers;
            ''')
            z = cursor.fetchall()
            
            count = 0
            new = []
            for i in range(len(r)):
                new.append([])

            for x in range (len(z)):
                for y in range (len(r)):
                    m1 = cursor.execute('''
                    SELECT COUNT(w.mid) 
                    FROM watch w
                    INNER JOIN sessions s
                    ON w.sid = s.sid
                    WHERE w.cid = :n
                    AND w.mid = :t
                    AND strftime('%Y',s.sdate) IN (:y);
                    ''', {"n": z[x][0], "t": r[y][0], "y": year} )
                    m1 = cursor.fetchall()
                

                    m2 = cursor.execute('''
                    SELECT COUNT(w.mid) 
                    FROM watch w
                    INNER JOIN sessions s
                    ON w.sid = s.sid
                    WHERE w.cid = :n
                    AND w.mid = :t
                    AND strftime('%Y',s.sdate) IN (:y);
                    ''', {"n": z[x][0], "t": r[y][1], "y": year} )
                    m2 = cursor.fetchall()
                    
                    
                    count = int((m1[0][0] + m2[0][0]) / 2)
                    if (count < 1):
                        count = 0
                    new[y].append(count)
            
                  
            for x in range (len(new)):
                lst[x].append(sum(new[x]))
            
            lst.sort(key = lambda x: x[3], reverse=True)  
            
            for x in range(len(lst)):
                print(f"M1: {lst[x][0]}, M2: {lst[x][1]}, # of Customers watched: {lst[x][3]}, score: {lst[x][2]}")
            
            while True:
                choice2 = input("Do you want to (1) search a different list, (2) update a pair, or (3) leave? ")
                if (choice2 == '1'):
                    break
                elif(choice2 == '2'):
                    while True:
                        choice3 = input("Do you want to (1) update a score, (2) delete a pair?, or (3) add pair? ")
                        if(choice3 == '1'):
                            while True:
                                i1 = input("Enter your m1 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE watched = :n''', {"n": i1})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M1 does not exist in lists")
                            while True:
                                i2 = input("Enter your m2 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE recommended = :n''', {"n": i2})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M2 does not exist in lists")

                            while True:
                                try:
                                    score = float(input("What score would you like to input (0 < score < 1)? "))
                                    assert(0 < score < 1)
                                    break
                                except:
                                    print("Invalid input")
                            
                            cursor.execute('''
                            UPDATE recommendations
                            SET score = :n
                            WHERE watched = :w
                            AND recommended = :r
                             ''', {"n": score, "w": i1, "r": i2})
                            
                            print("Pair updated.")
                            break

                        elif(choice3 == '2'):
                            while True:
                                i1 = input("Enter your m1 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE watched = :n''', {"n": i1})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M1 does not exist in lists")
                            while True:
                                i2 = input("Enter your m2 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE recommended = :n''', {"n": i2})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M2 does not exist in lists")
                            
                            cursor.execute('''
                            DELETE 
                            FROM recommendations
                            WHERE watched = :w
                            AND recommended = :r
                             ''', {"w": i1, "r": i2})
                            
                            print("Pair Deleted.")
                            break
                        elif(choice3 == '3'):
                            while True:
                                i1 = input("Enter your m1 movie id: ")
                                i2 = input("Enter your m2 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE watched = :n
                                AND recommeded = :r''', {"n": i1, "r": i2})
                                r = r.fetchone()
                                if (r != None):
                                    print("Pair already exist in lists")
                                else:
                                    break
                                
                            while True:
                                try:
                                    score = float(input("What score would you like to input (0 < score < 1)? "))
                                    assert(0 < score < 1)
                                    break
                                except:
                                    print("Invalid input")

                            cursor.execute(''' 
                            insert into recommendations values (:w, :r, :s);
                            ''', {"w": i1, "r": i2, "s": score})

                            print("Pair Added.")
                            break      
                                  
                        else:
                            print("Invalid input")
                elif(choice2 == '3'):
                    break
                else:
                    print("Invalid input")
       
        elif(choice == '3'):
            r = cursor.execute('''
            SELECT *
            FROM recommendations r;
            ''')
            r = cursor.fetchall()
            lst = [list(x) for x in r]

            z = cursor.execute(''' 
            SELECT cid 
            FROM customers;
            ''')
            z = cursor.fetchall()
            
            count = 0
            new = []
            for i in range(len(r)):
                new.append([])

            for x in range (len(z)):
                for y in range (len(r)):
                    m1 = cursor.execute('''
                    SELECT COUNT(w.mid) 
                    FROM watch w
                    INNER JOIN sessions s
                    ON w.sid = s.sid
                    WHERE w.cid = :n
                    AND w.mid = :t;
                    ''', {"n": z[x][0], "t": r[y][0]} )
                    m1 = cursor.fetchall()
                

                    m2 = cursor.execute('''
                    SELECT COUNT(w.mid) 
                    FROM watch w
                    INNER JOIN sessions s
                    ON w.sid = s.sid
                    WHERE w.cid = :n
                    AND w.mid = :t;
                    ''', {"n": z[x][0], "t": r[y][1]} )
                    m2 = cursor.fetchall()
                    
                    
                    count = int((m1[0][0] + m2[0][0]) / 2)
                    if (count < 1):
                        count = 0
                    new[y].append(count)
            
                  
            for x in range (len(new)):
                lst[x].append(sum(new[x]))
            
            lst.sort(key = lambda x: x[3], reverse=True)  
            
            for x in range(len(lst)):
                print(f"M1: {lst[x][0]}, M2: {lst[x][1]}, # of Customers watched: {lst[x][3]}, score: {lst[x][2]}")
            
            while True:
                choice2 = input("Do you want to (1) search a different list, (2) update a pair, or (3) leave? ")
                if (choice2 == '1'):
                    break
                elif(choice2 == '2'):
                    while True:
                        choice3 = input("Do you want to (1) update a score, (2) delete a pair, (3) add a pair? ")
                        if(choice3 == '1'):
                            while True:
                                i1 = input("Enter your m1 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE watched = :n''', {"n": i1})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M1 does not exist in lists")
                            while True:
                                i2 = input("Enter your m2 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE recommended = :n''', {"n": i2})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M2 does not exist in lists")

                            while True:
                                try:
                                    score = float(input("What score would you like to input (0 < score < 1)? "))
                                    assert(0 < score < 1)
                                    break
                                except:
                                    print("Invalid input")
                            
                            cursor.execute('''
                            UPDATE recommendations
                            SET score = :n
                            WHERE watched = :w
                            AND recommended = :r
                             ''', {"n": score, "w": i1, "r": i2})
                            
                            print("Pair updated.")
                            break

                        elif(choice3 == '2'):
                            while True:
                                i1 = input("Enter your m1 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE watched = :n''', {"n": i1})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M1 does not exist in lists")
                            while True:
                                i2 = input("Enter your m2 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE recommended = :n''', {"n": i2})
                                r = r.fetchone()
                                if (r != None):
                                    break
                                else:
                                    print("M2 does not exist in lists")
                            
                            cursor.execute('''
                            DELETE 
                            FROM recommendations
                            WHERE watched = :w
                            AND recommended = :r
                             ''', {"w": i1, "r": i2})
                            
                            print("Pair Deleted.")
                            break
                        elif(choice3 == '3'):
                            while True:
                                i1 = input("Enter your m1 movie id: ")
                                i2 = input("Enter your m2 movie id: ")
                                r = cursor.execute(''' 
                                SELECT *
                                FROM recommendations
                                WHERE watched = :n
                                AND recommeded = :r''', {"n": i1, "r": i2})
                                r = r.fetchone()
                                if (r != None):
                                    print("Pair already exist in lists")
                                else:
                                    break
                                
                            while True:
                                try:
                                    score = float(input("What score would you like to input (0 < score < 1)? "))
                                    assert(0 < score < 1)
                                    break
                                except:
                                    print("Invalid input")

                            cursor.execute(''' 
                            insert into recommendations values (:w, :r, :s);
                            ''', {"w": i1, "r": i2, "s": score})

                            print("Pair Added.")
                            break      
                                  
                        else:
                            print("Invalid input")
                elif(choice2 == '3'):
                    break
                else:
                    print("Invalid input")
        
        elif(choice == '4'):
            break
        else:
            print("Incorrect input")
            continue

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

if __name__=="__main__":
    # path = get_path()
    # connect(path)
    
    # login_screen()
    # search()
    # display_one_result(80, True)
    # print(start_watch())
    # follow('c100', 40)
    # end_watch(12, 'c100', 80, '2021-08-23 02:34:56')
    # add_movie()
    # date = start_session('c100')
    # mid = search()
    # end_session(19, mid, date)
    # update_recommendation()
    main()

    # connection.commit()
    # connection.close()