import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with the path to the repository.
        :param repo_path: Path to the local Git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Runs a Git command in the repository's context.
        :param command: The Git command to run.
        :return: Output of the command.
        """
        try:
            result = subprocess.run(command, cwd=self.repo_path, text=True,
                                    capture_output=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr

    def clone(self, repo_url):
        """
        Clones a repository from a given URL.
        :param repo_url: URL of the repository to clone.
        :return: Output of the clone command.
        """
        return self.run_command(['git', 'clone', repo_url])

    def commit(self, message):
        """
        Commits changes in the repository with a message.
        :param message: Commit message.
        :return: Output of the commit command.
        """
        return self.run_command(['git', 'commit', '-m', message])

    def push(self):
        """
        Pushes changes to the remote repository.
        :return: Output of the push command.
        """
        return self.run_command(['git', 'push'])

    def pull(self):
        """
        Pulls changes from the remote repository.
        :return: Output of the pull command.
        """
        return self.run_command(['git', 'pull'])

    def status(self):
        """
        Gets the status of the repository.
        :return: Output of the status command.
        """
        return self.run_command(['git', 'status'])

    def log(self):
        """
        Gets the commit log of the repository.
        :return: Output of the log command.
        """
        return self.run_command(['git', 'log'])

    def add(self, file_path):
        """
        Adds a file to the staging area.
        :param file_path: Path of the file to add.
        :return: Output of the add command.
        """
        return self.run_command(['git', 'add', file_path])
