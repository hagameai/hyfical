import os
import subprocess

class GitBranchUtilities:
    """
    A class to manage advanced operations on Git branches.
    This includes functionalities like renaming branches, deleting branches,
    and fetching information about current branches.
    """

    def __init__(self):
        pass

    def rename_branch(self, old_name: str, new_name: str) -> str:
        """
        Renames a given branch from old_name to new_name.
        
        Args:
            old_name (str): The current name of the branch.
            new_name (str): The new name for the branch.

        Returns:
            str: A message indicating the result of the operation.
        """
        try:
            subprocess.run(['git', 'branch', '-m', old_name, new_name], check=True)
            return f'Branch renamed from {old_name} to {new_name}'
        except subprocess.CalledProcessError as e:
            return f'Error renaming branch: {e}'

    def delete_branch(self, branch_name: str) -> str:
        """
        Deletes a given branch. Make sure to switch to another branch first.
        
        Args:
            branch_name (str): The name of the branch to delete.

        Returns:
            str: A message indicating the result of the operation.
        """
        try:
            subprocess.run(['git', 'branch', '-d', branch_name], check=True)
            return f'Branch {branch_name} deleted successfully'
        except subprocess.CalledProcessError as e:
            return f'Error deleting branch: {e}'

    def list_branches(self) -> str:
        """
        Lists all branches in the current repository.
        
        Returns:
            str: A list of branch names.
        """
        try:
            result = subprocess.run(['git', 'branch'], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f'Error fetching branches: {e}'

# Example usage:
if __name__ == '__main__':
    git_util = GitBranchUtilities()
    print(git_util.list_branches())
    print(git_util.rename_branch('old_branch', 'new_branch'))
    print(git_util.delete_branch('new_branch'))