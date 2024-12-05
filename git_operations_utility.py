import os
import subprocess

class GitOperationsUtility:
    """
    A utility class to enhance Git operations with additional functionalities.
    """

    @staticmethod
    def clone_repository(repo_url, destination):
        """
        Clone a Git repository to a specified destination.
        
        :param repo_url: URL of the repository to clone.
        :param destination: Directory where the repository should be cloned.
        :raises ValueError: If the repo_url or destination is invalid.
        :raises subprocess.CalledProcessError: If cloning fails.
        """
        if not repo_url or not destination:
            raise ValueError('Both repo_url and destination must be provided.')

        try:
            subprocess.run(['git', 'clone', repo_url, destination], check=True)
            print(f'Repository cloned to {destination}.')
        except subprocess.CalledProcessError as e:
            print(f'Error cloning repository: {e}')
            raise

    @staticmethod
    def fetch_updates(repo_path):
        """
        Fetch updates from the remote repository.
        
        :param repo_path: Path to the local Git repository.
        :raises ValueError: If the repo_path is invalid.
        :raises subprocess.CalledProcessError: If fetching fails.
        """
        if not os.path.exists(repo_path):
            raise ValueError('The specified repository path does not exist.')

        try:
            subprocess.run(['git', '-C', repo_path, 'fetch'], check=True)
            print('Updates fetched successfully.')
        except subprocess.CalledProcessError as e:
            print(f'Error fetching updates: {e}')
            raise

    @staticmethod
    def checkout_branch(repo_path, branch_name):
        """
        Checkout a specific branch in the local repository.
        
        :param repo_path: Path to the local Git repository.
        :param branch_name: Name of the branch to checkout.
        :raises ValueError: If the repo_path or branch_name is invalid.
        :raises subprocess.CalledProcessError: If checkout fails.
        """
        if not os.path.exists(repo_path) or not branch_name:
            raise ValueError('Valid repo_path and branch_name must be provided.')

        try:
            subprocess.run(['git', '-C', repo_path, 'checkout', branch_name], check=True)
            print(f'Checked out to branch {branch_name}.')
        except subprocess.CalledProcessError as e:
            print(f'Error checking out branch: {e}')
            raise
