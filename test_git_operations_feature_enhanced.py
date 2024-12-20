import unittest
from git_operations_feature_enhanced import GitOperationsEnhanced

class TestGitOperationsEnhanced(unittest.TestCase):
    def setUp(self):
        self.git_operations = GitOperationsEnhanced()

    def test_clone_repository(self):
        result = self.git_operations.clone_repository('https://github.com/example/repo.git')
        self.assertTrue(result)

    def test_checkout_branch(self):
        result = self.git_operations.checkout_branch('feature-branch')
        self.assertTrue(result)

    def test_merge_branch(self):
        result = self.git_operations.merge_branch('feature-branch')
        self.assertTrue(result)

    def test_invalid_checkout(self):
        with self.assertRaises(ValueError):
            self.git_operations.checkout_branch('invalid-branch')

    def test_clone_non_existent_repo(self):
        with self.assertRaises(Exception):
            self.git_operations.clone_repository('https://github.com/example/nonexistent.git')

if __name__ == '__main__':
    unittest.main()