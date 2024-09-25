# Project Documentation

## Overview
This project provides a set of classes for performing basic Git operations encapsulated within a Python class, `GitOperations`. The repository contains scripts for Git initialization, file addition, and other related tasks.

## File Structure
- **Total Files:** 113
- **Total Lines:** 7012
- **File Types:**
  - `.py`: 74
  - `.md`: 39

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): Name of the repository to be created.
- **Returns:**
  - `bool`: True if the repository was initialized successfully, False otherwise.
- **Exceptions:** 
  - Prints an error message if initialization fails.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters:**
  - `repo_name` (str): Name of the repository where the file will be added.
  - `file_name` (str): Name of the file to be added.
- **Returns:**
  - `bool`: True if the file was added successfully, False otherwise.

## Testing

### Test Suite
Unit tests are provided to validate the functionality of the `GitOperations` class. All tests are implemented using the `unittest` framework.

#### Test Cases

- **TestGitOperations Class**
  - `setUp()`: Creates a temporary directory for testing.
  - `tearDown()`: Cleans up the test directory after tests.
  - `test_initialize_repository()`: Validates successful repository initialization.
  - `test_initialize_existing_repository()`: Tests behavior when initializing an existing repository.

## Installation
Clone the repository and install any required dependencies using `pip`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License. See the LICENSE file for details.