import os
import subprocess

class GitUtilities:
    """
    A class providing utility functions for Git operations.
    """

    @staticmethod
    def check_git_installed():
        """
        Check if Git is installed on the system.
        """
        try:
            subprocess.run(['git', '--version'], check=True, stdout=subprocess.PIPE)
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def get_current_branch():
        """
        Get the name of the current Git branch.
        """
        try:
            branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], text=True).strip()
            return branch
        except subprocess.CalledProcessError:
            raise RuntimeError("Failed to get current branch. Ensure you are in a Git repository.")

    @staticmethod
    def list_remote_branches():
        """
        List all remote branches in the Git repository.
        """
        try:
            branches = subprocess.check_output(['git', 'branch', '-r'], text=True).strip().split('\n')
            return [branch.strip() for branch in branches]
        except subprocess.CalledProcessError:
            raise RuntimeError("Failed to list remote branches.")

# Example usage:
if __name__ == '__main__':
    if GitUtilities.check_git_installed():
        print("Git is installed.")
        print(f"Current branch: {GitUtilities.get_current_branch()}")
        print("Remote branches:")
        print(GitUtilities.list_remote_branches())
    else:
        print("Git is not installed.")