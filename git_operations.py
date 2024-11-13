import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with the path to the repository.
        :param repo_path: The path to the git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Executes a git command in the repository.
        :param command: The git command to execute.
        :return: The output of the command.
        """
        result = subprocess.run(command, cwd=self.repo_path, shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 text=True)
        if result.returncode != 0:
            raise Exception(f'Error executing command: {command}\n{result.stderr}')
        return result.stdout

    def clone(self, repo_url):
        """
        Clones a git repository from the given URL.
        :param repo_url: The URL of the repository to clone.
        """
        command = f'git clone {repo_url}'
        self.run_command(command)

    def commit(self, message):
        """
        Commits changes in the repository with the provided message.
        :param message: The commit message.
        """
        self.run_command('git add .')
        command = f'git commit -m "{message}"'
        self.run_command(command)

    def push(self):
        """
        Pushes changes to the remote repository.
        """
        self.run_command('git push')

    def pull(self):
        """
        Pulls changes from the remote repository.
        """
        self.run_command('git pull')

    def status(self):
        """
        Returns the current status of the repository.
        :return: The output of 'git status'.
        """
        return self.run_command('git status')