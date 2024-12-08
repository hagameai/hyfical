import os
import subprocess

class GitBranchOperations:
    """
    A class to manage Git branches.
    """

    @staticmethod
    def create_branch(branch_name):
        """
        Create a new branch in the current repository.
        :param branch_name: Name of the new branch
        """
        try:
            subprocess.check_call(['git', 'checkout', '-b', branch_name])
            print(f'Branch {branch_name} created successfully.')
        except subprocess.CalledProcessError as e:
            print(f'Error creating branch {branch_name}: {e}')

    @staticmethod
    def delete_branch(branch_name):
        """
        Delete a branch from the current repository.
        :param branch_name: Name of the branch to delete
        """
        try:
            subprocess.check_call(['git', 'branch', '-d', branch_name])
            print(f'Branch {branch_name} deleted successfully.')
        except subprocess.CalledProcessError as e:
            print(f'Error deleting branch {branch_name}: {e}')

    @staticmethod
    def list_branches():
        """
        List all branches in the current repository.
        """
        try:
            branches = subprocess.check_output(['git', 'branch']).decode('utf-8')
            print('Branches:
' + branches)
        except subprocess.CalledProcessError as e:
            print(f'Error listing branches: {e}')
