# Project Documentation

## Overview
This project implements basic Git operations encapsulated within a `GitOperations` class. It includes unit tests to validate the functionality of these operations.

## File Structure
- **Total Files:** 37
- **Total Lines:** 2197
- **File Types:**
  - Python files (`.py`): 24
  - Markdown files (`.md`): 13

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): Name of the repository to be created.
- **Returns:** 
  - `True` if the repository was initialized successfully, `False` otherwise.

#### `add_file(repo_name, file_name, content)`
Adds a file to the specified Git repository.

- **Parameters:**
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to be added.
  - `content` (str): Content to write to the file.

## Unit Tests

### TestGitOperations Class
Unit tests for the `GitOperations` class.

#### Setup and Teardown
- **setUp()**: Creates a temporary directory for testing.
- **tearDown()**: Removes the test directory after tests.

### Test Cases
- `test_initialize_repository`: Verifies successful initialization of a new Git repository.
- `test_initialize_existing_repository`: Checks behavior when attempting to initialize an existing repository.

## Running Tests
To run the tests, use the following command:
```bash
python -m unittest discover
```

## Contribution
Please submit issues and pull requests to contribute to the project. Ensure to follow coding standards and include tests for new features.