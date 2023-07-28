def movie_info_view() -> str:
    '''
    This view is for the customer to see imformation about the movie.

    This view has a back button, a watch movie button, a follow cast member button,
    a logout button.

    This view has to show the following information:
    - Movie title
    - Release year
    - Duration
    - List of names of cast members and their roles

    When the back button is clicked, the view returns 'movie_search_view'.
    When the watch movie button is clicked, the view caches the movie,
    then returns 'watch_movie_view'.
    When the follow cast member button is clicked, the view caches the cast
    member, then returns 'follow_cast_member_view'.
    When the logout button is clicked, the view reset the cache, log the user out,
    and returns 'login_view'.

    You may want to use find_cast(), count_customer_watched(), logout()
    '''