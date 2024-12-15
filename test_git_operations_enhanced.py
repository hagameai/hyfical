import unittest
from git_operations_feature_enhanced import GitOperationsEnhanced
from git_branch_management import GitBranchManagement

class TestGitOperationsEnhanced(unittest.TestCase):
    def setUp(self):
        self.git_ops = GitOperationsEnhanced()
        self.branch_mgmt = GitBranchManagement()

    def test_clone_repository(self):
        result = self.git_ops.clone_repository('https://github.com/user/repo.git', './repo')
        self.assertTrue(result)

    def test_create_branch(self):
        result = self.branch_mgmt.create_branch('new-feature')
        self.assertTrue(result)

    def test_delete_branch(self):
        self.branch_mgmt.create_branch('branch-to-delete')
        result = self.branch_mgmt.delete_branch('branch-to-delete')
        self.assertTrue(result)

    def test_checkout_branch(self):
        self.branch_mgmt.create_branch('feature-branch')
        result = self.branch_mgmt.checkout_branch('feature-branch')
        self.assertTrue(result)

    def test_invalid_branch_deletion(self):
        result = self.branch_mgmt.delete_branch('non-existent-branch')
        self.assertFalse(result)

    def tearDown(self):
        self.git_ops.clean_up()
        self.branch_mgmt.clean_up()

if __name__ == '__main__':
    unittest.main()