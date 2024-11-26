import unittest
from git_operations import GitOperations

class TestGitOperations(unittest.TestCase):

    def setUp(self):
        self.git_ops = GitOperations()

    def test_clone_repository(self):
        # Test normal case: cloning a repository
        result = self.git_ops.clone('https://github.com/example/repo.git')
        self.assertTrue(result)

    def test_clone_invalid_repository(self):
        # Test edge case: cloning a non-existent repository
        with self.assertRaises(Exception):
            self.git_ops.clone('https://github.com/example/nonexistent.git')

    def test_commit_changes(self):
        # Test normal case: committing changes
        self.git_ops.add('file.txt')
        result = self.git_ops.commit('Added file.txt')
        self.assertTrue(result)

    def test_commit_no_changes(self):
        # Test edge case: committing with no changes
        with self.assertRaises(Exception):
            self.git_ops.commit('No changes to commit')

    def test_push_changes(self):
        # Test normal case: pushing changes
        result = self.git_ops.push()
        self.assertTrue(result)

    def test_push_without_commit(self):
        # Test edge case: pushing without a commit
        with self.assertRaises(Exception):
            self.git_ops.push()

if __name__ == '__main__':
    unittest.main()