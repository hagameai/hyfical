# Project Documentation

## Overview
This project encapsulates basic Git operations in Python, providing functionalities to initialize repositories and manage files.

## File Structure
- **Total Files**: 142
- **Total Lines**: 8880
- **File Types**: 
  - Python files: 91 (`.py`)
  - Markdown files: 51 (`.md`)

## GitOperations Class
The `GitOperations` class contains static methods for performing Git-related operations.

### Methods

#### `initialize_repository(repo_name: str) -> bool`
- **Description**: Initializes a new Git repository in the specified directory.
- **Parameters**:
  - `repo_name`: Name of the repository to be created.
- **Returns**: `True` if successful, `False` if the repository already exists or an error occurs.

#### `add_file(repo_name: str, file_name: str) -> bool`
- **Description**: Adds a file to the specified Git repository.
- **Parameters**:
  - `repo_name`: Name of the repository.
  - `file_name`: Name of the file to be added.
- **Returns**: `True` if file added successfully, `False` otherwise.

## Testing
Unit tests for the `GitOperations` class are provided to ensure functionalities work as expected.

### Test Class: `TestGitOperations`
- **Setup**: Creates a temporary directory for testing.
- **Teardown**: Cleans up the test directory after tests complete.

#### Test Methods
- `test_initialize_repository`: Validates repository initialization.
- `test_initialize_existing_repository`: Checks behavior when initializing an existing repository.

## Usage
To utilize the `GitOperations` class, import it into your Python script and call the methods as needed. Ensure Git is installed and accessible in your system's PATH. 

## Contribution
For contributions, please fork the repository and submit a pull request with your changes.