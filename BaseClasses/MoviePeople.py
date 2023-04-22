from tkinter import N


class MoviePeople:
    def __inti__(self):
        self.pid = None
        self.name = None
        self.birthYear = None

    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def get_birthYear(self):
        return self.birthYear

    def set_pid(self, pid):
        self.pid = pid

    def set_name(self, name):
        self.name = name

    def set_birthYear(self, birthYear):
        self.birthYear = birthYear