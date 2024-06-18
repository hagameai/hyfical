# Project Documentation

## Overview
This project contains a set of Python scripts that implement basic Git operations, including initializing repositories, adding files, and committing changes.

## File Structure
```
.
├── git_operations.py          # Main file for Git operations
├── test_git_operations.py     # Unit tests for Git operations
├── ...
```

## Git Operations
### `git_operations.py`
This module encapsulates basic Git functionalities through the `GitOperations` class.

#### Class: `GitOperations`
- **Methods:**
  - `initialize_repository(repo_name: str) -> bool`
    - Initializes a new Git repository in the specified directory.
    - Returns `True` if successful, `False` if the repository already exists.
  
  - `add_file(repo_name: str, file_name: str) -> bool`
    - Adds a specified file to the Git repository.
    - Returns `True` if successful, `False` otherwise.

## Testing
### `test_git_operations.py`
This file contains unit tests for the `GitOperations` class.

#### Test Class: `TestGitOperations`
- **Methods:**
  - `setUp()`
    - Prepares a temporary directory for testing.
  
  - `tearDown()`
    - Cleans up the temporary directory after tests.

  - `test_initialize_repository()`
    - Validates successful initialization of a Git repository.
  
  - `test_initialize_existing_repository()`
    - Tests behavior when initializing an existing repository.

## Contribution
To contribute, please fork the repository and submit a pull request with clear descriptions of your changes. 

## License
This project is licensed under the MIT License.