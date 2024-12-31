import subprocess
import os

class GitMergeUtilities:
    """
    A class to handle Git merge operations.
    This class provides methods to facilitate and manage merges in Git.
    """

    def __init__(self, repo_path):
        """
        Initialize with the path to the Git repository.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def merge_branch(self, source_branch, target_branch):
        """
        Merge the source branch into the target branch.
        :param source_branch: The branch to merge from.
        :param target_branch: The branch to merge into.
        :return: Output of the merge command.
        """
        try:
            os.chdir(self.repo_path)
            subprocess.check_call(['git', 'checkout', target_branch])
            output = subprocess.check_output(['git', 'merge', source_branch])
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f"Error during merge: {e.output.decode('utf-8')}")
            raise

    def abort_merge(self):
        """
        Abort the current merge operation.
        """
        try:
            os.chdir(self.repo_path)
            subprocess.check_call(['git', 'merge', '--abort'])
            print("Merge aborted successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error aborting merge: {e.output.decode('utf-8')}")
            raise

    def get_merge_status(self):
        """
        Get the status of the current merge operation.
        :return: Output of the status command.
        """
        try:
            os.chdir(self.repo_path)
            output = subprocess.check_output(['git', 'status'])
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f"Error getting merge status: {e.output.decode('utf-8')}")
            raise
