import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with the path to the repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Executes a given shell command in the repository path.
        """
        try:
            result = subprocess.run(command, cwd=self.repo_path, check=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr.decode('utf-8')}")
            return None

    def clone(self, repo_url):
        """
        Clones a repository from the given URL.
        """
        return self.run_command(['git', 'clone', repo_url])

    def pull(self):
        """
        Pulls the latest changes from the remote repository.
        """
        return self.run_command(['git', 'pull'])

    def add(self, file_pattern):
        """
        Stages changes for commit based on the file pattern.
        """
        return self.run_command(['git', 'add', file_pattern])

    def commit(self, message):
        """
        Commits the staged changes with a given message.
        """
        return self.run_command(['git', 'commit', '-m', message])

    def push(self):
        """
        Pushes the committed changes to the remote repository.
        """
        return self.run_command(['git', 'push'])
