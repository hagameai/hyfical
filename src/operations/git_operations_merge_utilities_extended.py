import os
import subprocess

class GitMergeUtilities:
    """
    A class to manage and enhance Git merge operations.
    """

    def __init__(self):
        pass

    def merge_branch(self, branch_name: str) -> str:
        """
        Merges the specified branch into the current branch.
        :param branch_name: Name of the branch to merge.
        :return: Success message or error message.
        """
        try:
            result = subprocess.run(['git', 'merge', branch_name], 
                                    check=True, 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f'Error merging branch {branch_name}: {e.stderr.decode('utf-8')}'

    def resolve_conflicts(self) -> str:
        """
        Resolves merge conflicts if any are present.
        :return: Success message or error message.
        """
        try:
            result = subprocess.run(['git', 'mergetool'], 
                                    check=True, 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f'Error resolving conflicts: {e.stderr.decode('utf-8')}'

    def finalize_merge(self) -> str:
        """
        Finalizes the merge by committing the changes.
        :return: Success message or error message.
        """
        try:
            result = subprocess.run(['git', 'commit', '-m', 'Merge commit'], 
                                    check=True, 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f'Error finalizing merge: {e.stderr.decode('utf-8')}'
