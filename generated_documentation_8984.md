# Project Documentation

## Overview
This project encapsulates basic Git operations through a Python class, `GitOperations`, allowing users to manage Git repositories programmatically.

## File Structure
- **Total Files:** 137
- **Total Lines:** 8625
- **File Types:**
  - **Python Files (.py):** 88
  - **Markdown Files (.md):** 49

## Class: GitOperations

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): Name of the repository to be created.
  
- **Returns:** 
  - `bool`: True if the repository was initialized successfully, False otherwise.

- **Raises:**
  - Prints error message if initialization fails.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters:**
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to be added.

- **Returns:** 
  - `bool`: True if the file was added successfully, False otherwise.

### Unit Tests
The project includes unit tests for validating the functionality of the `GitOperations` class, ensuring that methods perform as expected.

### Test Class: TestGitOperations

#### Methods

##### `setUp()`
Creates a temporary directory for testing.

##### `tearDown()`
Removes the test directory after tests.

##### `test_initialize_repository()`
Tests the successful initialization of a Git repository.

##### `test_initialize_existing_repository()`
Tests the behavior when attempting to initialize an existing repository.

## Installation
To use this project, clone the repository and install the required dependencies.

## Usage
Import the `GitOperations` class and call its methods to perform Git operations programmatically.

## Contribution
Contributions are welcome! Please submit a pull request for any improvements or bug fixes.