import os
import shutil

class GitFileManagementUtilities:
    """
    A class to provide utility functions for managing files in Git repositories.
    This includes operations like copying, moving, and deleting files.
    """

    @staticmethod
    def copy_file(source: str, destination: str) -> None:
        """
        Copy a file from source to destination.
        :param source: Path to the source file.
        :param destination: Path to the destination file.
        :raises FileNotFoundError: If the source file does not exist.
        :raises IOError: If the file cannot be copied.
        """
        if not os.path.isfile(source):
            raise FileNotFoundError(f"Source file '{source}' does not exist.")
        try:
            shutil.copy2(source, destination)
        except IOError as e:
            raise IOError(f"Failed to copy file: {e}")

    @staticmethod
    def move_file(source: str, destination: str) -> None:
        """
        Move a file from source to destination.
        :param source: Path to the source file.
        :param destination: Path to the destination file.
        :raises FileNotFoundError: If the source file does not exist.
        :raises IOError: If the file cannot be moved.
        """ 
        if not os.path.isfile(source):
            raise FileNotFoundError(f"Source file '{source}' does not exist.")
        try:
            shutil.move(source, destination)
        except IOError as e:
            raise IOError(f"Failed to move file: {e}")

    @staticmethod
    def delete_file(file_path: str) -> None:
        """
        Delete a file at the specified file path.
        :param file_path: Path to the file to be deleted.
        :raises FileNotFoundError: If the file does not exist.
        :raises IOError: If the file cannot be deleted.
        """ 
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist.")
        try:
            os.remove(file_path)
        except IOError as e:
            raise IOError(f"Failed to delete file: {e}")
