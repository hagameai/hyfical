# Project Documentation

## Overview
This project provides a set of basic Git operations encapsulated within the `GitOperations` class, allowing users to initialize repositories and manage files easily.

## File Structure
- **Total Files**: 96
- **Total Lines**: 5963
- **File Types**:
  - Python Files: 62
  - Markdown Files: 34

## GitOperations Class
### Description
The `GitOperations` class includes methods for basic Git functionalities such as initializing a repository and adding files.

### Methods

#### `initialize_repository(repo_name)`
- **Description**: Initializes a new Git repository in the specified directory.
- **Parameters**:
  - `repo_name`: Name of the repository to be created.
- **Returns**: 
  - `True` if successful, `False` otherwise.

#### `add_file(repo_name, file_name)`
- **Description**: Adds a specified file to the Git repository.
- **Parameters**:
  - `repo_name`: Name of the repository.
  - `file_name`: Name of the file to add.
- **Returns**: 
  - `True` if file is added successfully, `False` otherwise.

## Testing
The project includes unit tests for the `GitOperations` class to ensure functionalities work as expected.

### Test Class: `TestGitOperations`
- **Framework**: `unittest`
  
#### Test Methods
- `test_initialize_repository`: Validates successful repository initialization.
- `test_initialize_existing_repository`: Checks behavior when trying to initialize an existing repository.

## Usage
To use the GitOperations class, import it in your script and call the methods as needed to manage your Git repositories.

## Contribution
Please follow the standard coding practices and submit a pull request for any enhancements or bug fixes.