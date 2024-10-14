# Project Documentation

## Overview
This project provides a set of basic Git operations encapsulated within a `GitOperations` class. It allows users to create and manage Git repositories programmatically.

## File Structure
- **Source Files**
  - Python files: 82
  - Markdown files: 47

- **Tests**
  - Unit tests for `GitOperations` class are included.

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): Name of the repository to be created.

- **Returns:**
  - `bool`: True if the repository was initialized successfully, False otherwise.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters:**
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to be added.

- **Returns:**
  - `bool`: True if the file was added successfully, False otherwise.

## Testing

### Running Tests
To run the unit tests, use:
```bash
python -m unittest discover
```

### Test Cases
- **TestGitOperations Class**
  - Tests for repository initialization and file addition.
  - Includes setup and teardown methods for clean testing environments.

## Contribution
Contributions are welcome. Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.