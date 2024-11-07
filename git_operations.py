import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with the given repository path.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Runs a shell command in the repository path.
        :param command: Command to be executed.
        """
        result = subprocess.run(command, cwd=self.repo_path, shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True)
        return result.stdout, result.stderr

    def clone(self, repo_url):
        """
        Clones a Git repository from the given URL.
        :param repo_url: URL of the repository to clone.
        """
        command = f'git clone {repo_url}'
        return self.run_command(command)

    def commit(self, message):
        """
        Commits changes in the repository with a given message.
        :param message: Commit message.
        """
        command = f'git commit -m "{message}"'
        return self.run_command(command)

    def push(self, branch='main'):
        """
        Pushes changes to the specified branch.
        :param branch: Branch to push changes to.
        """
        command = f'git push origin {branch}'
        return self.run_command(command)

    def pull(self, branch='main'):
        """
        Pulls changes from the specified branch.
        :param branch: Branch to pull changes from.
        """
        command = f'git pull origin {branch}'
        return self.run_command(command)
