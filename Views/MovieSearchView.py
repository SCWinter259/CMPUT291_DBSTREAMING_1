def movie_search_view() -> str:
    '''
    This view is for the customer to search for a movie.

    This view has a text field which serves as a search bar, a search button, and a logout
    button.

    All requirements for searching and string matching in this view are taken care of by the
    search engine written in the QueryFunctions file. 

    When the search button is clicked, if there is no result, this view should display a
    message accordingly. If there are results, they should be displayed 5 items at a time,
    along with a button saying 'Show more results'. When this button is clicked, 5 more
    results will be displayed (if there are less than 5 more, display all results that are 
    left to display). This button should only appear if there are more results left.

    Each of the result should be displayed with its title, year, duration, and a button
    saying 'More information'. When this button is clicked, the view should return 'movie_info_view'.

    If the logout button is clicked, the view should clear the cache, log the user out, and
    return 'login_view'.

    You may want to use search() and logout() functions.
    '''