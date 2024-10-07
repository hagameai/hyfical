# Project Documentation

## Overview
This project encapsulates basic Git operations using Python. It provides functionalities to initialize a Git repository and manage files within it.

## File Structure
- **Total Files**: 123
- **Total Lines**: 7677
- **File Types**:
  - Python Files: 79 (`.py`)
  - Markdown Files: 44 (`.md`)

## GitOperations Class
The `GitOperations` class provides static methods for performing Git operations.

### Methods

#### `initialize_repository(repo_name: str) -> bool`
Initializes a new Git repository in the specified directory.

- **Parameters**:
  - `repo_name`: Name of the repository to be created.
- **Returns**: 
  - `True` if the repository was initialized successfully, `False` otherwise.

#### `add_file(repo_name: str, file_name: str) -> bool`
Adds a file to the specified Git repository.

- **Parameters**:
  - `repo_name`: Name of the repository.
  - `file_name`: Name of the file to be added.
- **Returns**: 
  - `True` if the file was added successfully, `False` otherwise.

## Testing
Unit tests for the `GitOperations` class are provided in separate test files.

### Test Class: `TestGitOperations`
- **Framework**: `unittest`
- **Setup**: Creates a temporary directory for testing.
- **Teardown**: Removes the test directory after tests.

### Key Tests
- `test_initialize_repository`: Verifies successful initialization of a Git repository.
- `test_initialize_existing_repository`: Tests behavior when trying to initialize an existing repository.

## Usage
To utilize the `GitOperations` class, import it in your Python script and call the methods as needed. Ensure that Git is installed and accessible in your environment.