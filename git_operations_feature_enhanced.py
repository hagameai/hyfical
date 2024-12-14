import os
import subprocess

class GitOperationsEnhanced:
    """
    A class to enhance Git operations with additional features.
    """

    def __init__(self):
        pass

    def create_branch(self, branch_name):
        """
        Create a new branch in the Git repository.
        :param branch_name: Name of the new branch to create.
        """
        try:
            subprocess.run(['git', 'checkout', '-b', branch_name], check=True)
            print(f'Branch {branch_name} created successfully.')
        except subprocess.CalledProcessError as e:
            print(f'Error creating branch {branch_name}: {e}')

    def delete_branch(self, branch_name):
        """
        Delete an existing branch in the Git repository.
        :param branch_name: Name of the branch to delete.
        """
        try:
            subprocess.run(['git', 'branch', '-d', branch_name], check=True)
            print(f'Branch {branch_name} deleted successfully.')
        except subprocess.CalledProcessError as e:
            print(f'Error deleting branch {branch_name}: {e}')

    def list_branches(self):
        """
        List all branches in the Git repository.
        """
        try:
            branches = subprocess.check_output(['git', 'branch']).decode('utf-8')
            print('Current branches:\n', branches)
        except subprocess.CalledProcessError as e:
            print(f'Error listing branches: {e}')

# Example usage:
# git_ops = GitOperationsEnhanced()
# git_ops.create_branch('feature-x')
# git_ops.delete_branch('feature-x')
# git_ops.list_branches()