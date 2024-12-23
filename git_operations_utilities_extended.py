import os
import subprocess

class GitOperationsUtilitiesExtended:
    """
    A class to provide extended utility functions for Git operations.
    """

    @staticmethod
    def execute_command(command):
        """
        Execute a shell command and return the output.
        :param command: Command to execute as a string.
        :return: Tuple containing (output, error).
        """
        try:
            result = subprocess.run(command, shell=True, check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8'), None
        except subprocess.CalledProcessError as e:
            return None, e.stderr.decode('utf-8')

    @staticmethod
    def check_git_status():
        """
        Check the current status of the Git repository.
        :return: Output of the git status command.
        """
        output, error = GitOperationsUtilitiesExtended.execute_command('git status')
        if error:
            raise Exception(f'Error checking git status: {error}')
        return output

    @staticmethod
    def list_branches():
        """
        List all branches in the Git repository.
        :return: List of branch names.
        """
        output, error = GitOperationsUtilitiesExtended.execute_command('git branch')
        if error:
            raise Exception(f'Error listing branches: {error}')
        return output.splitlines()

    @staticmethod
    def create_branch(branch_name):
        """
        Create a new branch in the Git repository.
        :param branch_name: Name of the branch to create.
        """
        output, error = GitOperationsUtilitiesExtended.execute_command(f'git branch {branch_name}')
        if error:
            raise Exception(f'Error creating branch {branch_name}: {error}')
        return output

    @staticmethod
    def delete_branch(branch_name):
        """
        Delete a branch from the Git repository.
        :param branch_name: Name of the branch to delete.
        """
        output, error = GitOperationsUtilitiesExtended.execute_command(f'git branch -d {branch_name}')
        if error:
            raise Exception(f'Error deleting branch {branch_name}: {error}')
        return output
