import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes GitOperations with a repository path.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path

    def git_command(self, command):
        """
        Executes a Git command in the repository.
        :param command: Git command as a string
        :return: Output of the Git command
        """
        try:
            result = subprocess.check_output(command, cwd=self.repo_path, shell=True, text=True)
            return result.strip()
        except subprocess.CalledProcessError as e:
            return f'Error: {e.output.strip()}'

    def clone(self, repo_url):
        """
        Clones a Git repository from a remote URL.
        :param repo_url: URL of the remote repository
        """
        return self.git_command(f'git clone {repo_url}')

    def pull(self):
        """
        Pulls the latest changes from the remote repository.
        """
        return self.git_command('git pull')

    def commit(self, message):
        """
        Commits changes to the local repository.
        :param message: Commit message
        """
        self.git_command('git add .')  # Stage all changes
        return self.git_command(f'git commit -m "{message}"')

    def push(self):
        """
        Pushes local commits to the remote repository.
        """
        return self.git_command('git push')
