import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with the path to the repository.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Runs a shell command in the context of the repository.
        :param command: The command to run.
        :return: Output of the command.
        """
        result = subprocess.run(command, cwd=self.repo_path, shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise Exception(f"Error: {result.stderr.decode().strip()}")
        return result.stdout.decode().strip()

    def clone(self, repo_url):
        """
        Clones a Git repository from the given URL.
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

    def commit(self, message):
        """
        Commits changes to the repository with the given message.
        :param message: The commit message.
        """
        command = f'git commit -m "{message}"'
        return self.run_command(command)

    def push(self):
        """
        Pushes local commits to the remote repository.
        """
        command = 'git push'
        return self.run_command(command)

    def status(self):
        """
        Returns the status of the repository.
        :return: Status output.
        """
        command = 'git status'
        return self.run_command(command)