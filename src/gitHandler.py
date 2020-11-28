from github import Github
import MongoController
from repo import Repo


class GitHandler:

    def __init__(self, access):
        self.gAuth = Github(access).get_user()

        self.repos = self.list_repos()
        self.status = "{repo} has been updated with commit {id} by {author} with message {message} \n" \
                      "Link: {link} \n" \
                      "Automated with PyGitBot"

    def get_one(self, n_repo):
        name = self.gAuth.get_repo(self.repos[n_repo])
        identifiers = name.get_commits()
        last_commit = identifiers[0].sha
        link = name.html_url
        try:
            author = name.get_commit(last_commit).author.login
        except AttributeError:
            author = self.gAuth.login
        message = name.get_commit(last_commit)

        message = name.get_commit(last_commit).commit.message

        return Repo(name, last_commit, author, message, link)

    def list_repos(self):
        repos = []
        for repo in self.gAuth.get_repos():
            repos.append(repo.name)
        return repos
