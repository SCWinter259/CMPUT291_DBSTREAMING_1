from tkinter import N


class MoviePeople:
    def __inti__(self):
        self.pid = None
        self.name = None
        self.birthYear = None

    # getters
    def get_pid(self) -> str: return self.pid
    def get_name(self) -> str: return self.name
    def get_birthYear(self) -> int: return self.birthYear

    # setters
    def set_pid(self, pid:str): self.pid = pid
    def set_name(self, name:str): self.name = name
    def set_birthYear(self, birthYear:int): self.birthYear = birthYear