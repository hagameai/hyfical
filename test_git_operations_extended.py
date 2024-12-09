import unittest
from git_operations import GitOperations, GitBranchOperations, GitUtilities

class TestGitOperations(unittest.TestCase):
    def setUp(self):
        self.git_ops = GitOperations()

    def test_initialization(self):
        self.assertIsInstance(self.git_ops, GitOperations)

    def test_clone_repository(self):
        result = self.git_ops.clone_repository('https://github.com/example/repo.git')
        self.assertTrue(result)

    def test_branch_creation(self):
        branch_ops = GitBranchOperations()
        result = branch_ops.create_branch('new-feature')
        self.assertTrue(result)

    def test_utilities_function(self):
        utilities = GitUtilities()
        result = utilities.some_utility_function()
        self.assertEqual(result, 'expected_value')

    def test_edge_case_invalid_repo(self):
        with self.assertRaises(ValueError):
            self.git_ops.clone_repository('invalid_url')

if __name__ == '__main__':
    unittest.main()