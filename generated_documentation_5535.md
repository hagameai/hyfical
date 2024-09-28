# Project Documentation

## Overview
This project contains a set of Python scripts that encapsulate basic Git operations. The main class, `GitOperations`, provides methods for initializing repositories and managing files.

## File Structure
- **Total Files**: 116
- **Total Lines**: 7209
- **File Types**:
  - **Python files**: 75 (`.py`)
  - **Markdown files**: 41 (`.md`)

## GitOperations Class

### Methods

#### `initialize_repository(repo_name: str) -> bool`
Initializes a new Git repository in the specified directory.

- **Parameters**: 
  - `repo_name`: Name of the repository to be created.
- **Returns**: 
  - `True` if the repository was initialized successfully, `False` otherwise.

#### `add_file(repo_name: str, file_name: str) -> bool`
Adds a file to the specified Git repository.

- **Parameters**: 
  - `repo_name`: The name of the repository.
  - `file_name`: The name of the file to be added.
- **Returns**: 
  - `True` if the file was added successfully, `False` otherwise.

## Testing

### Unit Tests
The project includes unit tests for the `GitOperations` class using the `unittest` framework.

#### Test Class: `TestGitOperations`
- **Setup**: Creates a temporary directory for testing.
- **Teardown**: Removes the test directory after tests.

#### Test Methods
- `test_initialize_repository`: Tests the successful initialization of a Git repository.
- `test_initialize_existing_repository`: Tests the behavior when attempting to initialize an existing repository.

## Contributing
Contributions are welcome. Please adhere to the project's coding standards and include tests for any new features.