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
        Adds a file to the specified Git repository and commits it.

        :param repo_name: Name of the repository.
        :param file_name: Name of the file to be added.
        :return: True if the file was added and committed successfully, False otherwise.
        """
        try:
            file_path = os.path.join(repo_name, file_name)
            with open(file_path, 'w') as f:
                f.write("Initial content of the file.")
            subprocess.check_call(['git', 'add', file_name], cwd=repo_name)
            subprocess.check_call(['git', 'commit', '-m', 'Add ' + file_name], cwd=repo_name)
            print(f"File '{file_name}' added and committed successfully.")
            return True
        except Exception as e:
            print(f"Error adding file '{file_name}': {e}")
            return False

    @staticmethod
    def list_files(repo_name):
        """
        Lists all files in the specified Git repository.

        :param repo_name: Name of the repository.
        :return: A list of file names in the repository.
        """
        try:
            return os.listdir(repo_name)
        except Exception as e:
            print(f"Error listing files in repository '{repo_name}': {e}")
            return []

    @staticmethod
    def delete_repository(repo_name):
        """
        Deletes the specified Git repository.

        :param repo_name: Name of the repository to be deleted.
        :return: True if the repository was deleted successfully, False otherwise.
        """
        try:
            if os.path.exists(repo_name):
                shutil.rmtree(repo_name)
                print(f"Repository '{repo_name}' deleted successfully.")
                return True
            else:
                print(f"Repository '{repo_name}' does not exist.")
                return False
        except Exception as e:
            print(f"Error deleting repository '{repo_name}': {e}")
            return False