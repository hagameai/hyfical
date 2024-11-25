import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with the specified repository path.
        """
        self.repo_path = repo_path

    def execute_command(self, command):
        """
        Executes a given shell command in the repository path.
        """
        result = subprocess.run(command, cwd=self.repo_path, shell=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

    def clone_repo(self, repo_url):
        """
        Clones a repository from the specified URL.
        """
        command = f'git clone {repo_url}'
        return self.execute_command(command)

    def pull_repo(self):
        """
        Pulls the latest changes from the remote repository.
        """
        command = 'git pull'
        return self.execute_command(command)

    def commit_changes(self, message):
        """
        Commits changes with the specified commit message.
        """
        command = f'git commit -m "{message}"'
        return self.execute_command(command)

    def push_changes(self):
        """
        Pushes changes to the remote repository.
        """
        command = 'git push'
        return self.execute_command(command)