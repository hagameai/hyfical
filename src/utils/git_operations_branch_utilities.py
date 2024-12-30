import os
import subprocess

class GitBranchUtilities:
    """
    A class that provides various utilities for managing Git branches.
    """

    @staticmethod
    def create_branch(branch_name):
        """
        Create a new branch with the specified name.
        Raises an exception if the branch already exists or if the creation fails.
        """
        try:
            result = subprocess.run(['git', 'branch', branch_name],
                                    check=True,
                                    capture_output=True,
                                    text=True)
            print(f'Branch created: {branch_name}')  # Log branch creation
        except subprocess.CalledProcessError as e:
            print(f'Error creating branch: {e.stderr}')  # Log the error
            raise Exception(f'Failed to create branch: {branch_name}')

    @staticmethod
    def delete_branch(branch_name):
        """
        Delete the specified branch if it exists.
        Raises an exception if the deletion fails.
        """
        try:
            result = subprocess.run(['git', 'branch', '-d', branch_name],
                                    check=True,
                                    capture_output=True,
                                    text=True)
            print(f'Branch deleted: {branch_name}')  # Log branch deletion
        except subprocess.CalledProcessError as e:
            print(f'Error deleting branch: {e.stderr}')  # Log the error
            raise Exception(f'Failed to delete branch: {branch_name}')

    @staticmethod
    def list_branches():
        """
        Return a list of all branches in the repository.
        """
        try:
            result = subprocess.run(['git', 'branch'],
                                    check=True,
                                    capture_output=True,
                                    text=True)
            branches = result.stdout.strip().split('\n')
            return [branch.strip() for branch in branches]
        except subprocess.CalledProcessError as e:
            print(f'Error listing branches: {e.stderr}')  # Log the error
            raise Exception('Failed to list branches')
