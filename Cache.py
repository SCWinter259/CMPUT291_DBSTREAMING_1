class Cache:
    def __init__(self):
        '''
        A cache object to cache all kinds of data to communicate between functions
        As a principle, this object only has getters and setters
        '''
        # for caching current user (Customer or Editor object)
        self.user = None
        # for caching current session (Session object)
        self.session = None

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_session(self):
        return self.session

    def set_session(self, session):
        self.session = session