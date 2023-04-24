import System.config as config
import sqlite3

class Session:
    def __init__(self):
        self.sid = None
        self.cid = None
        self.sdate = None
        self.stime = None       # stime is a special variable, born just for the sake of calculation
        self.duration = None

    def start(self):
        '''
        starts a session given the cid. Store the session's information
        into the database with a duration of NULL
        '''

    def end(self):
        pass

    # getters
    def get_sid(self): return self.sid
    def get_cid(self): return self.cid
    def get_sdate(self): return self.sdate
    def get_stime(self): return self.stime
    def get_duration(self): return self.duration

    # setters
    def set_sid(self, sid): self.sid = sid
    def set_cid(self, cid): self.cid = cid
    def set_sdate(self, sdate): self.sdate = sdate
    def set_stime(self, stime): self.stime = stime
    def set_duration(self, duration): self.duration = duration