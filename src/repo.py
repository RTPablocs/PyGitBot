class Repo:
    def __init__(self, name, identifier, author, commit, url):
        self.name = name
        self._id = identifier
        self.author = author
        self.commit = commit
        self.url = url
