import logging

class GitOperationsLogging:
    """
    A class to manage logging for Git operations.
    This class provides methods to set up logging and log various Git operations.
    """

    def __init__(self, log_file='git_operations.log'):
        """
        Initializes the logging configuration.

        :param log_file: The file where logs will be stored.
        """
        logging.basicConfig(filename=log_file,
                            level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_git_operation(self, operation, status):
        """
        Logs the result of a Git operation.

        :param operation: The Git operation performed (e.g., 'commit', 'push').
        :param status: The status of the operation (e.g., 'success', 'failure').
        """
        logging.info(f'Operation: {operation}, Status: {status}')

    def log_error(self, error_message):
        """
        Logs an error message.

        :param error_message: The error message to log.
        """
        logging.error(f'Error: {error_message}')