# Project Documentation

## Overview

This project encapsulates basic Git operations using Python. It includes functionality to initialize a Git repository and manage files within it.

## File Structure

- **Source Code**: `*.py`
- **Tests**: `*.py`
- **Documentation**: `*.md`

### Total Files: 126
- Python files: 80
- Markdown files: 46
- Total Lines of Code: 7861

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`

- **Description**: Initializes a new Git repository in the specified directory.
- **Parameters**: 
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: True if initialized successfully, False otherwise.

#### `add_file(repo_name, file_name)`

- **Description**: Adds a file to the specified Git repository.
- **Parameters**: 
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to be added.
- **Returns**: 
  - `bool`: True if the file was added successfully, False otherwise.

## Testing

### TestGitOperations Class

- **Purpose**: Unit tests for GitOperations class.
- **Methods**:
  - `setUp()`: Creates a temporary directory for testing.
  - `tearDown()`: Cleans up the test directory.
  - `test_initialize_repository()`: Tests the successful initialization of a Git repository.
  - `test_initialize_existing_repository()`: Tests handling of existing repositories.

### Running Tests

To execute the tests, use the command:

```bash
python -m unittest discover
```

## Contribution

For contributions, please follow the standard fork-and-pull request workflow. Ensure all tests pass before submitting a pull request.