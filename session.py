class Session:
    def __init__(self):
        self.sid = None
        self.cid = None
        self.sdate = None
        self.duration = None

    def start(self):
        pass

    def end(self):
        pass

    def get_sid(self):
        return self.sid

    def get_cid(self):
        return self.cid

    def get_sdate(self):
        return self.sdate

    def get_duration(self):
        return self.duration

    def set_sid(self, sid):
        self.sid = sid

    def set_cid(self, cid):
        self.cid = cid

    def set_duration(self, duration):
        self.duration = duration