# Project Documentation

## Overview
This project contains a set of Python scripts for performing basic Git operations, including repository initialization and file management. It consists of 12 files with a total of 704 lines of code, primarily written in Python.

## File Structure
- **Python Files (.py)**: 7
  - `git_operations.py`: Implements Git operations.
- **Markdown Files (.md)**: 5
  - Documentation and testing information.

## GitOperations Class
### Description
The `GitOperations` class encapsulates methods for basic Git functionalities.

### Methods
1. **initialize_repository(repo_name)**
   - Initializes a new Git repository.
   - **Parameters**: 
     - `repo_name`: The name of the repository to create.
   - **Returns**: `True` if successful, `False` if the repository exists or an error occurs.

2. **add_file(repo_name, file_name)**
   - Adds a specified file to the Git repository.
   - **Parameters**:
     - `repo_name`: The repository name.
     - `file_name`: The file to be added.
   - **Returns**: Status of file addition.

## Testing
### Test Suite
Unit tests are provided to validate the functionality of the `GitOperations` class. The tests cover both normal and exceptional scenarios.

### Test Cases
1. **test_initialize_repository**
   - Verifies the successful initialization of a Git repository.

2. **test_initialize_existing_repository**
   - Ensures that attempting to initialize an existing repository returns `False`.

3. **test_add_file_to_repository**
   - Tests the addition of a file to a repository.

## How to Run Tests
To execute the tests, run:
```bash
python -m unittest discover -s tests
```

## Conclusion
This project provides foundational Git operations in Python, supported by unit tests to ensure reliability.