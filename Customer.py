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
        pass

    def logout(self):
        pass

    def signup(self):
        pass

    def get_cid(self):
        return self.cid
    
    def get_name(self):
        return self.name

    def get_pwd(self):
        return self.pwd

    def set_cid(self, cid):
        self.cid = cid

    def set_name(self, name):
        self.name = name

    def set_pwd(self, pwd):
        self.pwd = pwd