import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with a repository path.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path

    def clone_repo(self, repo_url):
        """
        Clones a repository from the given URL.
        :param repo_url: URL of the repository to clone
        """
        subprocess.run(['git', 'clone', repo_url], cwd=self.repo_path)

    def commit_changes(self, message):
        """
        Commits changes in the repository with the given message.
        :param message: Commit message
        """
        subprocess.run(['git', 'add', '.'], cwd=self.repo_path)
        subprocess.run(['git', 'commit', '-m', message], cwd=self.repo_path)

    def push_changes(self):
        """
        Pushes committed changes to the remote repository.
        """
        subprocess.run(['git', 'push'], cwd=self.repo_path)

    def pull_changes(self):
        """
        Pulls changes from the remote repository.
        """
        subprocess.run(['git', 'pull'], cwd=self.repo_path)