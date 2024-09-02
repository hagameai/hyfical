# Git Operations Documentation

## Overview
This project provides a set of basic Git operations encapsulated within the `GitOperations` class, allowing users to initialize repositories and manage files within them.

## Class: `GitOperations`
The `GitOperations` class includes static methods to perform various Git-related tasks.

### Method: `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): The name of the repository to be created.
  
- **Returns:** 
  - `bool`: `True` if the repository was initialized successfully, `False` otherwise.

### Method: `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters:**
  - `repo_name` (str): The name of the repository.
  - `file_name` (str): The name of the file to be added.

- **Returns:**
  - `bool`: `True` if the file was added successfully, `False` otherwise.

## Testing
The project contains unit tests for the `GitOperations` class, validating the core functionalities.

### Test Class: `TestGitOperations`
- **Methods:**
  - `setUp()`: Creates a temporary directory for testing.
  - `tearDown()`: Cleans up the temporary directory after tests.
  - `test_initialize_repository()`: Tests the successful initialization of a Git repository.
  - `test_initialize_existing_repository()`: Tests behavior when initializing an existing repository.

## Usage
To use the `GitOperations` class, import it and call the desired methods. Ensure Git is installed and accessible in your environment.

```python
from git_operations import GitOperations

# Example usage
GitOperations.initialize_repository("my_repo")
```