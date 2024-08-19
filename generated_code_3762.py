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

        :param repo_name: Name of the repository.
        :param commit_message: Message for the commit.
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
    def clone_repository(repo_url, target_dir):
        """
        Clones a Git repository from a URL to a target directory.

        :param repo_url: URL of the repository to clone.
        :param target_dir: Directory where the repository will be cloned.
        :return: True if the repository was cloned successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'clone', repo_url, target_dir])
            print(f"Repository cloned to '{target_dir}' successfully.")
            return True
        except Exception as e:
            print(f"Error cloning repository: {e}")
            return False

    @staticmethod
    def fetch_updates(repo_name):
        """
        Fetches updates from the remote repository.

        :param repo_name: Name of the repository.
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
    def pull_updates(repo_name):
        """
        Pulls updates from the remote repository.

        :param repo_name: Name of the repository.
        :return: True if updates were pulled successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'pull'], cwd=repo_name)
            print("Updates pulled successfully.")
            return True
        except Exception as e:
            print(f"Error pulling updates: {e}")
            return False

    @staticmethod
    def push_changes(repo_name):
        """
        Pushes local commits to the remote repository.

        :param repo_name: Name of the repository.
        :return: True if changes were pushed successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'push'], cwd=repo_name)
            print("Changes pushed successfully.")
            return True
        except Exception as e:
            print(f"Error pushing changes: {e}")
            return False