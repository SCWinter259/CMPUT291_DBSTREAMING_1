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
    print("session is: " + str(sid))
    cursor.execute('''INSERT INTO watch VALUES (:sid, :cid, :mid, :time_watched)''',
                    {"sid":sid, "cid":cid, "mid": mid, "time_watched":time_watched})
    connection.commit()
    print("Your watch has ended")