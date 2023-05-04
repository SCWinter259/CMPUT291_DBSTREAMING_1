from Controllers.Cache import Cache
from Views.LoginView import login_view
from Views.RegisterView import register_view
from Views.GeneralEditorView import general_editor_view
from Views.MovieSearchView import movie_search_view
from Views.MovieInfoView import movie_info_view
from Views.WatchMovieView import watch_movie_view
from Views.FollowCastMemberView import follow_cast_member_view

class SysStack:
    def __init__(self):
        '''
        This is a stack to control the flow of the whole program. By implementing this,
        a back function is no longer necessary.
        The function name at the end of the call stack will always be the name of the
        function to be called!
        '''
        self.stack = []
        self.cache = None

        self.all_views = {
            "exit": exit(),
            "login_view": login_view(self.cache),
            "register_view": register_view(self.cache),
            "general_editor_view": general_editor_view(self.cache),
            "movie_search_view": movie_search_view(self.cache),
            "movie_info_view": movie_info_view(self.cache),
            "watch_movie_view": watch_movie_view(self.cache),
            "follow_cast_member_view": follow_cast_member_view(self.cache)
        }

    def add(self, func_name):
        self.stack.append(func_name)

    def remove(self):
        self.stack.pop()

    def peek(self) -> function:
        return self.stack[-1]

    def see_stack(self) -> list:
        return self.stack       # for debugging
    
    def set_cache(self, cache:Cache): self.cache = cache

    def control(self, func_name):
        '''
        This method receives function name and checks is the function is already in the stack.
        If yes, pop all function names after it. If no, add it to the end.
        '''
        if func_name in self.stack:
            while(self.peek() != func_name):
                self.remove()
        else:
            self.add(func_name)

    def get_next_function(self) -> function: return self.all_views[self.peek()]