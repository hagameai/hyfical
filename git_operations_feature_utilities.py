import os
import subprocess

class GitOperationsUtilities:
    """
    A utility class for performing various Git operations
    such as cloning repositories, fetching updates, and more.
    """

    @staticmethod
    def clone_repository(repo_url: str, destination: str) -> bool:
        """
        Clone a Git repository to a specified destination.
        :param repo_url: URL of the Git repository to clone.
        :param destination: Local path where the repository should be cloned.
        :return: True if successful, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'clone', repo_url, destination])
            return True
        except subprocess.CalledProcessError as e:
            print(f'Error cloning repository: {e}')
            return False

    @staticmethod
    def fetch_updates(repo_path: str) -> bool:
        """
        Fetch updates from the remote repository.
        :param repo_path: Local path of the Git repository.
        :return: True if successful, False otherwise.
        """
        try:
            subprocess.check_call(['git', '-C', repo_path, 'fetch'])
            return True
        except subprocess.CalledProcessError as e:
            print(f'Error fetching updates: {e}')
            return False

    @staticmethod
    def status(repo_path: str) -> str:
        """
        Get the current status of the Git repository.
        :param repo_path: Local path of the Git repository.
        :return: Status message from Git.
        """
        try:
            status_output = subprocess.check_output(['git', '-C', repo_path, 'status'], text=True)
            return status_output
        except subprocess.CalledProcessError as e:
            return f'Error getting status: {e}'