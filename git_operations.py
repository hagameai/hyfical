import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initialize the GitOperations with the path to the repository.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Execute a shell command in the repository directory.
        :param command: Command to execute.
        :return: Output of the command.
        """
        result = subprocess.run(command, cwd=self.repo_path, shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True)
        if result.returncode != 0:
            raise Exception(f'Error: {result.stderr.strip()}')
        return result.stdout.strip()

    def clone(self, repo_url):
        """
        Clone a Git repository.
        :param repo_url: URL of the repository to clone.
        """
        command = f'git clone {repo_url}'
        return self.run_command(command)

    def add(self, file_pattern):
        """
        Add files to the staging area.
        :param file_pattern: Pattern of files to add.
        """
        command = f'git add {file_pattern}'
        return self.run_command(command)

    def commit(self, message):
        """
        Commit changes to the repository.
        :param message: Commit message.
        """
        command = f'git commit -m "{message}"'
        return self.run_command(command)

    def push(self):
        """
        Push changes to the remote repository.
        """
        command = 'git push'
        return self.run_command(command)

    def pull(self):
        """
        Pull changes from the remote repository.
        """
        command = 'git pull'
        return self.run_command(command)