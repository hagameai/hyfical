import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initialize the GitOperations with a repository path.
        """
        self.repo_path = repo_path

    def clone(self, repo_url):
        """
        Clone a git repository from the given URL.
        :param repo_url: URL of the repository to clone
        """
        subprocess.run(['git', 'clone', repo_url], cwd=self.repo_path)

    def add(self, file_path):
        """
        Add a file to the staging area.
        :param file_path: Path of the file to add
        """
        subprocess.run(['git', 'add', file_path], cwd=self.repo_path)

    def commit(self, message):
        """
        Commit the staged changes with a message.
        :param message: Commit message
        """
        subprocess.run(['git', 'commit', '-m', message], cwd=self.repo_path)

    def push(self):
        """
        Push the committed changes to the remote repository.
        """
        subprocess.run(['git', 'push'], cwd=self.repo_path)

    def pull(self):
        """
        Pull the latest changes from the remote repository.
        """
        subprocess.run(['git', 'pull'], cwd=self.repo_path)

    def status(self):
        """
        Get the status of the repository.
        :return: Status output
        """
        return subprocess.run(['git', 'status'], cwd=self.repo_path, capture_output=True, text=True).stdout

    def log(self):
        """
        Get the commit logs of the repository.
        :return: Commit log output
        """
        return subprocess.run(['git', 'log'], cwd=self.repo_path, capture_output=True, text=True).stdout
