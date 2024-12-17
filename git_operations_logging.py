import logging

class GitOperationsLogging:
    """
    A class to handle logging for Git operations.
    This class provides methods to set up logging and log messages for various Git operations.
    """

    def __init__(self, log_file='git_operations.log'):
        """
        Initializes the logging configuration.
        :param log_file: The name of the log file.
        """
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def log_info(self, message):
        """
        Logs an informational message.
        :param message: The message to log.
        """
        logging.info(message)

    def log_warning(self, message):
        """
        Logs a warning message.
        :param message: The message to log.
        """
        logging.warning(message)

    def log_error(self, message):
        """
        Logs an error message.
        :param message: The message to log.
        """
        logging.error(message)

    def log_exception(self, exception):
        """
        Logs an exception message with traceback.
        :param exception: The exception to log.
        """
        logging.exception(str(exception))
