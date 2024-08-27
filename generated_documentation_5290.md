# Project Documentation

## Overview

This project encapsulates basic Git operations through a Python class, providing functionalities to manage Git repositories programmatically.

## File Structure

- **Python Files**: 53
- **Markdown Files**: 29

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`

Initializes a new Git repository in the specified directory.

- **Parameters**:
  - `repo_name`: Name of the repository to be created.
- **Returns**: 
  - `True` if the repository was initialized successfully, `False` otherwise.

#### `add_file(repo_name, file_name)`

Adds a file to the specified Git repository.

- **Parameters**:
  - `repo_name`: Name of the repository.
  - `file_name`: Name of the file to be added.
- **Returns**: 
  - `True` if the file was added successfully, `False` otherwise.

## Testing

### TestGitOperations Class

Unit tests to validate functionalities of the `GitOperations` class.

#### Test Methods

- `test_initialize_repository()`: Validates successful repository initialization.
- `test_initialize_existing_repository()`: Checks behavior when initializing an existing repository.

## Usage

To utilize the `GitOperations` class, import it and call the desired methods as demonstrated in the test cases.