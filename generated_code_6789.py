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
    def commit_changes(repo_name, message):
        """
        Commits changes in the specified Git repository.

        :param repo_name: Name of the repository.
        :param message: Commit message.
        :return: True if changes were committed successfully, False otherwise.
        """
        try:
            subprocess.check_call(['git', 'commit', '-m', message], cwd=repo_name)
            print(f"Changes committed with message: '{message}'")
            return True
        except Exception as e:
            print(f"Error committing changes: {e}")
            return False

import unittest
import os
import shutil
from git_operations import GitOperations

class TestGitOperations(unittest.TestCase):
    """
    Unit tests for basic Git operations.
    This test suite covers both normal and exceptional scenarios.
    """

    def setUp(self):
        self.repo_name = "test_repo"
        if os.path.exists(self.repo_name):
            shutil.rmtree(self.repo_name)

    def tearDown(self):
        if os.path.exists(self.repo_name):
            shutil.rmtree(self.repo_name)

    def test_initialize_repository(self):
        """ Test repository initialization. """
        response = GitOperations.initialize_repository(self.repo_name)
        self.assertTrue(response, "Repository should be initialized successfully.")
        self.assertTrue(os.path.exists(self.repo_name), "Repository directory should exist.")

    def test_initialize_existing_repository(self):
        """ Test initializing an existing repository. """
        GitOperations.initialize_repository(self.repo_name)
        response = GitOperations.initialize_repository(self.repo_name)
        self.assertFalse(response, "Should not initialize an existing repository.")

    def test_add_file_to_repository(self):
        """ Test adding a file to the Git repository. """
        GitOperations.initialize_repository(self.repo_name)
        response = GitOperations.add_file(self.repo_name, "test_file.txt")
        self.assertTrue(response, "File should be added successfully.")

    def test_commit_changes(self):
        """ Test committing changes in the Git repository. """
        GitOperations.initialize_repository(self.repo_name)
        GitOperations.add_file(self.repo_name, "test_file.txt")
        response = GitOperations.commit_changes(self.repo_name, "Initial commit")
        self.assertTrue(response, "Changes should be committed successfully.")

# README.md content
# hyfical

# This project focuses on basic Git operations to help users understand Git functionalities.