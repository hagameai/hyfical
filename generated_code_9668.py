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
    def add_file(repo_name, file_name, content):
        """
        Adds a file to the specified Git repository.

        :param repo_name: Name of the repository.
        :param file_name: Name of the file to be added.
        :param content: Content to write to the file.
        :return: True if the file was added successfully, False otherwise.
        """
        try:
            file_path = os.path.join(repo_name, file_name)
            with open(file_path, 'w') as file:
                file.write(content)
            subprocess.check_call(['git', 'add', file_name], cwd=repo_name)
            print(f"File '{file_name}' added successfully.")
            return True
        except Exception as e:
            print(f"Error adding file '{file_name}': {e}")
            return False

    @staticmethod
    def commit_changes(repo_name, message):
        """
        Commits changes in the Git repository.

        :param repo_name: Name of the repository.
        :param message: Commit message.
        :return: True if changes were committed successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'commit', '-m', message], cwd=repo_name)
            print(f"Changes committed with message: {message}")
            return True
        except Exception as e:
            print(f"Error committing changes: {e}")
            return False

    @staticmethod
    def push_changes(repo_name, remote='origin', branch='main'):
        """
        Pushes committed changes to the remote repository.

        :param repo_name: Name of the repository.
        :param remote: Name of the remote repository.
        :param branch: Name of the branch to push to.
        :return: True if changes were pushed successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'push', remote, branch], cwd=repo_name)
            print(f"Changes pushed to {remote}/{branch}.")
            return True
        except Exception as e:
            print(f"Error pushing changes: {e}")
            return False