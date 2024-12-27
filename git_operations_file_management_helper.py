import os
import subprocess

class GitFileManagementHelper:
    """
    A class to provide additional helper methods for Git file management.
    This class includes methods for checking the status of files,
    adding files to staging, and committing changes.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitFileManagementHelper with the path to the Git repository.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path
        if not os.path.isdir(repo_path):
            raise ValueError(f"The provided path '{repo_path}' is not a valid directory.")

    def check_status(self):
        """
        Checks the status of the Git repository.
        :return: Output of the `git status` command
        """
        try:
            result = subprocess.run(['git', 'status'], cwd=self.repo_path, text=True,
                                    capture_output=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error checking Git status: {e.stderr}")

    def add_file(self, file_name):
        """
        Adds a file to the staging area.
        :param file_name: The name of the file to add
        """
        try:
            result = subprocess.run(['git', 'add', file_name], cwd=self.repo_path,
                                    text=True, capture_output=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error adding file '{file_name}': {e.stderr}")

    def commit_changes(self, message):
        """
        Commits the staged changes with a provided commit message.
        :param message: Commit message
        """
        try:
            result = subprocess.run(['git', 'commit', '-m', message], cwd=self.repo_path,
                                    text=True, capture_output=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error committing changes: {e.stderr}")

    def get_log(self):
        """
        Retrieves the Git commit log.
        :return: Output of the `git log` command
        """
        try:
            result = subprocess.run(['git', 'log'], cwd=self.repo_path, text=True,
                                    capture_output=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error retrieving log: {e.stderr}")
