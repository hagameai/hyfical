# Project Documentation

## Overview

This project consists of a set of Python scripts that encapsulate basic Git operations. The main class, `GitOperations`, provides methods for initializing repositories and adding files.

## File Structure

- **Total Files**: 141
- **Total Lines**: 8840
- **File Types**:
  - Python scripts: 90 (`.py`)
  - Markdown documentation: 51 (`.md`)

## GitOperations Class

### Description

The `GitOperations` class provides static methods to perform various Git operations.

### Methods

#### `initialize_repository(repo_name)`

- **Description**: Initializes a new Git repository in the specified directory.
- **Parameters**:
  - `repo_name` (str): The name of the repository to be created.
- **Returns**: 
  - `bool`: True if the repository was initialized successfully, False otherwise.

#### `add_file(repo_name, file_name)`

- **Description**: Adds a file to the specified Git repository.
- **Parameters**:
  - `repo_name` (str): The name of the repository.
  - `file_name` (str): The name of the file to be added.
- **Returns**: 
  - `bool`: True if the file was added successfully, False otherwise.

## Testing

### TestGitOperations Class

The `TestGitOperations` class provides unit tests for the `GitOperations` class.

#### Methods

- `setUp()`: Creates a temporary directory for testing.
- `tearDown()`: Cleans up the test directory after tests.
- `test_initialize_repository()`: Tests successful initialization of a Git repository.
- `test_initialize_existing_repository()`: Tests behavior when trying to initialize an existing repository.

## Contributing

Contributions are welcome! Please follow the project's coding standards and include tests for any new features or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.