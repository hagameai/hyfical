import os
import subprocess

class GitMergeEnhanced:
    """
    A class to enhance Git merge operations with additional features.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitMergeEnhanced class.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def merge_branch(self, source_branch, target_branch):
        """
        Merges the source branch into the target branch.
        :param source_branch: Name of the branch to merge from.
        :param target_branch: Name of the branch to merge into.
        :raises Exception: If the merge fails.
        """
        try:
            # Checkout target branch
            subprocess.check_call(['git', 'checkout', target_branch], cwd=self.repo_path)
            # Merge source branch
            subprocess.check_call(['git', 'merge', source_branch], cwd=self.repo_path)
            print(f'Successfully merged {source_branch} into {target_branch}.')
        except subprocess.CalledProcessError as e:
            raise Exception(f'Merge failed: {e}')

    def abort_merge(self):
        """
        Aborts the current merge operation if in progress.
        """
        try:
            subprocess.check_call(['git', 'merge', '--abort'], cwd=self.repo_path)
            print('Merge aborted successfully.')
        except subprocess.CalledProcessError as e:
            raise Exception(f'Abort failed: {e}')

    def status(self):
        """
        Returns the status of the current repository.
        :return: Status output.
        """
        return subprocess.check_output(['git', 'status'], cwd=self.repo_path).decode('utf-8')

# Example usage:
# git_merge = GitMergeEnhanced('/path/to/repo')
# git_merge.merge_branch('feature-branch', 'main')
