import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initialize GitOperations with the path to the repository.
        :param repo_path: Path to the local Git repository.
        """
        self.repo_path = repo_path

    def execute_command(self, command):
        """
        Execute a shell command in the repository directory.
        :param command: Command to be executed.
        :return: Output of the command.
        """
        try:
            result = subprocess.run(command, cwd=self.repo_path, 
                                    shell=True, check=True, 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr

    def clone(self, repo_url):
        """
        Clone a remote repository to the local path.
        :param repo_url: URL of the remote repository.
        """
        command = f'git clone {repo_url}'
        return self.execute_command(command)

    def pull(self):
        """
        Pull the latest changes from the remote repository.
        """
        command = 'git pull'
        return self.execute_command(command)

    def commit(self, message):
        """
        Commit changes in the repository with a message.
        :param message: Commit message.
        """
        command = f'git commit -m "{message}"'
        return self.execute_command(command)

    def push(self):
        """
        Push local changes to the remote repository.
        """
        command = 'git push'
        return self.execute_command(command)

    def status(self):
        """
        Get the current status of the repository.
        :return: Status output.
        """
        command = 'git status'
        return self.execute_command(command)