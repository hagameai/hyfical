import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with a repository path.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Runs a shell command in the repository directory.
        :param command: The command to run
        """
        result = subprocess.run(command, cwd=self.repo_path, shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True)
        return result.stdout, result.stderr

    def clone(self, repo_url):
        """
        Clones a Git repository from the specified URL.
        :param repo_url: URL of the repository to clone
        """
        return self.run_command(f'git clone {repo_url}')

    def commit(self, message):
        """
        Commits changes in the repository with the provided message.
        :param message: Commit message
        """
        self.run_command('git add .')
        return self.run_command(f'git commit -m "{message}"')

    def push(self, remote='origin', branch='main'):
        """
        Pushes changes to the specified remote branch.
        :param remote: The remote name (default: 'origin')
        :param branch: The target branch (default: 'main')
        """
        return self.run_command(f'git push {remote} {branch}')

    def pull(self, remote='origin', branch='main'):
        """
        Pulls changes from the specified remote branch.
        :param remote: The remote name (default: 'origin')
        :param branch: The source branch (default: 'main')
        """
        return self.run_command(f'git pull {remote} {branch}')

    def status(self):
        """
        Returns the current status of the repository.
        """
        return self.run_command('git status')

    def log(self):
        """
        Returns the commit log of the repository.
        """
        return self.run_command('git log')