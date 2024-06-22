# Git Operations Documentation

## Overview
This project provides a set of basic Git operations encapsulated in the `GitOperations` class. The functionality includes initializing a repository, adding files, and committing changes.

## File Structure
- **Total Files**: 18
- **Total Lines**: 1019
- **File Types**: 
  - Python Files: 9 (`.py`)
  - Markdown Files: 9 (`.md`)

## Main Components

### `git_operations.py`
This file contains the `GitOperations` class, which provides methods for basic Git operations. 

#### Methods
1. **initialize_repository(repo_name)**
   - Initializes a new Git repository.
   - **Parameters**: 
     - `repo_name`: Name of the repository to create.
   - **Returns**: `True` if successful, `False` if the repository already exists.

2. **add_file(repo_name, file_name)**
   - Adds a file to the specified repository.
   - **Parameters**: 
     - `repo_name`: Name of the repository.
     - `file_name`: Name of the file to be added.

## Testing
The project includes unit tests to validate the functionality of the `GitOperations` class.

### Test Files
- **Test Suite**: `test_git_operations.py`
- **Framework**: `unittest`
- **Key Tests**:
  - Test successful repository initialization.
  - Test handling of existing repositories.

## Usage
To use the `GitOperations` class, import it and call the methods as needed. Ensure Git is installed and accessible in the environment.

```python
from git_operations import GitOperations

# Example usage
GitOperations.initialize_repository("my_repo")
``` 

## Contributing
Please feel free to contribute by submitting pull requests or raising issues for improvements.