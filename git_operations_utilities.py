import os
import subprocess

class GitUtilities:
    """
    A class that provides utility functions for Git operations.
    """

    @staticmethod
    def check_git_installed():
        """
        Check if Git is installed on the system.
        Raises an error if not installed.
        """
        try:
            subprocess.run(['git', '--version'], check=True, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError:
            raise EnvironmentError('Git is not installed or not found in PATH.')

    @staticmethod
    def init_git_repo(repo_path):
        """
        Initialize a new Git repository at the specified path.
        :param repo_path: Path where the Git repository will be initialized.
        """
        if not os.path.exists(repo_path):
            os.makedirs(repo_path)
        os.chdir(repo_path)
        subprocess.run(['git', 'init'], check=True)

    @staticmethod
    def clone_repo(repo_url, target_path):
        """
        Clone a Git repository from a URL to a target path.
        :param repo_url: URL of the Git repository to clone.
        :param target_path: Path where the repository will be cloned.
        """
        subprocess.run(['git', 'clone', repo_url, target_path], check=True)

    @staticmethod
    def list_branches():
        """
        List all branches in the current Git repository.
        Returns a list of branch names.
        """
        result = subprocess.run(['git', 'branch'], check=True, stdout=subprocess.PIPE)
        branches = result.stdout.decode().splitlines()
        return [branch.strip() for branch in branches]

    @staticmethod
    def checkout_branch(branch_name):
        """
        Switch to the specified branch in the current Git repository.
        :param branch_name: Name of the branch to switch to.
        """
        subprocess.run(['git', 'checkout', branch_name], check=True)