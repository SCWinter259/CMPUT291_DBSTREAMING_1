from Views.TestView import test_view
from Views.LoginView import login_view
from Views.CustomerViews.RegisterView import register_view
from Views.EditorViews.GeneralEditorView import general_editor_view
from Views.CustomerViews.MovieSearchView import movie_search_view
from Views.CustomerViews.MovieInfoView import movie_info_view
from Views.CustomerViews.WatchMovieView import watch_movie_view
from Views.CustomerViews.FollowCastMemberView import follow_cast_member_view

views = {
    "test_view": test_view,
    "login_view": login_view,
    "register_view": register_view,
    "general_editor_view": general_editor_view,
    "movie_search_view": movie_search_view,
    "movie_info_view": movie_info_view,
    "watch_movie_view": watch_movie_view,
    "follow_cast_member_view": follow_cast_member_view
}