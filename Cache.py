class Cache:
    def __init__(self):
        '''
        A cache object to cache all kinds of data to communicate between functions
        '''
        # for caching current user (Customer or Editor object)
        self.user = None

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user