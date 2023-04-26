class Session:
    def __init__(self):
        self.sid = None
        self.cid = None
        self.stime = None
        self.etime = None
        self.duration = None

    def start(self):
        '''
        starts a session given the cid. Store the session's information
        into the database with a duration of NULL
        '''

    def end(self):
        pass

    # getters
    def get_sid(self) -> int: return self.sid
    def get_cid(self) -> str: return self.cid
    def get_stime(self) -> str: return self.stime
    def get_etime(self) -> str: return self.etime
    def get_duration(self) -> int: return self.duration

    # setters
    def set_sid(self, sid:int): self.sid = sid
    def set_cid(self, cid:str): self.cid = cid
    def set_stime(self, stime:str): self.stime = stime
    def set_etime(self, etime:str): self.etime = etime
    def set_duration(self, duration:int): self.duration = duration