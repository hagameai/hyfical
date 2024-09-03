# Project Documentation

## Overview

This project encapsulates basic Git operations through the `GitOperations` class, providing functionalities to initialize repositories and manage files within them.

## File Structure

- **Total Files:** 92
- **Total Lines:** 5707
- **File Types:**
  - Python Files: 59 (`.py`)
  - Markdown Files: 33 (`.md`)

## GitOperations Class

### Description

The `GitOperations` class offers static methods for performing basic Git tasks.

### Methods

#### `initialize_repository(repo_name)`

Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): Name of the repository to be created.
- **Returns:** 
  - `bool`: True if the repository was initialized successfully, False otherwise.

#### `add_file(repo_name, file_name)`

Adds a file to the specified Git repository.

- **Parameters:**
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to add.
- **Returns:**
  - `bool`: True if the file was added successfully, False otherwise.

## Unit Testing

### Overview

Unit tests are provided for the `GitOperations` class to ensure functionality.

### Test Class: `TestGitOperations`

- **Framework:** unittest

#### Methods

- `setUp()`: Creates a temporary directory for testing.
- `tearDown()`: Removes the test directory after tests.

#### Test Cases

- `test_initialize_repository`: Validates successful initialization of a Git repository.
- `test_initialize_existing_repository`: Tests response when attempting to initialize an existing repository.

## Contribution

To contribute to this project, please fork the repository and submit a pull request with your changes. Ensure tests are included for any new features or modifications.