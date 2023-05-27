from Views.LoginView import login_view
from Views.RegisterView import register_view
from Views.GeneralEditorView import general_editor_view
from Views.MovieSearchView import movie_search_view
from Views.MovieInfoView import movie_info_view
from Views.WatchMovieView import watch_movie_view
from Views.FollowCastMemberView import follow_cast_member_view

views = {
    "login_view": login_view,
    "register_view": register_view,
    "general_editor_view": general_editor_view,
    "movie_search_view": movie_search_view,
    "movie_info_view": movie_info_view,
    "watch_movie_view": watch_movie_view,
    "follow_cast_member_view": follow_cast_member_view
}