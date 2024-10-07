# Project Documentation

## Overview
This project provides a set of utilities for performing basic Git operations encapsulated within the `GitOperations` class. The implementation is designed to streamline the process of repository management.

## File Structure
- **Total Files:** 122
- **Total Lines:** 7620
- **File Types:**
  - Python Files: 79 (`.py`)
  - Markdown Files: 43 (`.md`)

## GitOperations Class

### Description
The `GitOperations` class contains static methods for initializing a Git repository and adding files to it.

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.
- **Parameters:**
  - `repo_name` (str): Name of the repository to be created.
- **Returns:** 
  - `bool`: `True` if the repository was initialized successfully, `False` otherwise.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.
- **Parameters:**
  - `repo_name` (str): The path to the repository.
  - `file_name` (str): The name of the file to be added.
- **Returns:**
  - `bool`: `True` if the file was added successfully, `False` otherwise.

## Testing
The project includes unit tests for the `GitOperations` class. Tests are organized using the `unittest` framework.

### Test Structure
- **Test Class:** `TestGitOperations`
- **Key Tests:**
  - `test_initialize_repository`: Validates successful initialization of a Git repository.
  - `test_initialize_existing_repository`: Checks handling of attempts to initialize an existing repository.

### Running Tests
To run the tests, use the command:
```bash
python -m unittest discover
```

## Contributing
Contributions are welcome! Please follow the standard Git workflow for submitting changes. 

## License
This project is licensed under the MIT License.