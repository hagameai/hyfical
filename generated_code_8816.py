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
            with open(file_path, 'w') as file:
                file.write("Sample content.")
            subprocess.check_call(['git', 'add', file_name], cwd=repo_name)
            print(f"File '{file_name}' added to repository '{repo_name}'.")
            return True
        except Exception as e:
            print(f"Error adding file: {e}")
            return False

    @staticmethod
    def commit_changes(repo_name, commit_message):
        """
        Commits changes to the Git repository with a message.

        :param repo_name: Name of the repository.
        :param commit_message: Commit message.
        :return: True if changes were committed successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'commit', '-m', commit_message], cwd=repo_name)
            print(f"Changes committed with message: '{commit_message}'.")
            return True
        except Exception as e:
            print(f"Error committing changes: {e}")
            return False

    @staticmethod
    def list_commits(repo_name):
        """
        Lists the commits in the Git repository.

        :param repo_name: Name of the repository.
        :return: List of commit messages.
        """
        try:
            commits = subprocess.check_output(['git', 'log', '--oneline'], cwd=repo_name)
            return commits.decode('utf-8').strip().split('\n')
        except Exception as e:
            print(f"Error listing commits: {e}")
            return []

    @staticmethod
    def clone_repository(repo_url, clone_dir):
        """
        Clones a Git repository from a remote URL.

        :param repo_url: URL of the repository to clone.
        :param clone_dir: Directory where the repository will be cloned.
        :return: True if the repository was cloned successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'clone', repo_url, clone_dir])
            print(f"Repository cloned from '{repo_url}' to '{clone_dir}'.")
            return True
        except Exception as e:
            print(f"Error cloning repository: {e}")
            return False