# Project Documentation

## Overview
This project provides a set of functionalities for basic Git operations, implemented in Python. It includes features such as initializing a repository, adding files, and committing changes, with appropriate error handling.

## File Structure
- `git_operations.py`: Contains the implementation of Git operations.
- `test_git_operations.py`: Contains unit tests for validating the functionalities of the Git operations.

## Git Operations

### `GitOperations` Class
A class to encapsulate basic Git operations.

#### Methods

- **`initialize_repository(repo_name)`**
  - Initializes a new Git repository in the specified directory.
  - **Parameters**: 
    - `repo_name` (str): Name of the repository to be created.
  - **Returns**: 
    - `bool`: True if the repository was initialized successfully, False otherwise.

- **`add_file(repo_name, file_name)`**
  - Adds a file to the specified Git repository.
  - **Parameters**: 
    - `repo_name` (str): Name of the repository.
    - `file_name` (str): Name of the file to be added.

## Testing

### Test Suite
The project includes a test suite located in `test_git_operations.py`, which uses `unittest` to validate the functionality of the Git operations.

#### Test Cases

- **`test_initialize_repository`**
  - Tests successful initialization of a Git repository.
  
- **`test_initialize_existing_repository`**
  - Tests the behavior when attempting to initialize an already existing repository.

- **`test_add_file_to_repository`**
  - Tests adding a file to the Git repository.

## Usage
To use the Git operations, instantiate the `GitOperations` class and call the desired method, passing the appropriate parameters.

## Contributing
Contributions to enhance the functionalities or improve the documentation are welcome. Please follow the standard Git workflow for contributions.