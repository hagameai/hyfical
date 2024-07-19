# Project Documentation

## Overview
This project encapsulates basic Git operations through a Python class, providing functionalities to initialize repositories and manage files within them.

## File Structure
```
.
├── git_operations.py        # Main class for Git operations
├── test_git_operations.py   # Unit tests for Git operations
...
```

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): Name of the repository to be created.
- **Returns:**
  - bool: True if the repository was initialized successfully, False otherwise.

#### `add_file(repo_name, file_name, content)`
Adds a file to the specified Git repository with the given content.

- **Parameters:**
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to be added.
  - `content` (str): Content to be written in the file.

## Testing

### TestGitOperations Class
Unit tests that validate the functionalities of the `GitOperations` class.

#### Methods

- `setUp()`: Creates a temporary directory for testing.
- `tearDown()`: Removes the test directory after tests.
- `test_initialize_repository()`: Tests the successful initialization of a Git repository.
- `test_initialize_existing_repository()`: Tests the behavior when trying to initialize an existing repository.

## Usage
To use the `GitOperations` class, import it and call the desired method. Ensure that the required permissions are granted for file and directory operations. 

## Contribution
For contributions, please follow the standard pull request process and ensure tests are updated accordingly.