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

    def is_customer(self) -> bool: return False

    # getters
    def get_eid(self) -> str: return self.eid
    def get_pwd(self) -> str: return self.pwd

    # setters
    def set_eid(self, eid:str): self.eid = eid
    def set_pwd(self, pwd:str): self.pwd = pwd