# Project Documentation

## Overview
This project implements basic Git operations using Python, encapsulated within the `GitOperations` class. It provides functionalities to initialize a repository, add files, and commit changes.

## File Structure
- **Total Files:** 23
- **File Types:**
  - `.py`: 12 files
  - `.md`: 11 files

## Core Functionality

### GitOperations Class
This class contains static methods for performing Git operations.

#### Methods

- **initialize_repository(repo_name)**
  - Initializes a new Git repository in the specified directory.
  - **Parameters:**
    - `repo_name`: Name of the repository to be created.
  - **Returns:** 
    - `True` if successful, `False` if the repository already exists or an error occurs.

- **add_file(repo_name, file_name)**
  - Adds a specified file to the initialized Git repository.
  - **Parameters:**
    - `repo_name`: Name of the repository.
    - `file_name`: Name of the file to be added.
  - **Returns:**
    - `True` if the file was added successfully, `False` otherwise.

## Testing
Unit tests are provided to ensure the functionality of the `GitOperations` class. 

### Test Class: TestGitOperations
- **setUp()**
  - Creates a temporary directory for testing purposes.

- **tearDown()**
  - Cleans up the temporary directory after tests.

### Key Tests
- **test_initialize_repository()**
  - Validates successful repository initialization.
  
- **test_initialize_existing_repository()**
  - Ensures proper handling when attempting to initialize an existing repository.

## Installation & Usage
1. Clone the repository.
2. Ensure Python and Git are installed.
3. Run tests using `unittest` to verify functionality.

## Contribution
Contributions are welcome! Please submit a pull request with a clear description of your changes.