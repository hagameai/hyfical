import unittest
from git_operations import GitOperations

class TestGitOperations(unittest.TestCase):
    def setUp(self):
        self.git_ops = GitOperations()

    def test_clone_repository(self):
        # Test cloning a valid repository
        result = self.git_ops.clone('https://github.com/example/repo.git', 'test_repo')
        self.assertTrue(os.path.exists('test_repo'))

    def test_clone_invalid_repository(self):
        # Test cloning an invalid repository
        with self.assertRaises(subprocess.CalledProcessError):
            self.git_ops.clone('https://github.com/example/invalid_repo.git', 'test_invalid_repo')

    def test_commit_changes(self):
        # Test committing changes
        os.makedirs('test_commit_repo', exist_ok=True)
        with open('test_commit_repo/test.txt', 'w') as f:
            f.write('Test')
        self.git_ops.add('test_commit_repo/test.txt')
        self.git_ops.commit('Initial commit')
        self.assertIn('Initial commit', self.git_ops.log())

    def test_commit_no_changes(self):
        # Test committing with no changes
        with self.assertRaises(ValueError):
            self.git_ops.commit('No changes here')

    def tearDown(self):
        # Cleanup created directories
        subprocess.run(['rm', '-rf', 'test_repo', 'test_commit_repo', 'test_invalid_repo'], check=False)

if __name__ == '__main__':
    unittest.main()