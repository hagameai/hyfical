import os
import subprocess

class GitHelper:
    """
    A class to provide additional Git functionalities such as checking the status,
    getting the log, and performing a pull operation.
    """

    def __init__(self, repo_path):
        """
        Initializes GitHelper with the given repository path.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path

    def check_status(self):
        """
        Checks the status of the current Git repository.
        :return: Output of the git status command
        """
        try:
            result = subprocess.run(['git', 'status'], cwd=self.repo_path,
                                     capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error checking status: {e.stderr}'

    def get_log(self, n=5):
        """
        Retrieves the last n commits from the Git log.
        :param n: Number of commits to retrieve
        :return: Output of the git log command
        """
        try:
            result = subprocess.run(['git', 'log', f'-n{n}'], cwd=self.repo_path,
                                     capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error retrieving log: {e.stderr}'

    def pull(self):
        """
        Pulls the latest changes from the remote repository.
        :return: Output of the git pull command
        """
        try:
            result = subprocess.run(['git', 'pull'], cwd=self.repo_path,
                                     capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error during pull: {e.stderr}'
