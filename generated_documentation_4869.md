# Project Documentation

## Overview
This project implements basic Git operations using Python. It provides functionalities to initialize a Git repository, add files, and commit changes, encapsulated in a class called `GitOperations`.

## File Structure
- **Source Files**: 
  - `git_operations.py`: Contains the `GitOperations` class with methods for Git operations.
- **Test Files**: 
  - `test_git_operations.py`: Unit tests for validating Git operations functionality.

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters**:
  - `repo_name` (str): The name of the repository to be created.
- **Returns**: `True` if the repository was initialized successfully, `False` otherwise.

#### `add_file(repo_name, file_name)`
Adds a specified file to the Git repository.

- **Parameters**:
  - `repo_name` (str): The name of the repository.
  - `file_name` (str): The name of the file to be added.
- **Returns**: `True` if the file was added successfully, `False` otherwise.

## Testing

### TestGitOperations Class
This class contains unit tests to validate the functionalities of the `GitOperations` class.

#### Test Cases
- **test_initialize_repository**: Validates the successful initialization of a Git repository.
- **test_initialize_existing_repository**: Ensures that attempting to initialize an existing repository fails gracefully.

### Running Tests
Use the following command to run the tests:
```bash
python -m unittest discover
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License.