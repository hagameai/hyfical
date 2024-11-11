import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initialize with the path to the Git repository.
        """
        self.repo_path = repo_path

    def clone_repo(self, repo_url):
        """
        Clone a Git repository from the given URL.
        """
        subprocess.run(['git', 'clone', repo_url], cwd=self.repo_path)

    def commit_changes(self, message):
        """
        Commit changes in the repository with a provided message.
        """
        subprocess.run(['git', 'add', '.'], cwd=self.repo_path)
        subprocess.run(['git', 'commit', '-m', message], cwd=self.repo_path)

    def push_changes(self):
        """
        Push committed changes to the remote repository.
        """
        subprocess.run(['git', 'push'], cwd=self.repo_path)

    def pull_changes(self):
        """
        Pull changes from the remote repository.
        """
        subprocess.run(['git', 'pull'], cwd=self.repo_path)

    def get_status(self):
        """
        Get the current status of the repository.
        """
        result = subprocess.run(['git', 'status'], cwd=self.repo_path, capture_output=True, text=True)
        return result.stdout
