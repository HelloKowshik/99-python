class GithubRepo:
    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self):
        return f"-> {self.name} is a {self.language} Repo With {self.num_stars} Stars"

    def __repr__(self):
        return f"GithubRepo({self.name}, {self.language}, {self.num_stars})"

