import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with the given repository path.
        :param repo_path: Path to the local Git repository.
        """
        self.repo_path = repo_path

    def clone_repo(self, repo_url):
        """
        Clones a Git repository from the given URL.
        :param repo_url: URL of the Git repository to clone.
        """
        subprocess.run(['git', 'clone', repo_url, self.repo_path], check=True)

    def commit_changes(self, message):
        """
        Commits changes in the repository with the provided message.
        :param message: Commit message.
        """
        subprocess.run(['git', 'add', '.'], cwd=self.repo_path, check=True)
        subprocess.run(['git', 'commit', '-m', message], cwd=self.repo_path, check=True)

    def push_changes(self):
        """
        Pushes committed changes to the remote repository.
        """
        subprocess.run(['git', 'push'], cwd=self.repo_path, check=True)

    def pull_changes(self):
        """
        Pulls changes from the remote repository to the local repository.
        """
        subprocess.run(['git', 'pull'], cwd=self.repo_path, check=True)