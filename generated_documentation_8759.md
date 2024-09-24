# Git Operations Documentation

## Overview
This project provides a set of basic Git operations encapsulated in a Python class. The main functionalities include initializing a repository and adding files to it.

## File Structure
- **Total Files**: 112
- **Total Lines**: 6933
- **File Types**:
  - **Python Files**: 73
  - **Markdown Files**: 39

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters**:
  - `repo_name`: The name of the repository to be created.
- **Returns**: `True` if successful, `False` otherwise.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters**:
  - `repo_name`: The name of the repository.
  - `file_name`: The name of the file to be added.
- **Returns**: `True` if the file was added successfully, `False` otherwise.

## Testing

### TestGitOperations Class
Unit tests for the `GitOperations` class to validate basic Git functionalities.

#### Test Methods

- **setUp()**: Creates a temporary directory for testing.
- **tearDown()**: Removes the test directory after tests.
- **test_initialize_repository()**: Tests successful initialization of a Git repository.
- **test_initialize_existing_repository()**: Tests behavior when initializing an existing repository.

## Usage
To use the `GitOperations` class, import it into your Python script and call the methods as needed. Ensure you have Git installed in your environment.