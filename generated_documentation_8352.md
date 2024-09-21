# Git Operations Documentation

## Overview
This project provides a set of basic Git operations encapsulated within the `GitOperations` class. It includes functionality for initializing a repository and adding files.

## File Structure
- **Python Files**: 73
- **Markdown Files**: 38
- **Total Files**: 111
- **Total Lines**: 6875

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters**:
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: True if the repository was initialized successfully, False if it already exists or an error occurred.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters**:
  - `repo_name` (str): Name of the repository where the file will be added.
  - `file_name` (str): The name of the file to be added.

### Usage Example
```python
from git_operations import GitOperations

# Initialize a repository
GitOperations.initialize_repository("my_repo")

# Add a file to the repository
GitOperations.add_file("my_repo", "my_file.txt")
```

## Testing

### TestGitOperations Class
Unit tests for the `GitOperations` class validate basic functionalities such as initializing repositories and adding files.

#### Tests Included
- **test_initialize_repository**: Verifies successful initialization of a Git repository.
- **test_initialize_existing_repository**: Checks behavior when trying to initialize an already existing repository.

### Running Tests
To run the tests, execute the following command:
```bash
python -m unittest discover
```

## Conclusion
The `GitOperations` class provides essential Git functionalities, making it easier to manage repositories programmatically. Ensure to run tests regularly to validate functionality.