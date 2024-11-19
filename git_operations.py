import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with the specified repository path.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Runs a shell command in the repository path.
        :param command: Command to run.
        :return: Output of the command.
        """
        result = subprocess.run(command, shell=True, cwd=self.repo_path,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        return result.stdout.strip() if result.returncode == 0 else result.stderr.strip()

    def clone_repo(self, repo_url):
        """
        Clones a Git repository from the specified URL.
        :param repo_url: URL of the repository to clone.
        """
        return self.run_command(f'git clone {repo_url}')

    def pull_repo(self):
        """
        Pulls the latest changes from the remote repository.
        """
        return self.run_command('git pull')

    def commit_changes(self, message):
        """
        Commits changes to the local repository.
        :param message: Commit message.
        """
        self.run_command('git add .')
        return self.run_command(f'git commit -m "{message}"')

    def push_changes(self):
        """
        Pushes committed changes to the remote repository.
        """
        return self.run_command('git push')

    def status(self):
        """
        Returns the current status of the Git repository.
        """
        return self.run_command('git status')

    def log(self):
        """
        Returns the commit log of the repository.
        """
        return self.run_command('git log')
