def follow_cast_member_view() -> str:
    '''
    This view is for the user to choose a cast member to follow.

    This view has a back button, a logout button, and for each
    cast member, there is a follow button for each cast member.

    Follow button should be labeled "follow xxx" with xxx being the
    name of the cast member. When the follow button is clicked, there
    should be a notification that the user has successfully followed
    the cast member, or that the user has already followed the cast
    member.

    When the back button is clicked, the view returns 'movie_info_view'.
    When the logout button is clicked, the view reset the cache, log the user out,
    and returns 'login_view'.

    You may want to use follow() and streamlit toast component (for the
    follow notification).
    '''