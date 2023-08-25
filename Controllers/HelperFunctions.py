from typing import Union
import config

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
        {"word": '%' + word + '%'}
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
        {"word": '%' + word + '%'}
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
        {"word": '%' + word + '%'}
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
                if mid_list[i][0] == mid[0]:       # if yes, increase count
                    found = True
                    mid_list[i][1] += count
                    break
            if not found:           # if not, append new sub list
                mid_list.append([mid[0], count])

    return mid_list

def has_watched(cid: str, mid: int, runtime: int) -> bool:
    '''
    This function tells if the customer with the given cid has watched
    the movie with the given mid or not.
    Returns True if the customer has watched the movie, False otherwise.
    '''
    config.cursor.execute(
        '''SELECT SUM(duration) FROM watch WHERE cid=:cid AND mid=:mid''',
        {"cid": cid, "mid": mid}
    )

    time_watched = config.cursor.fetchone()[0]

    if time_watched != None and time_watched / runtime > 0.5: return True
    return False