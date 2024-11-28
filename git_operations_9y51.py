import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations including clone, commit, push, and pull.
    """

    def __init__(self, repo_url, local_dir):
        """
        Initialize the GitOperations with repository URL and local directory.
        """
        self.repo_url = repo_url
        self.local_dir = local_dir

    def clone_repo(self):
        """
        Clone the repository from the given URL to the local directory.
        """
        if not os.path.exists(self.local_dir):
            subprocess.run(['git', 'clone', self.repo_url, self.local_dir], check=True)
        else:
            print(f'Repository already exists at {self.local_dir}.')

    def commit_changes(self, message):
        """
        Commit changes in the local repository with a given message.
        """
        os.chdir(self.local_dir)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)

    def push_changes(self):
        """
        Push local commits to the remote repository.
        """
        os.chdir(self.local_dir)
        subprocess.run(['git', 'push'], check=True)

    def pull_changes(self):
        """
        Pull updates from the remote repository to the local repository.
        """
        os.chdir(self.local_dir)
        subprocess.run(['git', 'pull'], check=True)