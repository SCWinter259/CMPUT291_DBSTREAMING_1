class Editor:
    def __init__(self):
        self.eid = None
        self.pwd = None

    def add_movie(self):
        pass

    def update_recommendation(self):
        pass

    def login(self):
        pass

    def logout(self):
        pass

    def signup(self):
        pass

    def is_customer(self):
        return False

    def get_eid(self):
        return self.eid

    def get_pwd(self):
        return self.pwd

    def set_eid(self, eid):
        self.eid = eid

    def set_pwd(self, pwd):
        self.pwd = pwd