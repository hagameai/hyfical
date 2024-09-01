# Project Documentation

## Overview
This project encapsulates basic Git operations through a Python class `GitOperations`. It provides functionality to initialize repositories and manage files within them.

## File Structure
- **Total Files**: 88
- **Total Lines**: 5511
- **File Types**:
  - `.py`: 58
  - `.md`: 30

## GitOperations Class
### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters**: 
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: `True` if initialized successfully, `False` if the repository already exists or an error occurs.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters**: 
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to be added.
- **Returns**: 
  - `bool`: `True` if the file was added successfully, `False` otherwise.

## Testing
Unit tests are implemented using the `unittest` framework. Each test case ensures the functionality of the `GitOperations` methods.

### Test Class: `TestGitOperations`
#### Methods

- `setUp()`: Creates a temporary directory for testing.
- `tearDown()`: Cleans up the test directory after tests.
- `test_initialize_repository()`: Tests successful initialization of a Git repository.
- `test_initialize_existing_repository()`: Tests behavior when initializing an existing repository.

## Usage
To use the `GitOperations` class, import it and call the desired methods as shown in the test cases.

```python
from git_operations import GitOperations

# Example usage
GitOperations.initialize_repository('my_repo')
```

## Contributing
Contributions are welcome. Please submit a pull request with your changes. Ensure all tests are passing before submitting.