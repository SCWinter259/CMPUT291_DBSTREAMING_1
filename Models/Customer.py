class Customer:
    def __init__(self):
        self.cid = None
        self.name = None
        self.pwd = None
    
    def search(self):
        pass

    def select_movie(self):
        pass

    def see_more(self):
        pass

    def follow(self):
        pass

    def start_watch(self):
        pass

    def end_watch(self):
        pass

    def login(self):
        '''
        starts a session (and maybe do something else)
        '''
        pass

    def logout(self):
        '''
        ends a session (and maybe do something else)
        '''
        pass

    def is_customer(self) -> bool: return True

    # getters
    def get_cid(self) -> str: return self.cid
    def get_name(self) -> str: return self.name
    def get_pwd(self) -> str: return self.pwd

    # setters
    def set_cid(self, cid:str): self.cid = cid
    def set_name(self, name:str): self.name = name
    def set_pwd(self, pwd:str): self.pwd = pwd