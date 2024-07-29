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

        :param repo_name: Name of the repository where the file will be added.
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
            print(f"Error adding file: {e}")
            return False

    @staticmethod
    def commit_changes(repo_name, message):
        """
        Commits changes in the specified Git repository.

        :param repo_name: Name of the repository where changes are committed.
        :param message: Commit message.
        :return: True if the commit was successful, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'commit', '-m', message], cwd=repo_name)
            print("Changes committed successfully.")
            return True
        except Exception as e:
            print(f"Error committing changes: {e}")
            return False

    @staticmethod
    def push_changes(repo_name, remote='origin', branch='master'):
        """
        Pushes committed changes to a remote repository.

        :param repo_name: Name of the repository where changes are pushed.
        :param remote: Name of the remote repository.
        :param branch: Branch to push changes to.
        :return: True if the push was successful, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'push', remote, branch], cwd=repo_name)
            print("Changes pushed successfully.")
            return True
        except Exception as e:
            print(f"Error pushing changes: {e}")
            return False