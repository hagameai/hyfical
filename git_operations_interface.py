import os
import subprocess

class GitOperationsInterface:
    """
    A class to provide a simplified interface to perform common Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperationsInterface with the repository path.
        
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def execute_command(self, command):
        """
        Executes a Git command in the specified repository path.
        
        :param command: The Git command to execute.
        :return: Output of the command.
        """
        try:
            result = subprocess.run(command, cwd=self.repo_path, text=True,
                                   shell=True, capture_output=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error executing command '{command}': {e}")
            return None

    def list_branches(self):
        """
        Lists all branches in the repository.
        
        :return: List of branch names.
        """
        command = 'git branch'
        output = self.execute_command(command)
        return output.splitlines() if output else []

    def create_branch(self, branch_name):
        """
        Creates a new branch in the repository.
        
        :param branch_name: Name of the new branch.
        :return: Success status.
        """
        command = f'git branch {branch_name}'
        return self.execute_command(command) is not None

    def delete_branch(self, branch_name):
        """
        Deletes a branch in the repository.
        
        :param branch_name: Name of the branch to delete.
        :return: Success status.
        """
        command = f'git branch -d {branch_name}'
        return self.execute_command(command) is not None

    def checkout_branch(self, branch_name):
        """
        Checks out a specified branch in the repository.
        
        :param branch_name: Name of the branch to check out.
        :return: Success status.
        """
        command = f'git checkout {branch_name}'
        return self.execute_command(command) is not None

# Example usage:
# git_ops = GitOperationsInterface('/path/to/repo')
# git_ops.create_branch('new-feature')
# branches = git_ops.list_branches()