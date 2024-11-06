import os
import subprocess

class GitOperations:
    """
    A class to encapsulate basic Git operations.
    """

    @staticmethod
    def clone_repository(repo_url: str, target_dir: str) -> None:
        """
        Clones a git repository into a target directory.

        :param repo_url: URL of the repository to clone.
        :param target_dir: Directory where the repository will be cloned.
        """
        subprocess.run(['git', 'clone', repo_url, target_dir], check=True)

    @staticmethod
    def pull_latest(target_dir: str) -> None:
        """
        Pulls the latest changes from the remote repository into the target directory.

        :param target_dir: Directory of the git repository to pull from.
        """
        os.chdir(target_dir)
        subprocess.run(['git', 'pull'], check=True)

    @staticmethod
    def create_branch(branch_name: str, target_dir: str) -> None:
        """
        Creates a new branch in the specified repository directory.

        :param branch_name: Name of the new branch.
        :param target_dir: Directory of the git repository.
        """
        os.chdir(target_dir)
        subprocess.run(['git', 'checkout', '-b', branch_name], check=True)

    @staticmethod
    def commit_changes(commit_message: str, target_dir: str) -> None:
        """
        Commits changes in the specified repository directory with a message.

        :param commit_message: Commit message for the changes.
        :param target_dir: Directory of the git repository.
        """
        os.chdir(target_dir)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
