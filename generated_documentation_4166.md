# Project Documentation

## Overview
This project implements basic Git operations through a Python class, `GitOperations`. It provides functionalities like initializing a repository and adding files.

## File Structure
- **Python Files**: 65
- **Markdown Files**: 35
- **Total Files**: 100
- **Total Lines**: 6189

## GitOperations Class
### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.
- **Parameters**: 
  - `repo_name` (str): Name of the repository to create.
- **Returns**: 
  - `bool`: True if successful, False otherwise.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.
- **Parameters**:
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to add.

## Testing
Unit tests are implemented using the `unittest` framework. Each test case ensures that the Git operations work as expected.

### Test Cases
- **`test_initialize_repository`**: Validates successful initialization of a repository.
- **`test_initialize_existing_repository`**: Checks behavior when trying to initialize an existing repository.

## Requirements
- Python 3.x
- Git installed on the system

## Usage
Import the `GitOperations` class and use its methods to perform Git operations programmatically.