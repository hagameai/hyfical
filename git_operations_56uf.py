import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initialize the GitOperations with the repository path.
        """
        self.repo_path = repo_path
        self._validate_repo()

    def _validate_repo(self):
        """
        Validate if the given path is a Git repository.
        """
        if not os.path.isdir(os.path.join(self.repo_path, '.git')):
            raise ValueError(f"{self.repo_path} is not a valid Git repository.")

    def commit(self, message):
        """
        Commit changes with the provided message.
        """
        self._run_git_command(['git', 'add', '.'])
        self._run_git_command(['git', 'commit', '-m', message])

    def push(self):
        """
        Push changes to the remote repository.
        """
        self._run_git_command(['git', 'push'])

    def pull(self):
        """
        Pull changes from the remote repository.
        """
        self._run_git_command(['git', 'pull'])

    def _run_git_command(self, command):
        """
        Run a git command in the repository directory.
        """
        result = subprocess.run(command, cwd=self.repo_path, text=True, capture_output=True)
        if result.returncode != 0:
            raise RuntimeError(f"Error executing command {' '.join(command)}: {result.stderr}")
        return result.stdout
