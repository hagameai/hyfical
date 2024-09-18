# Project Documentation

## Overview
This project contains a Python package for basic Git operations, encapsulated in the `GitOperations` class. The package allows users to initialize repositories and manage files within them.

## File Structure
```
.
├── git_operations.py          # Contains GitOperations class
├── tests/                     # Directory for unit tests
│   ├── test_git_operations.py # Unit tests for GitOperations
│   └── ...
└── ...
```

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters**: 
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: True if the repository was initialized successfully, False otherwise.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters**: 
  - `repo_name` (str): The repository to which the file will be added.
  - `file_name` (str): The name of the file to be added.
- **Returns**: 
  - `bool`: True if the file was added successfully, False otherwise.

## Testing
The project includes unit tests for the `GitOperations` class, ensuring the functionality of the Git operations.

### Running Tests
Use the following command to run the tests:
```bash
python -m unittest discover -s tests
```

### Test Cases
- **test_initialize_repository**: Tests the successful creation of a new Git repository.
- **test_initialize_existing_repository**: Validates behavior when attempting to initialize an existing repository.

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request for any features or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.