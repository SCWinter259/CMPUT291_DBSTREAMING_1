class Movie:
    def __init__(self, mid: int, title: str, year: int, runtime: int):
        self.mid = mid
        self.title = title
        self.year = year
        self.runtime = runtime

    # getters
    def get_mid(self) -> int: return self.mid
    def get_title(self) -> str: return self.title
    def get_year(self) -> int: return self.year
    def get_runtime(self) -> int: return self.runtime

    # setters
    def set_mid(self, mid: int): self.mid = mid
    def set_title(self, title: str): self.title = title
    def set_year(self, year: int): self.year = year
    def set_runtime(self, runtime: int): self.runtime = runtime