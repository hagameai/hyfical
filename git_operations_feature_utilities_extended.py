import os
import subprocess

class GitOperationsFeatureUtilities:
    """
    A utility class to enhance Git operations with additional features.
    This includes methods for checking the status of the repository,
    fetching remote branches, and more.
    """

    @staticmethod
    def check_status():
        """
        Check the current status of the Git repository.
        Returns the status output.
        """
        try:
            status = subprocess.check_output(['git', 'status'], stderr=subprocess.STDOUT)
            return status.decode('utf-8')
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error checking status: {e.output.decode('utf-8')}")

    @staticmethod
    def fetch_remote_branches():
        """
        Fetch all remote branches from the repository.
        Returns the output of the fetch command.
        """
        try:
            fetch_output = subprocess.check_output(['git', 'fetch'], stderr=subprocess.STDOUT)
            return fetch_output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error fetching remote branches: {e.output.decode('utf-8')}")

    @staticmethod
    def get_current_branch():
        """
        Get the name of the current branch.
        Returns the branch name as a string.
        """
        try:
            branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stderr=subprocess.STDOUT)
            return branch_name.decode('utf-8').strip()
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error getting current branch: {e.output.decode('utf-8')}")
