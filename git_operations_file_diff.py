import os
import subprocess

class GitFileDiff:
    """
    A class to compute the differences between files in a Git repository.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitFileDiff with the repository path.
        :param repo_path: Path to the Git repository.
        """
        if not os.path.exists(repo_path):
            raise ValueError(f"Repository path '{repo_path}' does not exist.")
        self.repo_path = repo_path

    def get_file_diff(self, file_path):
        """
        Gets the diff of a specified file in the repository.
        :param file_path: Path to the file relative to the repository.
        :return: The diff output as a string.
        """
        command = ['git', 'diff', file_path]
        result = subprocess.run(command, cwd=self.repo_path, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Error getting diff for '{file_path}': {result.stderr.strip()}")
        return result.stdout.strip()

    def get_diff_between_commits(self, commit1, commit2):
        """
        Gets the diff between two commits.
        :param commit1: The first commit hash.
        :param commit2: The second commit hash.
        :return: The diff output as a string.
        """
        command = ['git', 'diff', commit1, commit2]
        result = subprocess.run(command, cwd=self.repo_path, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Error getting diff between commits '{commit1}' and '{commit2}': {result.stderr.strip()}")
        return result.stdout.strip()