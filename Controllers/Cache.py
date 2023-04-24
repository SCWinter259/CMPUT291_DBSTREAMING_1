class Cache:
    def __init__(self):
        '''
        A cache object to cache all kinds of data to communicate between functions
        As a principle, this object only has getters and setters
        Attributes:
        user - Stores a Customer or Editor object
        session - Stores a Session object
        '''
        self.user = None
        self.session = None

    # getters
    def get_user(self): return self.user
    def get_session(self): return self.session

    # setters
    def set_user(self, user): self.user = user
    def set_session(self, session): self.session = session