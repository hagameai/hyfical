# Project Documentation

## Overview

This project implements a set of basic Git operations encapsulated within a Python class. The project includes unit tests to ensure the functionality works as intended.

## File Structure

- **Total Files**: 119
- **Total Lines**: 7400
- **File Types**:
  - Python files: 77
  - Markdown files: 42

## GitOperations Class

### Description
The `GitOperations` class provides methods for performing basic Git tasks.

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters**:
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: True if successful, False if the repository already exists or an error occurs.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters**:
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to add.
- **Returns**: 
  - `bool`: True if the file was added successfully, False otherwise.

## Testing

### TestGitOperations Class

The `TestGitOperations` class contains unit tests for the `GitOperations` class.

#### Test Methods

- `setUp()`: Creates a temporary directory for testing.
- `tearDown()`: Cleans up the test directory after each test.
- `test_initialize_repository()`: Tests the successful initialization of a Git repository.
- `test_initialize_existing_repository()`: Tests the behavior when trying to initialize an existing repository.

## Usage

To use the `GitOperations` class, import it into your script:

```python
from git_operations import GitOperations
```

Then, you can call its methods as needed. Make sure to handle the return values appropriately to ensure smooth operations.