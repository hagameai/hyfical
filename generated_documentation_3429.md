# Project Documentation

## Overview
This project provides a Python class encapsulating basic Git operations, allowing users to initialize repositories and manage files within them.

## File Structure
- **Python Files**: 78
- **Markdown Files**: 42
- **Total Lines**: 7481

## GitOperations Class

### Description
The `GitOperations` class contains static methods to perform fundamental Git operations.

### Methods

#### `initialize_repository(repo_name)`
- **Description**: Initializes a new Git repository in the specified directory.
- **Parameters**: 
  - `repo_name` (str): The name of the repository to be created.
- **Returns**: 
  - `bool`: True if initialized successfully, otherwise False.

#### `add_file(repo_name, file_name)`
- **Description**: Adds a file to the specified Git repository.
- **Parameters**: 
  - `repo_name` (str): The name of the repository.
  - `file_name` (str): The name of the file to add.
- **Returns**: 
  - `bool`: True if the file was added successfully, otherwise False.

## Testing
Unit tests are implemented using the `unittest` framework to validate the functionality of the `GitOperations` class. Key tests include:

- Successful initialization of a Git repository.
- Handling of attempts to initialize an existing repository.

### Running Tests
Execute the tests using the command:
```bash
python -m unittest discover
```

## Usage
To use the `GitOperations` class:
1. Import the class:
   ```python
   from git_operations import GitOperations
   ```
2. Call methods as needed:
   ```python
   GitOperations.initialize_repository("my_repo")
   ```

## Contributions
Contributions are welcome! Please adhere to the coding standards and best practices outlined in this documentation.