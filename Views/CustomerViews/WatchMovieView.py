
def watch_movie_view() -> str:
    '''
    This view is to show the customer that they are watching a movie.

    This view has a text showing the title of the movie the customer is watching,
    a button to stop watching the movie, and a button to logout.

    When the stop watching button is clicked, the watch would be recorded in the
    watch table, the cached movie will be clear, and the view would return 'movie_search_view'.
    When the logout button is clicked, the view would stop the watch and store it in the
    table (just like the stop watching button), but will also clear the cache, store the
    session, and return 'login_view'.

    You may want to use end_watch(), end_session() functions.
    '''