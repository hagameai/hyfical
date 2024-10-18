import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    @staticmethod
    def initialize_repository(repo_name):
        """
        Initializes a new Git repository in the specified directory.

        :param repo_name: Name of the repository to be created.
        :return: True if the repository was initialized successfully, False otherwise.
        """
        try:
            if os.path.exists(repo_name):
                print(f"Repository '{repo_name}' already exists.")
                return False
            os.makedirs(repo_name)
            subprocess.check_call(['git', 'init'], cwd=repo_name)
            print(f"Repository '{repo_name}' initialized successfully.")
            return True
        except Exception as e:
            print(f"Error initializing repository: {e}")
            return False

    @staticmethod
    def add_file(repo_name, file_name):
        """
        Adds a file to the specified Git repository.

        :param repo_name: The path to the repository.
        :param file_name: The name of the file to add.
        :return: True if the file was added successfully, False otherwise.
        """
        try:
            file_path = os.path.join(repo_name, file_name)
            with open(file_path, 'w') as f:
                f.write('# New file created\n')
            subprocess.check_call(['git', 'add', file_name], cwd=repo_name)
            print(f"File '{file_name}' added successfully to '{repo_name}'.")
            return True
        except Exception as e:
            print(f"Error adding file: {e}")
            return False

    @staticmethod
    def commit_changes(repo_name, message):
        """
        Commits changes in the specified Git repository.

        :param repo_name: The path to the repository.
        :param message: The commit message.
        :return: True if the commit was successful, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'commit', '-m', message], cwd=repo_name)
            print(f"Changes committed successfully with message: '{message}'.")
            return True
        except Exception as e:
            print(f"Error committing changes: {e}")
            return False

    @staticmethod
    def clone_repository(repo_url, clone_dir):
        """
        Clones a remote Git repository to the specified directory.

        :param repo_url: The URL of the repository to clone.
        :param clone_dir: The directory to clone the repository into.
        :return: True if the repository was cloned successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'clone', repo_url, clone_dir])
            print(f"Repository cloned successfully from '{repo_url}' to '{clone_dir}'.")
            return True
        except Exception as e:
            print(f"Error cloning repository: {e}")
            return False