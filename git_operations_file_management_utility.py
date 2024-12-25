import os
import shutil

class GitFileManagementUtility:
    """
    A class that provides utility functions for managing files in a Git environment.
    This includes operations for copying, moving, and deleting files safely.
    """

    @staticmethod
    def copy_file(src, dest):
        """
        Copies a file from src to dest.
        Raises an error if the source file does not exist.
        """
        if not os.path.isfile(src):
            raise FileNotFoundError(f"Source file '{src}' does not exist.")
        shutil.copy(src, dest)

    @staticmethod
    def move_file(src, dest):
        """
        Moves a file from src to dest.
        Raises an error if the source file does not exist.
        """
        if not os.path.isfile(src):
            raise FileNotFoundError(f"Source file '{src}' does not exist.")
        shutil.move(src, dest)

    @staticmethod
    def delete_file(filepath):
        """
        Deletes the specified file.
        Raises an error if the file does not exist.
        """
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File '{filepath}' does not exist.")
        os.remove(filepath)

    @staticmethod
    def list_files(directory):
        """
        Returns a list of files in the specified directory.
        Raises an error if the directory does not exist.
        """
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Directory '{directory}' does not exist.")
        return os.listdir(directory)
