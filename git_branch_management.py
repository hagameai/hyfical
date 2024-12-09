import os
import subprocess

class GitBranchManagement:
    """
    A class to manage Git branches and perform operations on them.
    """

    def __init__(self):
        pass

    def create_branch(self, branch_name):
        """
        Creates a new Git branch with the specified name.
        
        Args:
            branch_name (str): The name of the new branch.
        """
        try:
            subprocess.run(['git', 'checkout', '-b', branch_name], check=True)
            print(f"Branch '{branch_name}' created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating branch '{branch_name}': {e}")

    def delete_branch(self, branch_name):
        """
        Deletes the specified Git branch if it exists.
        
        Args:
            branch_name (str): The name of the branch to delete.
        """
        try:
            subprocess.run(['git', 'branch', '-d', branch_name], check=True)
            print(f"Branch '{branch_name}' deleted successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error deleting branch '{branch_name}': {e}")

    def list_branches(self):
        """
        Lists all Git branches in the current repository.
        """
        try:
            branches = subprocess.check_output(['git', 'branch'], text=True)
            print("Available branches:\n" + branches)
        except subprocess.CalledProcessError as e:
            print(f"Error listing branches: {e}")

if __name__ == '__main__':
    g_branch_mgmt = GitBranchManagement()
    g_branch_mgmt.list_branches()  
    # Example usage:
    # g_branch_mgmt.create_branch('new-feature')
    # g_branch_mgmt.delete_branch('old-feature')
