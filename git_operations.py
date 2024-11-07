import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations such as clone, commit, push, and pull.
    """

    def __init__(self, repo_path):
        """
        Initialize the GitOperations with the repository path.
        """
        self.repo_path = repo_path

    def clone(self, repo_url):
        """
        Clone a Git repository from the given URL.
        :param repo_url: The URL of the repository to clone.
        """
        subprocess.run(['git', 'clone', repo_url], check=True)

    def commit(self, message):
        """
        Commit changes in the repository with the provided message.
        :param message: The commit message.
        """
        os.chdir(self.repo_path)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)

    def push(self):
        """
        Push committed changes to the remote repository.
        """
        os.chdir(self.repo_path)
        subprocess.run(['git', 'push'], check=True)

    def pull(self):
        """
        Pull the latest changes from the remote repository.
        """
        os.chdir(self.repo_path)
        subprocess.run(['git', 'pull'], check=True)