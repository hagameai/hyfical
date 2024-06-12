# Project Documentation

## Overview

This project implements basic Git operations, including repository initialization, file addition, and committing changes. It serves as a practical guide for users to understand essential Git functionalities.

## File Structure

```
- git_operations.py       # Implements Git operations
- test_git_operations.py   # Unit tests for Git operations
- README.md                # Project description and usage
```

## Git Operations

### `git_operations.py`

This file contains the `GitOperations` class, which encapsulates methods for performing basic Git tasks.

#### Methods

- `initialize_repository(repo_name: str) -> bool`
  - Initializes a new Git repository.
  - Returns `True` if successful, `False` if the repository already exists.

### Example Usage

```python
from git_operations import GitOperations

GitOperations.initialize_repository('my_new_repo')
```

## Testing

### `test_git_operations.py`

Unit tests are provided to ensure the functionality of the Git operations.

#### Test Cases

- `test_initialize_repository`
  - Tests successful initialization of a new Git repository.
  
- `test_initialize_existing_repository`
  - Tests the behavior when attempting to initialize an existing repository.

### Running Tests

Execute the following command to run tests:

```bash
python -m unittest discover
```

## Contributing

Contributions are welcome. Please submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for details.