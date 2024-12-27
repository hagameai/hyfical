import os
import subprocess

class GitCommitManagement:
    """
    A class to manage Git commits, allowing users to
    create, amend, and view commit logs.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitCommitManagement class.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path

    def create_commit(self, message, add_all=False):
        """
        Creates a new Git commit with the specified message.
        :param message: Commit message
        :param add_all: If True, stage all changes before committing
        """
        try:
            if add_all:
                subprocess.check_call(['git', 'add', '.'], cwd=self.repo_path)
            subprocess.check_call(['git', 'commit', '-m', message], cwd=self.repo_path)
            print(f'Commit created: {message}')  
        except subprocess.CalledProcessError as e:
            print(f'Error during commit: {e}')  

    def amend_commit(self, message):
        """
        Amends the last commit with a new message.
        :param message: New commit message
        """
        try:
            subprocess.check_call(['git', 'commit', '--amend', '-m', message], cwd=self.repo_path)
            print(f'Last commit amended: {message}')  
        except subprocess.CalledProcessError as e:
            print(f'Error during amend: {e}')  

    def view_commit_log(self, n=10):
        """
        Displays the last n commits in the log.
        :param n: Number of commits to display
        """
        try:
            log = subprocess.check_output(['git', 'log', '-n', str(n)], cwd=self.repo_path).decode('utf-8')
            print(log)
        except subprocess.CalledProcessError as e:
            print(f'Error retrieving log: {e}')  

# Example usage:
# git_manager = GitCommitManagement('/path/to/repo')
# git_manager.create_commit('Initial commit', add_all=True)
# git_manager.amend_commit('Updated commit message')
# git_manager.view_commit_log(5)