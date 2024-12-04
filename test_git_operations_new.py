import unittest
from git_operations import GitOperations

class TestGitOperations(unittest.TestCase):
    def setUp(self):
        self.git_ops = GitOperations()

    def test_clone_repository(self):
        result = self.git_ops.clone('https://github.com/example/repo.git')
        self.assertTrue(result)

    def test_commit_changes(self):
        self.git_ops.add('file.txt')
        result = self.git_ops.commit('Test commit')
        self.assertTrue(result)

    def test_push_changes(self):
        result = self.git_ops.push('origin', 'main')
        self.assertTrue(result)

    def test_invalid_repository(self):
        with self.assertRaises(ValueError):
            self.git_ops.clone('invalid-url')

    def test_add_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.git_ops.add('nonexistent.txt')

if __name__ == '__main__':
    unittest.main()