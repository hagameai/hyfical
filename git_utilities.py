import os
import subprocess

class GitUtilities:
    """
    A utility class for advanced Git operations.
    This class provides additional functionalities such as checking the status,
    creating branches, and merging branches in a Git repository.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitUtilities with the path to the repository.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path

    def check_status(self):
        """
        Checks the status of the repository.
        :return: Output of the git status command
        """
        try:
            output = subprocess.check_output(['git', 'status'], cwd=self.repo_path, text=True)
            return output
        except subprocess.CalledProcessError as e:
            return f"Error checking status: {e.output}"

    def create_branch(self, branch_name):
        """
        Creates a new branch in the repository.
        :param branch_name: Name of the new branch
        :return: Output of the git branch command
        """
        try:
            subprocess.check_call(['git', 'checkout', '-b', branch_name], cwd=self.repo_path)
            return f'Branch {branch_name} created successfully.'
        except subprocess.CalledProcessError as e:
            return f"Error creating branch: {e.output}"

    def merge_branch(self, branch_name):
        """
        Merges the specified branch into the current branch.
        :param branch_name: Name of the branch to merge
        :return: Output of the git merge command
        """
        try:
            subprocess.check_call(['git', 'merge', branch_name], cwd=self.repo_path)
            return f'Merged branch {branch_name} successfully.'
        except subprocess.CalledProcessError as e:
            return f"Error merging branch: {e.output}"
