import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitOperations with a specific repository path.
        """
        self.repo_path = repo_path

    def clone_repo(self, repo_url):
        """
        Clones a repository from a given URL into the specified path.
        """
        subprocess.run(['git', 'clone', repo_url, self.repo_path], check=True)

    def checkout_branch(self, branch_name):
        """
        Checks out a specific branch in the repository.
        """
        os.chdir(self.repo_path)
        subprocess.run(['git', 'checkout', branch_name], check=True)

    def pull_changes(self):
        """
        Pulls the latest changes from the remote repository.
        """
        os.chdir(self.repo_path)
        subprocess.run(['git', 'pull'], check=True)

    def commit_changes(self, commit_message):
        """
        Commits changes with a specified commit message.
        """
        os.chdir(self.repo_path)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

    def push_changes(self):
        """
        Pushes committed changes to the remote repository.
        """
        os.chdir(self.repo_path)
        subprocess.run(['git', 'push'], check=True)

    def get_current_branch(self):
        """
        Returns the name of the current branch.
        """
        os.chdir(self.repo_path)
        result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True, check=True)
        return result.stdout.strip()