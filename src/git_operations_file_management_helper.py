import os
import shutil

class GitFileManagementHelper:
    """
    A helper class for managing Git files and directories.
    This class provides methods to copy, move, and delete files within a Git repository.
    """

    @staticmethod
    def copy_file(source: str, destination: str) -> None:
        """
        Copy a file from the source to the destination.
        :param source: Path to the source file.
        :param destination: Path to the destination file.
        :raises FileNotFoundError: If the source file does not exist.
        :raises Exception: For any other error during copy.
        """
        if not os.path.isfile(source):
            raise FileNotFoundError(f"Source file '{source}' not found.")
        try:
            shutil.copy2(source, destination)
        except Exception as e:
            raise Exception(f"An error occurred while copying: {e}")

    @staticmethod
    def move_file(source: str, destination: str) -> None:
        """
        Move a file from the source to the destination.
        :param source: Path to the source file.
        :param destination: Path to the destination file.
        :raises FileNotFoundError: If the source file does not exist.
        :raises Exception: For any other error during move.
        """
        if not os.path.isfile(source):
            raise FileNotFoundError(f"Source file '{source}' not found.")
        try:
            shutil.move(source, destination)
        except Exception as e:
            raise Exception(f"An error occurred while moving: {e}")

    @staticmethod
    def delete_file(file_path: str) -> None:
        """
        Delete a file specified by file_path.
        :param file_path: Path to the file to be deleted.
        :raises FileNotFoundError: If the file does not exist.
        :raises Exception: For any other error during deletion.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")
        try:
            os.remove(file_path)
        except Exception as e:
            raise Exception(f"An error occurred while deleting: {e}")