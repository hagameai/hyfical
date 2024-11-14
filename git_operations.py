import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initialize with the path to the repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Run a shell command in the repository.
        """
        result = subprocess.run(command, shell=True, cwd=self.repo_path,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        return result.stdout, result.stderr

    def clone(self, repo_url):
        """
        Clone a Git repository from the given URL.
        """
        command = f'git clone {repo_url}'
        return self.run_command(command)

    def pull(self):
        """
        Pull the latest changes from the remote repository.
        """
        command = 'git pull'
        return self.run_command(command)

    def commit(self, message):
        """
        Commit changes with a given commit message.
        """
        command = f'git commit -m "{message}"'
        return self.run_command(command)

    def push(self):
        """
        Push local changes to the remote repository.
        """
        command = 'git push'
        return self.run_command(command)

    def status(self):
        """
        Get the status of the repository.
        """
        command = 'git status'
        return self.run_command(command)