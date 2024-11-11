import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with the repository path.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Runs a shell command in the context of the repository.
        :param command: Command to run.
        :return: Output of the command.
        """
        result = subprocess.run(command, shell=True, cwd=self.repo_path,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        if result.returncode != 0:
            raise Exception(f'Error: {result.stderr}')
        return result.stdout

    def clone(self, repo_url):
        """
        Clones a repository from a given URL.
        :param repo_url: URL of the repository to clone.
        """
        command = f'git clone {repo_url}'
        return self.run_command(command)

    def pull(self):
        """
        Pulls the latest changes from the remote repository.
        """
        command = 'git pull'
        return self.run_command(command)

    def status(self):
        """
        Returns the status of the repository.
        :return: Status of the repository.
        """
        command = 'git status'
        return self.run_command(command)