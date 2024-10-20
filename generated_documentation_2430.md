# Git Operations Documentation

## Overview
This project provides a set of basic Git operations encapsulated in the `GitOperations` class. The class allows users to initialize a Git repository and add files to it.

## Class: `GitOperations`

### Methods

#### `initialize_repository(repo_name: str) -> bool`
Initializes a new Git repository in the specified directory.

- **Parameters**
  - `repo_name`: The name of the repository to be created.
  
- **Returns**
  - `True` if the repository was initialized successfully, `False` otherwise.

- **Example**
  ```python
  GitOperations.initialize_repository("my_repo")
  ```

#### `add_file(repo_name: str, file_name: str) -> bool`
Adds a file to the specified Git repository.

- **Parameters**
  - `repo_name`: The name of the repository to which the file will be added.
  - `file_name`: The name of the file to be added.

- **Returns**
  - `True` if the file was added successfully, `False` otherwise.

- **Example**
  ```python
  GitOperations.add_file("my_repo", "file.txt")
  ```

## Testing
Unit tests are provided in the `TestGitOperations` class to validate the functionality of the `GitOperations` class.

### Test Methods
- `test_initialize_repository()`: Tests successful initialization of a Git repository.
- `test_initialize_existing_repository()`: Tests the case where an attempt is made to initialize an existing repository.

### Running Tests
To run the tests, execute:
```bash
python -m unittest discover
```

## File Structure
- `git_operations.py`: Contains the `GitOperations` class.
- `test_git_operations.py`: Contains unit tests for the `GitOperations` class.