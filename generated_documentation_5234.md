# Git Operations Documentation

## Overview
This project provides a Python class, `GitOperations`, to perform basic Git operations, such as initializing a repository and adding files. The implementation relies on the `subprocess` module to interact with Git commands.

## Class: `GitOperations`

### Methods

#### `initialize_repository(repo_name: str) -> bool`
Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): Name of the repository to be created.
  
- **Returns:**
  - `bool`: True if the repository was initialized successfully, False otherwise.

- **Exceptions:**
  - Prints an error message if initialization fails.

#### `add_file(repo_name: str, file_name: str, content: str) -> bool`
Adds a file to the specified Git repository with the provided content.

- **Parameters:**
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to be added.
  - `content` (str): Content to be written to the file.

- **Returns:**
  - `bool`: True if the file was added successfully, False otherwise.

## Unit Testing

### Test Suite: `TestGitOperations`

Unit tests for the `GitOperations` class are implemented using the `unittest` framework. Key tests include:

- **test_initialize_repository**: Verifies that a new repository is created successfully.
- **test_initialize_existing_repository**: Checks that attempting to create an existing repository returns False.

### Running Tests
To execute the tests, use the following command:
```bash
python -m unittest discover
```

## Directory Structure
- `/git_operations`: Contains the main implementation files.
- `/tests`: Contains the unit test files.

## Dependencies
- Python 3.x
- Git must be installed and accessible in the system's PATH.

## Usage
1. Import the `GitOperations` class.
2. Call methods as needed to perform Git operations.

## License
This project is licensed under the MIT License. See the LICENSE file for details.