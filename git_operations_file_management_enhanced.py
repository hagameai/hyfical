import os
import subprocess

class GitFileManagementEnhanced:
    """
    A class to manage files in a Git repository. This includes operations to add, remove, and list files.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitFileManagementEnhanced class.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def add_file(self, file_path):
        """
        Adds a file to the staging area.
        :param file_path: Path of the file to add.
        """
        try:
            subprocess.run(['git', 'add', file_path], cwd=self.repo_path, check=True)
            print(f'File {file_path} added successfully.')
        except subprocess.CalledProcessError:
            print(f'Error adding file {file_path}.')

    def remove_file(self, file_path):
        """
        Removes a file from the repository.
        :param file_path: Path of the file to remove.
        """
        try:
            subprocess.run(['git', 'rm', file_path], cwd=self.repo_path, check=True)
            print(f'File {file_path} removed successfully.')
        except subprocess.CalledProcessError:
            print(f'Error removing file {file_path}.')

    def list_files(self):
        """
        Lists all files in the repository.
        """
        try:
            files = subprocess.check_output(['git', 'ls-files'], cwd=self.repo_path).decode().splitlines()
            return files
        except subprocess.CalledProcessError:
            print('Error listing files.')
            return []
