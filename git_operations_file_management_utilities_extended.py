import os
import subprocess

class GitFileManagementUtilities:
    """
    A class to manage Git file operations with additional utilities.
    """

    @staticmethod
    def list_files_in_repo():
        """
        List all files in the current Git repository.
        """
        try:
            # Retrieve the list of files
            output = subprocess.check_output(['git', 'ls-files'], universal_newlines=True)
            return output.splitlines()
        except subprocess.CalledProcessError as e:
            print(f'Error listing files: {e}')
            return []

    @staticmethod
    def get_file_status(file_path):
        """
        Get the Git status of a specific file.
        :param file_path: The path of the file to check.
        :return: The status of the file.
        """
        try:
            # Get the status of the file
            output = subprocess.check_output(['git', 'status', '--porcelain', file_path], universal_newlines=True)
            return output.strip()
        except subprocess.CalledProcessError as e:
            print(f'Error getting status for {file_path}: {e}')
            return None

    @staticmethod
    def delete_file(file_path):
        """
        Delete a file from the Git repository.
        :param file_path: The path of the file to delete.
        """
        try:
            # Remove the file using git
            subprocess.check_call(['git', 'rm', file_path])
            print(f'File {file_path} deleted successfully.')
        except subprocess.CalledProcessError as e:
            print(f'Error deleting file {file_path}: {e}')

# Example usage:
# utilities = GitFileManagementUtilities()
# print(utilities.list_files_in_repo())