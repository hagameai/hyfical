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

        :param repo_name: Name of the repository.
        :param file_name: Name of the file to add.
        :return: True if the file was added successfully, False otherwise.
        """
        try:
            file_path = os.path.join(repo_name, file_name)
            with open(file_path, 'w') as f:
                f.write("Sample content for the file.")
            subprocess.check_call(['git', 'add', file_name], cwd=repo_name)
            print(f"File '{file_name}' added to repository '{repo_name}'.")
            return True
        except Exception as e:
            print(f"Error adding file '{file_name}': {e}")
            return False

    @staticmethod
    def commit_changes(repo_name, commit_message):
        """
        Commits changes in the specified Git repository.

        :param repo_name: Name of the repository.
        :param commit_message: Commit message for the changes.
        :return: True if the commit was successful, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'commit', '-m', commit_message], cwd=repo_name)
            print(f"Changes committed with message: '{commit_message}'")
            return True
        except Exception as e:
            print(f"Error committing changes: {e}")
            return False

    @staticmethod
    def clone_repository(repo_url, target_directory):
        """
        Clones a Git repository from the given URL to the specified directory.

        :param repo_url: URL of the repository to clone.
        :param target_directory: Directory to clone the repository into.
        :return: True if the repository was cloned successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'clone', repo_url, target_directory])
            print(f"Repository cloned from '{repo_url}' to '{target_directory}'.")
            return True
        except Exception as e:
            print(f"Error cloning repository: {e}")
            return False

    @staticmethod
    def list_files(repo_name):
        """
        Lists all files in the specified Git repository.

        :param repo_name: Name of the repository.
        :return: List of file names in the repository.
        """
        try:
            return os.listdir(repo_name)
        except Exception as e:
            print(f"Error listing files in repository: {e}")
            return []