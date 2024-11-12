import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations such as clone, pull, and commit.
    """

    def __init__(self, repo_url, local_dir):
        """
        Initializes the GitOperations with the repository URL and local directory.
        :param repo_url: URL of the Git repository
        :param local_dir: Local directory to clone the repository into
        """
        self.repo_url = repo_url
        self.local_dir = local_dir

    def clone(self):
        """
        Clones the specified repository into the local directory.
        """
        subprocess.run(['git', 'clone', self.repo_url, self.local_dir], check=True)

    def pull(self):
        """
        Pulls the latest changes from the remote repository.
        """
        os.chdir(self.local_dir)
        subprocess.run(['git', 'pull'], check=True)

    def commit(self, message):
        """
        Commits changes in the local repository with the specified message.
        :param message: Commit message
        """
        os.chdir(self.local_dir)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)

    def push(self):
        """
        Pushes committed changes to the remote repository.
        """
        os.chdir(self.local_dir)
        subprocess.run(['git', 'push'], check=True)
