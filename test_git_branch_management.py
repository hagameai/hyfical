import unittest
from git_branch_management import GitBranchManagement

class TestGitBranchManagement(unittest.TestCase):

    def setUp(self):
        self.git_manager = GitBranchManagement()

    def test_create_branch(self):
        result = self.git_manager.create_branch('test-branch')
        self.assertEqual(result, 'Branch test-branch created')

    def test_delete_branch(self):
        self.git_manager.create_branch('test-branch')
        result = self.git_manager.delete_branch('test-branch')
        self.assertEqual(result, 'Branch test-branch deleted')

    def test_switch_branch(self):
        self.git_manager.create_branch('test-branch')
        result = self.git_manager.switch_branch('test-branch')
        self.assertEqual(result, 'Switched to branch test-branch')

    def test_delete_nonexistent_branch(self):
        result = self.git_manager.delete_branch('nonexistent-branch')
        self.assertEqual(result, 'Branch nonexistent-branch does not exist')

if __name__ == '__main__':
    unittest.main()