import os
import subprocess

class GitBranchFeatures:
    """
    A class to provide additional features for Git branch management.
    This includes merging branches, deleting branches, and listing all branches.
    """

    def __init__(self, repo_path):
        """
        Initializes the GitBranchFeatures with the path to the Git repository.
        :param repo_path: Path to the Git repository
        """
        self.repo_path = repo_path

    def run_command(self, command):
        """
        Runs a shell command and returns the output.
        :param command: Command to run
        :return: Output of the command
        """
        try:
            result = subprocess.run(command, cwd=self.repo_path, text=True, capture_output=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error running command '{command}': {e.stderr.strip()}")
            return None

    def list_branches(self):
        """
        Lists all branches in the repository.
        :return: List of branch names
        """
        command = ['git', 'branch']
        output = self.run_command(command)
        return output.split('\n') if output else []

    def merge_branch(self, branch_name):
        """
        Merges the specified branch into the current branch.
        :param branch_name: Name of the branch to merge
        :return: Success message or error
        """
        command = ['git', 'merge', branch_name]
        return self.run_command(command) or f"Failed to merge branch '{branch_name}'"

    def delete_branch(self, branch_name):
        """
        Deletes the specified branch.
        :param branch_name: Name of the branch to delete
        :return: Success message or error
        """
        command = ['git', 'branch', '-d', branch_name]
        return self.run_command(command) or f"Failed to delete branch '{branch_name}'"

# Example usage:
# git_features = GitBranchFeatures('/path/to/repo')
# print(git_features.list_branches())
# print(git_features.merge_branch('feature-branch'))
# print(git_features.delete_branch('old-branch'))
