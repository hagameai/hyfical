import unittest
from git_operations import GitOperations

class TestGitOperations(unittest.TestCase):
    def setUp(self):
        self.git_ops = GitOperations()

    def test_clone_repository(self):
        # Test cloning a valid repository
        result = self.git_ops.clone('https://github.com/example/repo.git')
        self.assertTrue(result)

    def test_clone_invalid_repository(self):
        # Test cloning an invalid repository
        result = self.git_ops.clone('https://github.com/example/invalid-repo.git')
        self.assertFalse(result)

    def test_commit_changes(self):
        # Test committing changes
        self.git_ops.add('file.txt')
        result = self.git_ops.commit('Test commit')
        self.assertTrue(result)

    def test_commit_no_changes(self):
        # Test committing with no changes
        result = self.git_ops.commit('No changes to commit')
        self.assertFalse(result)

    def test_push_changes(self):
        # Test pushing changes to remote
        result = self.git_ops.push('origin', 'main')
        self.assertTrue(result)

    def test_pull_changes(self):
        # Test pulling changes from remote
        result = self.git_ops.pull('origin', 'main')
        self.assertTrue(result)

    def test_branch_creation(self):
        # Test creating a new branch
        result = self.git_ops.create_branch('new-branch')
        self.assertTrue(result)

    def test_checkout_branch(self):
        # Test checking out to a branch
        result = self.git_ops.checkout('new-branch')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()