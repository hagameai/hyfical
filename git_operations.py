import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with a repository path.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Executes a shell command in the repository path.
        :param command: Command to be executed.
        :return: Output of the command.
        """
        try:
            result = subprocess.run(command, cwd=self.repo_path, text=True,
                                    shell=True, check=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f'Error: {e.stderr}')
            return None

    def clone(self, repo_url):
        """
        Clones a Git repository.
        :param repo_url: URL of the repository to clone.
        """
        command = f'git clone {repo_url}'
        return self.run_command(command)

    def pull(self):
        """
        Pulls the latest changes from the remote repository.
        """
        command = 'git pull'
        return self.run_command(command)

    def status(self):
        """
        Returns the status of the repository.
        """
        command = 'git status'
        return self.run_command(command)

    def add(self, file_name):
        """
        Stages a file for commit.
        :param file_name: Name of the file to add.
        """
        command = f'git add {file_name}'
        return self.run_command(command)

    def commit(self, message):
        """
        Commits staged changes with a message.
        :param message: Commit message.
        """
        command = f'git commit -m "{message}"'
        return self.run_command(command)

    def push(self):
        """
        Pushes committed changes to the remote repository.
        """
        command = 'git push'
        return self.run_command(command)

