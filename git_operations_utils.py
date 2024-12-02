import os
import subprocess

class GitUtils:
    """
    A utility class for performing advanced Git operations.
    """

    @staticmethod
    def clone_repo(repo_url, destination):
        """
        Clones a Git repository to a specified destination.
        
        :param repo_url: URL of the repository to clone.
        :param destination: Directory where the repository will be cloned.
        :raises ValueError: If the repo_url is invalid or cloning fails.
        """
        if not repo_url:
            raise ValueError("Repository URL must not be empty.")
        try:
            subprocess.run(['git', 'clone', repo_url, destination], check=True)
        except subprocess.CalledProcessError as e:
            raise ValueError(f"Failed to clone repository: {e}")

    @staticmethod
    def get_repo_status():
        """
        Retrieves the current status of the Git repository.
        
        :return: The output of 'git status' command.
        """
        try:
            result = subprocess.run(['git', 'status'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error retrieving status: {e}"