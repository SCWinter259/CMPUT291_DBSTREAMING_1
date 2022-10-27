from watch import end_watch

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