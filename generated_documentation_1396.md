# Project Documentation

## Overview
This project provides a set of utilities for performing basic Git operations via a Python class. The main functionalities include initializing a Git repository and adding files to it.

## File Structure
- **Total Files**: 46
- **Total Lines**: 2751
- **File Types**:
  - Python Files: 29 (`.py`)
  - Markdown Files: 17 (`.md`)

## GitOperations Class
### Description
The `GitOperations` class encapsulates basic Git functionalities.

### Methods

#### `initialize_repository(repo_name)`
- **Description**: Initializes a new Git repository in the specified directory.
- **Parameters**:
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: True if the repository was initialized successfully, False otherwise.

#### `add_file(repo_name, file_name, content)`
- **Description**: Adds a specified file with content to the Git repository.
- **Parameters**:
  - `repo_name` (str): Path to the repository.
  - `file_name` (str): Name of the file to be added.
  - `content` (str): Content to write to the file.
- **Returns**: 
  - `bool`: True if the file was added successfully, False otherwise.

## Testing
### TestGitOperations Class
- **Framework**: `unittest`
- **Setup**: Creates a temporary directory for testing.
- **Teardown**: Removes the test directory after tests.

### Key Tests
1. **test_initialize_repository**: Verifies successful repository initialization.
2. **test_initialize_existing_repository**: Checks behavior when initializing an existing repository.

## Usage
Instantiate the `GitOperations` class to access methods for managing Git repositories. Ensure Git is installed and available in the system PATH. 

### Example
```python
from git_operations import GitOperations

# Initialize a repository
GitOperations.initialize_repository("my_repo")
```

## Contributing
Contributions are welcome. Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.