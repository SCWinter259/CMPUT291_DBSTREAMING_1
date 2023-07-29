class Session:
    def __init__(self, sid: int, cid: str, stime: str):
        self.sid = sid
        self.cid = cid
        self.stime = stime

    def end(self):
        pass

    # getters
    def get_sid(self) -> int: return self.sid
    def get_cid(self) -> str: return self.cid
    def get_stime(self) -> str: return self.stime

    # setters
    def set_sid(self, sid: int): self.sid = sid
    def set_cid(self, cid: str): self.cid = cid
    def set_stime(self, stime: str): self.stime = stime