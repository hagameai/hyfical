import unittest
from git_branch_management import GitBranchManagement

class TestGitBranchManagement(unittest.TestCase):
    
    def setUp(self):
        self.git_manager = GitBranchManagement()
        self.branch_name = 'test-branch'

    def test_create_branch(self):
        result = self.git_manager.create_branch(self.branch_name)
        self.assertIn(self.branch_name, result)

    def test_delete_branch(self):
        self.git_manager.create_branch(self.branch_name)
        result = self.git_manager.delete_branch(self.branch_name)
        self.assertNotIn(self.branch_name, result)

    def test_switch_branch(self):
        self.git_manager.create_branch(self.branch_name)
        result = self.git_manager.switch_branch(self.branch_name)
        self.assertEqual(result, self.branch_name)

    def test_create_branch_existing(self):
        self.git_manager.create_branch(self.branch_name)
        with self.assertRaises(Exception):
            self.git_manager.create_branch(self.branch_name)

    def test_delete_non_existing_branch(self):
        with self.assertRaises(Exception):
            self.git_manager.delete_branch('non-existing-branch')

if __name__ == '__main__':
    unittest.main()