import os
import subprocess

class GitOperationsHelper:
    """
    A helper class for advanced Git operations.
    This class contains methods to perform complex Git tasks,
    focusing on error handling and user feedback.
    """

    @staticmethod
    def execute_git_command(command):
        """
        Executes a Git command and returns the output.
        Args:
            command (list): A list of command arguments.
        Returns:
            str: Output from the command execution.
        Raises:
            subprocess.CalledProcessError: If the command fails.
        """
        try:
            result = subprocess.run(command, check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {' '.join(command)}\n{e.stderr}")
            raise

    @staticmethod
    def get_current_branch():
        """
        Retrieves the current Git branch name.
        Returns:
            str: The name of the current branch.
        """
        return GitOperationsHelper.execute_git_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])

    @staticmethod
    def stash_changes():
        """
        Stashes any uncommitted changes in the working directory.
        """
        GitOperationsHelper.execute_git_command(['git', 'stash'])

    @staticmethod
    def checkout_branch(branch_name):
        """
        Checks out the specified Git branch.
        Args:
            branch_name (str): The name of the branch to checkout.
        """
        GitOperationsHelper.execute_git_command(['git', 'checkout', branch_name])
