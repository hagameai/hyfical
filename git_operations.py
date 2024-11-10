import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initialize the GitOperations with the path to the repository.
        :param repo_path: Path to the git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Run a shell command in the repository.
        :param command: Command to run.
        :return: Output of the command.
        """
        try:
            result = subprocess.run(command, cwd=self.repo_path, text=True, capture_output=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr

    def clone(self, repo_url):
        """
        Clone a git repository.
        :param repo_url: URL of the repository to clone.
        """
        return self.run_command(['git', 'clone', repo_url])

    def pull(self):
        """
        Pull the latest changes from the remote repository.
        """
        return self.run_command(['git', 'pull'])

    def commit(self, message):
        """
        Commit changes to the repository with a message.
        :param message: Commit message.
        """
        return self.run_command(['git', 'commit', '-m', message])

    def push(self):
        """
        Push local commits to the remote repository.
        """
        return self.run_command(['git', 'push'])
