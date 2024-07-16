# Project Documentation

## Overview
This project encapsulates basic Git operations in Python. The core functionality is provided by the `GitOperations` class, which allows users to initialize repositories and manage files.

## File Structure
- **Total Files:** 41
- **Total Lines:** 2474
- **File Types:**
  - Python files: 27
  - Markdown files: 14

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): The name of the repository to be created.
- **Returns:** 
  - `bool`: True if the repository was initialized successfully, False otherwise.

#### `add_file(repo_name, file_name, content)`
Adds a file to the specified Git repository.

- **Parameters:**
  - `repo_name` (str): The name of the repository.
  - `file_name` (str): The name of the file to be added.
  - `content` (str): The content to write to the file.
- **Returns:** 
  - `bool`: True if the file was added successfully, False otherwise.

## Testing
The project includes unit tests for the `GitOperations` class. Tests are implemented using the `unittest` framework.

### Test Cases
- `test_initialize_repository`: Validates successful repository initialization.
- `test_initialize_existing_repository`: Checks behavior when initializing an already existing repository.

## Installation
Ensure Python and Git are installed. Clone the repository and run tests using the command:
```bash
python -m unittest discover
```

## Contributions
Contributions are welcome. Please follow the standard pull request process and ensure tests pass before merging.