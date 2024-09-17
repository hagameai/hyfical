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
        :param file_name: Name of the file to be added.
        :return: True if the file was added successfully, False otherwise.
        """
        try:
            file_path = os.path.join(repo_name, file_name)
            with open(file_path, 'w') as f:
                f.write("Sample content.")
            subprocess.check_call(['git', 'add', file_name], cwd=repo_name)
            print(f"File '{file_name}' added successfully.")
            return True
        except Exception as e:
            print(f"Error adding file: {e}")
            return False

    @staticmethod
    def commit_changes(repo_name, commit_message):
        """
        Commits changes to the repository.

        :param repo_name: Name of the repository.
        :param commit_message: Commit message.
        :return: True if the commit was successful, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'commit', '-m', commit_message], cwd=repo_name)
            print("Changes committed successfully.")
            return True
        except Exception as e:
            print(f"Error committing changes: {e}")
            return False

    @staticmethod
    def get_status(repo_name):
        """
        Retrieves the status of the repository.

        :param repo_name: Name of the repository.
        :return: Status string.
        """
        try:
            status = subprocess.check_output(['git', 'status'], cwd=repo_name).decode('utf-8')
            return status
        except Exception as e:
            print(f"Error getting status: {e}")
            return None