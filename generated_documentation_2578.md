# Project Documentation

## Overview
This project consists of 34 files with a total of 2010 lines, primarily written in Python (.py) and Markdown (.md). It focuses on encapsulating basic Git operations.

## File Structure
- **Source Files**: 22 Python files
- **Documentation Files**: 12 Markdown files

## GitOperations Class
The `GitOperations` class provides methods for basic Git functionalities:

### Methods
- **initialize_repository(repo_name)**: Initializes a new Git repository.
  - **Parameters**: 
    - `repo_name` (str): The name of the repository to be created.
  - **Returns**: 
    - `True` if successful, `False` if the repository already exists or an error occurs.

- **add_file(repo_name, file_name)**: Adds a specified file to the Git repository.
  - **Parameters**: 
    - `repo_name` (str): The name of the repository.
    - `file_name` (str): The name of the file to be added.
  - **Returns**: 
    - `True` if the file is added successfully, `False` otherwise.

## Testing
Unit tests for `GitOperations` are implemented using the `unittest` framework. Each test case verifies the functionality of methods in the `GitOperations` class.

### Test Cases
- **test_initialize_repository**: Ensures a repository is initialized correctly.
- **test_initialize_existing_repository**: Ensures proper handling when attempting to initialize an existing repository.

## Setup and Usage
1. Clone the repository.
2. Install necessary dependencies.
3. Run tests using:
   ```bash
   python -m unittest discover
   ```

## Contribution
Contributions are welcome. Please submit a pull request or open an issue for improvements or bug fixes.