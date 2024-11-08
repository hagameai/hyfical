import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations instance.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Runs a shell command in the Git repository.
        :param command: Command to execute.
        """
        full_command = f'git {command}'
        result = subprocess.run(full_command, shell=True, cwd=self.repo_path,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

    def clone(self, repo_url):
        """
        Clones a Git repository.
        :param repo_url: URL of the repository to clone.
        """
        return self.run_command(f'clone {repo_url}')

    def commit(self, message):
        """
        Commits changes to the repository.
        :param message: Commit message.
        """
        return self.run_command(f'commit -m "{message}"')

    def push(self):
        """
        Pushes changes to the remote repository.
        """
        return self.run_command('push')

    def pull(self):
        """
        Pulls changes from the remote repository.
        """
        return self.run_command('pull')

    def status(self):
        """
        Shows the status of the repository.
        """
        return self.run_command('status')
