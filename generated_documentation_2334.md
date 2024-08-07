# Project Documentation

## Overview

This project provides a set of classes and methods to perform basic Git operations, encapsulated within the `GitOperations` class. The main functionalities include initializing a Git repository and adding files to it.

## File Structure

- **Total Files**: 60
- **Total Lines**: 3573
- **File Types**:
  - Python files: 36 (`.py`)
  - Markdown files: 24 (`.md`)

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`

Initializes a new Git repository in the specified directory.

- **Parameters**:
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: True if the repository was initialized successfully, False otherwise.

#### `add_file(repo_name, file_name)`

Adds a file to the specified Git repository.

- **Parameters**:
  - `repo_name` (str): Directory of the repository.
  - `file_name` (str): Name of the file to be added.

### Usage Example

```python
from git_operations import GitOperations

# Initialize a repository
GitOperations.initialize_repository("my_repo")

# Add a file to the repository
GitOperations.add_file("my_repo", "example.txt")
```

## Testing

### Unit Tests

The project includes unit tests for the `GitOperations` class, validating core functionalities. Tests are implemented using the `unittest` framework.

#### Test Cases

- **test_initialize_repository**: Verifies successful initialization of a Git repository.
- **test_initialize_existing_repository**: Ensures that attempting to initialize an existing repository returns the correct response.

### Running Tests

To run the tests, execute the following command in your terminal:

```bash
python -m unittest discover -s tests
```

## Contribution

Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for details.