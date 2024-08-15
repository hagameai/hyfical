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

        :param repo_name: Name of the repository where the file will be added.
        :param file_name: Name of the file to be added.
        :return: True if the file was added successfully, False otherwise.
        """
        try:
            file_path = os.path.join(repo_name, file_name)
            with open(file_path, 'w') as f:
                f.write("Sample content")
            subprocess.check_call(['git', 'add', file_name], cwd=repo_name)
            print(f"File '{file_name}' added successfully.")
            return True
        except Exception as e:
            print(f"Error adding file: {e}")
            return False

    @staticmethod
    def commit_changes(repo_name, commit_message):
        """
        Commits changes in the specified Git repository.

        :param repo_name: Name of the repository where changes will be committed.
        :param commit_message: Commit message for the changes.
        :return: True if changes were committed successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'commit', '-m', commit_message], cwd=repo_name)
            print("Changes committed successfully.")
            return True
        except Exception as e:
            print(f"Error committing changes: {e}")
            return False

    @staticmethod
    def clone_repository(repo_url, destination):
        """
        Clones a Git repository from a remote URL.

        :param repo_url: URL of the Git repository to clone.
        :param destination: Local directory where the repository will be cloned.
        :return: True if the repository was cloned successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'clone', repo_url, destination])
            print(f"Repository cloned successfully to '{destination}'.")
            return True
        except Exception as e:
            print(f"Error cloning repository: {e}")
            return False

    @staticmethod
    def fetch_updates(repo_name):
        """
        Fetches updates from the remote repository.

        :param repo_name: Name of the repository to fetch updates from.
        :return: True if updates were fetched successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'fetch'], cwd=repo_name)
            print("Updates fetched successfully.")
            return True
        except Exception as e:
            print(f"Error fetching updates: {e}")
            return False

    @staticmethod
    def push_changes(repo_name):
        """
        Pushes local changes to the remote repository.

        :param repo_name: Name of the repository where changes will be pushed.
        :return: True if changes were pushed successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'push'], cwd=repo_name)
            print("Changes pushed successfully.")
            return True
        except Exception as e:
            print(f"Error pushing changes: {e}")
            return False

    @staticmethod
    def pull_changes(repo_name):
        """
        Pulls changes from the remote repository to local.

        :param repo_name: Name of the repository to pull updates into.
        :return: True if changes were pulled successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'pull'], cwd=repo_name)
            print("Changes pulled successfully.")
            return True
        except Exception as e:
            print(f"Error pulling changes: {e}")
            return False