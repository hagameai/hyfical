# Project Documentation

## Overview
This project encapsulates basic Git operations using Python. It provides functionalities to initialize a Git repository and add files to it.

## File Structure
- **Total Files**: 43
- **Total Lines**: 2604
- **File Types**:
  - `.py`: 29 files
  - `.md`: 14 files

## GitOperations Class
### Description
The `GitOperations` class includes methods for basic Git functionalities.

### Methods

#### `initialize_repository(repo_name)`
- **Description**: Initializes a new Git repository.
- **Parameters**:
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: `True` if successful, `False` otherwise.

#### `add_file(repo_name, file_name, content)`
- **Description**: Adds a file to the specified Git repository.
- **Parameters**:
  - `repo_name` (str): Path to the repository.
  - `file_name` (str): Name of the file to add.
  - `content` (str): Content of the file.
- **Returns**: `True` if the file was added successfully, `False` otherwise.

## Testing
### Test Suite
The project includes unit tests for the `GitOperations` class using the `unittest` framework.

### Test Cases
- **test_initialize_repository**: Validates successful repository initialization.
- **test_initialize_existing_repository**: Checks behavior when trying to initialize an existing repository.

### Running Tests
To run the tests, execute:
```bash
python -m unittest discover
```

## Installation
1. Clone the repository.
2. Ensure Python and Git are installed.
3. Install dependencies if any.

## Contributing
Contributions are welcome! Please submit a pull request with your changes.