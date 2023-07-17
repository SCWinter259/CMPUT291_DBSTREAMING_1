def search(text: str) -> list:
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
    # get the list of keywords, all in lowercase
    keywords = list(set(_chop(text)))
    keywords = [word.lower() for word in keywords]  

    print(keywords)


    # for each keyword
        # find mids with title matches
        # find pids of movie people matches in moviePeople table
        # mids based on pids (casts table)
        # find mid based on role (casts table)

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

    print(text.split())

    return text.split()

search("Spider man ?, abcd:, fjksal  ,,casper")