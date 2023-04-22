import System.config as config
import sqlite3

class Session:
    def __init__(self):
        self.sid = None
        self.cid = None
        self.sdate = None
        # stime is a special variable, born just for the sake of calculation,
        # so it will be sotred as a tuple (used in end session)
        self.stime = None
        self.duration = None

    def start(self):
        '''
        starts a session given the cid. Store the session's information
        into the database with a duration of NULL
        '''
        # mark the starting time
        config.cursor.execute('''SELECT datetime('now')''')
        self.set_stime(config.cursor.fetchone())
        # mark the starting date
        config.cursor.execute('''SELECT date('now')''')
        self.set_sdate(config.cursor.fetchone()[0])
        # create a new session id
        config.cursor.execute('''SELECT MAX(sid) FROM sessions''')
        self.set_sid(config.cursor.fetchone()[0] + 1)

        config.cursor.execute('''INSERT INTO sessions VALUES(:sid, :cid, :sdate, NULL)''',
                                    {"sid": self.sid, "cid": self.cid, "sdate": self.sdate})

        config.connection.commit()

    def end(self):
        pass

    def get_sid(self):
        return self.sid

    def get_cid(self):
        return self.cid

    def get_sdate(self):
        return self.sdate

    def get_stime(self):
        return self.stime

    def get_duration(self):
        return self.duration

    def set_sid(self, sid):
        self.sid = sid

    def set_cid(self, cid):
        self.cid = cid

    def set_sdate(self, sdate):
        self.sdate = sdate

    def set_stime(self, stime):
        self.stime = stime

    def set_duration(self, duration):
        self.duration = duration
