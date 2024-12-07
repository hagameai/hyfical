import os
import subprocess

class GitFeatureOperations:
    """
    A class to encapsulate advanced Git features.
    This includes functionalities like merging branches, checking out branches,
    and viewing commit history.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitFeatureOperations with the path to the repository.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path

    def merge_branches(self, source_branch, target_branch):
        """
        Merges the source branch into the target branch.
        :param source_branch: The branch to merge from
        :param target_branch: The branch to merge into
        :raises RuntimeError: If the merge fails
        """
        try:
            self.checkout_branch(target_branch)
            subprocess.run(['git', 'merge', source_branch], check=True, cwd=self.repo_path)
        except subprocess.CalledProcessError:
            raise RuntimeError(f'Failed to merge {source_branch} into {target_branch}')

    def checkout_branch(self, branch_name):
        """
        Checks out the specified branch.
        :param branch_name: The branch to check out
        :raises RuntimeError: If the checkout fails
        """
        try:
            subprocess.run(['git', 'checkout', branch_name], check=True, cwd=self.repo_path)
        except subprocess.CalledProcessError:
            raise RuntimeError(f'Failed to checkout branch {branch_name}')

    def view_commit_history(self):
        """
        Views the commit history of the repository.
        :return: A list of commits
        """
        try:
            commits = subprocess.check_output(['git', 'log', '--oneline'], cwd=self.repo_path)
            return commits.decode('utf-8').splitlines()
        except subprocess.CalledProcessError:
            raise RuntimeError('Failed to retrieve commit history')
