class Movie:
    def __init__(self):
        self.title = None
        self.year = None
        self.runtime = None

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_runtime(self):
        return self.runtime

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_runtime(self, runtime):
        self.runtime = runtime