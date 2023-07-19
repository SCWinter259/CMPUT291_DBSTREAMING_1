class Session:
    def __init__(self, sid: int, cid: str, stime: str, etime: str, duration: int):
        self.sid = sid
        self.cid = cid
        self.stime = stime
        self.etime = etime
        self.duration = duration

    def end(self):
        pass

    # getters
    def get_sid(self) -> int: return self.sid
    def get_cid(self) -> str: return self.cid
    def get_stime(self) -> str: return self.stime
    def get_etime(self) -> str: return self.etime
    def get_duration(self) -> int: return self.duration

    # setters
    def set_sid(self, sid: int): self.sid = sid
    def set_cid(self, cid: str): self.cid = cid
    def set_stime(self, stime: str): self.stime = stime
    def set_etime(self, etime: str): self.etime = etime
    def set_duration(self, duration: int): self.duration = duration