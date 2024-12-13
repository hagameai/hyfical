import os
import shutil

class GitFileManagement:
    """
    A class for managing files in a Git repository.
    This includes operations for copying, moving, and deleting files.
    """

    @staticmethod
    def copy_file(source: str, destination: str) -> None:
        """
        Copy a file from the source to the destination.
        Raises an error if the source file does not exist.
        """
        if not os.path.isfile(source):
            raise FileNotFoundError(f"Source file '{source}' does not exist.")
        shutil.copy2(source, destination)

    @staticmethod
    def move_file(source: str, destination: str) -> None:
        """
        Move a file from the source to the destination.
        Raises an error if the source file does not exist.
        """
        if not os.path.isfile(source):
            raise FileNotFoundError(f"Source file '{source}' does not exist.")
        shutil.move(source, destination)

    @staticmethod
    def delete_file(file_path: str) -> None:
        """
        Delete a file at the specified path.
        Raises an error if the file does not exist.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist.")
        os.remove(file_path)

    @staticmethod
    def list_files(directory: str) -> list:
        """
        List all files in the specified directory.
        Raises an error if the directory does not exist.
        """
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Directory '{directory}' does not exist.")
        return os.listdir(directory)
