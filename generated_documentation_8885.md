# Git Operations Documentation

## Overview
This project provides a set of basic Git operations implemented in Python. It includes functionalities for initializing a repository, adding files, and committing changes. The implementation follows good programming practices and includes error handling.

## File Structure
- **git_operations.py**: Contains the `GitOperations` class with methods for Git functionalities.
- **tests/**: Directory containing unit tests for the Git operations.

## Class: GitOperations

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters**: 
    - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
    - `bool`: True if the repository was initialized successfully, False otherwise.
- **Exceptions**: 
    - Catches and prints exceptions related to repository initialization.

#### `add_file(repo_name, file_name)`
Adds a specified file to the Git repository.

- **Parameters**: 
    - `repo_name` (str): The name of the repository where the file will be added.
    - `file_name` (str): The name of the file to be added.
- **Returns**: 
    - `bool`: True if the file was added successfully, False otherwise.

### Error Handling
The methods include error handling to manage scenarios such as existing repositories and file addition failures.

## Testing
This project includes a suite of unit tests for validating the functionalities of the `GitOperations` class. The tests cover both normal and exceptional scenarios.

### Test Structure
- **Test Class**: `TestGitOperations`
- **Methods**:
    - `setUp()`: Prepares a temporary testing directory.
    - `tearDown()`: Cleans up the testing directory after tests.
    - `test_initialize_repository()`: Tests successful repository initialization.
    - `test_initialize_existing_repository()`: Tests behavior when initializing an existing repository.

## Contribution
Contributions are welcome! Please ensure that any contributions adhere to the project's coding standards and include appropriate unit tests.