# Project Documentation

## Overview

This project provides a set of utilities for basic Git operations, encapsulated within the `GitOperations` class. The functionalities include initializing a repository and adding files to it.

## File Structure

- **Total Files**: 143
- **Total Lines**: 8939
- **File Types**:
  - Python (`.py`): 91
  - Markdown (`.md`): 52

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`

- **Description**: Initializes a new Git repository in the specified directory.
- **Parameters**:
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: True if the repository was initialized successfully, False otherwise.

#### `add_file(repo_name, file_name)`

- **Description**: Adds a file to the specified Git repository.
- **Parameters**:
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to be added.
- **Returns**: 
  - `bool`: True if the file was added successfully, False otherwise.

## Testing

### TestGitOperations Class

Contains unit tests for the `GitOperations` class.

- **setUp**: Creates a temporary directory for testing.
- **tearDown**: Cleans up test directories post execution.

### Test Cases

1. **test_initialize_repository**: Validates successful initialization of a Git repository.
2. **test_initialize_existing_repository**: Checks behavior when attempting to initialize an existing repository.

## Usage

To use the Git operations, import the `GitOperations` class and call the respective methods as needed. Ensure that Git is installed and accessible in your environment.