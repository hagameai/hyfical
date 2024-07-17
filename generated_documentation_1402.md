# Project Documentation

## Overview
This project provides a set of classes and methods for performing basic Git operations programmatically. The primary class, `GitOperations`, encapsulates functionalities such as initializing a repository and adding files.

## File Structure
- **Source Files**: 29 Python files (`.py`)
- **Documentation Files**: 14 Markdown files (`.md`)
- **Total Lines**: 2604

## GitOperations Class
### Methods
#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters**: 
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: True if initialized successfully, False otherwise.
- **Exceptions**: Catches and prints errors during initialization.

#### `add_file(repo_name, file_name, content)`
Adds a file to the specified Git repository.

- **Parameters**: 
  - `repo_name` (str): Path to the repository.
  - `file_name` (str): Name of the file to be added.
  - `content` (str): Content to write to the file.
- **Returns**: 
  - `bool`: True if file added successfully, False otherwise.

## Testing
### TestGitOperations Class
Contains unit tests for validating the functionalities of the `GitOperations` class.

#### Tests
- `test_initialize_repository`: Validates successful initialization of a new repository.
- `test_initialize_existing_repository`: Checks behavior when trying to initialize an existing repository.

### Setup and Teardown
- **setUp**: Creates a temporary directory for testing.
- **tearDown**: Cleans up by removing the test directory after tests.

## Contribution
For contributions, please fork the repository and submit a pull request. Ensure to follow the coding standards and include tests for new features.