import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations class with the repository path.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Runs a shell command in the repository path.
        :param command: Command to run
        :return: Output of the command
        """
        result = subprocess.run(command, shell=True, cwd=self.repo_path,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

    def clone_repo(self, repo_url):
        """
        Clones a Git repository.
        :param repo_url: URL of the repository to clone
        """
        command = f'git clone {repo_url}'
        return self.run_command(command)

    def commit_changes(self, message):
        """
        Commits changes in the repository with a message.
        :param message: Commit message
        """
        command = 'git add . && git commit -m "' + message + '"'
        return self.run_command(command)

    def push_changes(self):
        """
        Pushes changes to the remote repository.
        """
        command = 'git push'
        return self.run_command(command)

    def pull_changes(self):
        """
        Pulls changes from the remote repository.
        """
        command = 'git pull'
        return self.run_command(command)

    def status(self):
        """
        Returns the status of the repository.
        :return: Status output
        """
        command = 'git status'
        return self.run_command(command)