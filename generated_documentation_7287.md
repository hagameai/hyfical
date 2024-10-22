# Project Documentation

## Overview
This project encapsulates basic Git operations using Python. It includes functionalities to initialize a Git repository and perform file operations within that repository.

## File Structure
- **Total Files**: 136
- **Total Lines**: 8546
- **File Types**: 
  - Python Files: 87 (.py)
  - Markdown Files: 49 (.md)

## GitOperations Class
### Description
The `GitOperations` class provides static methods for performing basic Git operations.

### Methods

#### `initialize_repository(repo_name)`
- **Description**: Initializes a new Git repository in the specified directory.
- **Parameters**:
  - `repo_name` (str): The name of the repository to be created.
- **Returns**: 
  - `bool`: True if the repository was initialized successfully, False otherwise.
- **Exceptions**: Catches and prints any exceptions during the process.

#### `add_file(repo_name, file_name)`
- **Description**: Adds a specified file to the Git repository.
- **Parameters**: 
  - `repo_name` (str): The name of the repository.
  - `file_name` (str): The name of the file to add.
- **Returns**: 
  - `bool`: True if the file was added successfully, False otherwise.

## Testing
### TestGitOperations Class
The `TestGitOperations` class uses `unittest` to validate functionalities of the `GitOperations` class.

#### Setup and Teardown
- **setUp**: Creates a temporary directory for testing.
- **tearDown**: Removes the test directory after tests.

### Test Cases
- **test_initialize_repository**: Tests successful initialization of a Git repository.
- **test_initialize_existing_repository**: Tests behavior when initializing an existing repository.

## Usage
To use the `GitOperations` class, simply import it and call the desired method with appropriate parameters.

## Contribution
Please follow the contribution guidelines in the repository for any changes or enhancements.