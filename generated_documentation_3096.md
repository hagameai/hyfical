# Project Documentation

## Overview
This project implements basic Git operations encapsulated within a Python class, `GitOperations`. The project consists of multiple Python files and corresponding unit tests.

## File Structure
- **Total Files**: 104
- **Total Lines**: 6436
- **File Types**: 
  - `.py`: 68 
  - `.md`: 36

## Class: GitOperations
The `GitOperations` class provides static methods to perform basic Git operations.

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters**: 
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: `True` if the repository was initialized successfully, `False` otherwise.

#### `add_file(repo_name, file_name)`
Adds a specified file to the Git repository.

- **Parameters**: 
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to add.
- **Returns**: 
  - `bool`: `True` if the file was added successfully, `False` otherwise.

## Testing
Unit tests for the `GitOperations` class are implemented using the `unittest` framework. Each test case creates a temporary directory for testing purposes.

### Test Cases

#### `test_initialize_repository`
Validates successful initialization of a Git repository.

#### `test_initialize_existing_repository`
Checks the behavior when trying to initialize an already existing repository.

## Running Tests
To run the tests, execute the following command in the terminal:
```bash
python -m unittest discover
```

## Conclusion
This documentation provides an overview of the Git operations implemented in the project, along with instructions for testing the functionality.