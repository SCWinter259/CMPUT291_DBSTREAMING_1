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