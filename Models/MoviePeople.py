from tkinter import N


class MoviePeople:
    def __init__(self, pid: str, name: str, birthYear: int):
        self.pid = pid
        self.name = name
        self.birthYear = birthYear

    # getters
    def get_pid(self) -> str: return self.pid
    def get_name(self) -> str: return self.name
    def get_birthYear(self) -> int: return self.birthYear

    # setters
    def set_pid(self, pid: str): self.pid = pid
    def set_name(self, name: str): self.name = name
    def set_birthYear(self, birthYear: int): self.birthYear = birthYear