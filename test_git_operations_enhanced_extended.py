import unittest
from git_operations_feature_enhanced import GitOperationsEnhanced
from git_branch_management import GitBranchManagement
from git_operations_additional import GitBranchOperations

class TestGitOperationsEnhanced(unittest.TestCase):

    def setUp(self):
        self.git_ops = GitOperationsEnhanced()
        self.branch_mgmt = GitBranchManagement()
        self.branch_ops = GitBranchOperations()

    def test_create_branch(self):
        branch_name = 'test_branch'
        self.branch_mgmt.create_branch(branch_name)
        self.assertTrue(self.branch_mgmt.branch_exists(branch_name))

    def test_delete_branch(self):
        branch_name = 'test_branch'
        self.branch_mgmt.create_branch(branch_name)
        self.branch_mgmt.delete_branch(branch_name)
        self.assertFalse(self.branch_mgmt.branch_exists(branch_name))

    def test_switch_branch(self):
        branch_name = 'test_branch'
        self.branch_mgmt.create_branch(branch_name)
        self.branch_mgmt.switch_branch(branch_name)
        self.assertEqual(self.branch_mgmt.current_branch(), branch_name)

    def test_handle_invalid_branch(self):
        with self.assertRaises(Exception):
            self.branch_mgmt.switch_branch('non_existent_branch')

    def test_git_operation_enhanced(self):
        result = self.git_ops.run_command('git status')
        self.assertIn('On branch', result)

if __name__ == '__main__':
    unittest.main()