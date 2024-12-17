import os
import subprocess

class GitMergeOperations:
    """
    A class to manage Git merge operations.
    Provides functionalities to perform merges and handle merge conflicts.
    """

    def __init__(self, repo_path):
        """
        Initialize the GitMergeOperations with the repository path.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def merge_branch(self, target_branch, source_branch):
        """
        Merges the source branch into the target branch.
        :param target_branch: The branch to merge into.
        :param source_branch: The branch to merge from.
        """
        try:
            subprocess.check_call(['git', 'checkout', target_branch], cwd=self.repo_path)
            subprocess.check_call(['git', 'merge', source_branch], cwd=self.repo_path)
            print(f'Successfully merged {source_branch} into {target_branch}.')
        except subprocess.CalledProcessError as e:
            print(f'Error during merging: {e}')
            raise

    def handle_merge_conflicts(self):
        """
        This method handles merge conflicts by aborting the merge.
        """
        try:
            subprocess.check_call(['git', 'merge', '--abort'], cwd=self.repo_path)
            print('Merge conflicts detected. Merge aborted.')
        except subprocess.CalledProcessError as e:
            print(f'Error during aborting merge: {e}')
            raise

# Example usage:
# if __name__ == '__main__':
#     merge_operations = GitMergeOperations('/path/to/repo')
#     merge_operations.merge_branch('main', 'feature-branch')
#     merge_operations.handle_merge_conflicts()