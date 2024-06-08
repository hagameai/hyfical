```python
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
        with open(os.path.join(self.repo_name, "test_file.txt"), 'w') as f:
            f.write("Test content")
        # Assuming add_file is a method you implement to add files
        response = GitOperations.add_file(self.repo_name, "test_file.txt")
        self.assertTrue(response, "File should be added successfully.")

    def test_commit_changes(self):
        """ Test committing changes in the Git repository. """
        GitOperations.initialize_repository(self.repo_name)
        with open(os.path.join(self.repo_name, "test_file.txt"), 'w') as f:
            f.write("Test content")
        GitOperations.add_file(self.repo_name, "test_file.txt")
        response = GitOperations.commit_changes(self.repo_name, "Initial commit")
        self.assertTrue(response, "Changes should be committed successfully.")

if __name__ == '__main__':
    unittest.main()
```