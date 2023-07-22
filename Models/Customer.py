class Customer:
    def __init__(self, cid: str, name: str, pwd: str):
        self.cid = cid
        self.name = name
        self.pwd = pwd
        self.selected_mid = None        # used to cache the movie selected for watching or for viewing information
        self.selected_pid = None        # used to cache the cast member selected for following (may not be necessary?)
    
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
    def get_selected_mid(self) -> int: return self.selected_mid
    def get_selected_pid(self) -> str: return self.selected_pid

    # setters
    def set_cid(self, cid: str): self.cid = cid
    def set_name(self, name: str): self.name = name
    def set_pwd(self, pwd: str): self.pwd = pwd
    def set_selected_mid(self, mid: int): self.selected_mid = mid
    def set_selected_pid(self, pid: str): self.selected_pid = pid