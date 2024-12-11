import os
import subprocess

class GitAPI:
    """
    A class to provide an interface for common Git operations.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitAPI with the repository path.
        :param repo_path: Path to the Git repository.
        """
        self.repo_path = repo_path
        if not os.path.exists(os.path.join(repo_path, '.git')):
            raise ValueError(f"{repo_path} is not a valid Git repository.")

    def run_git_command(self, command):
        """
        Executes a Git command in the repository.
        :param command: Git command as a list.
        :return: Output of the command.
        """
        try:
            result = subprocess.run(command, cwd=self.repo_path, text=True,
                                   capture_output=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error executing command: {' '.join(command)}\n{e.stderr}")

    def get_current_branch(self):
        """
        Gets the name of the current branch.
        :return: Current branch name.
        """
        return self.run_git_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()

    def checkout_branch(self, branch_name):
        """
        Checks out to a specified branch.
        :param branch_name: Name of the branch to check out.
        """
        self.run_git_command(['git', 'checkout', branch_name])

    def create_branch(self, branch_name):
        """
        Creates a new branch.
        :param branch_name: Name of the new branch.
        """
        self.run_git_command(['git', 'checkout', '-b', branch_name])
