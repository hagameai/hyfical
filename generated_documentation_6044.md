# Project Documentation

## Overview
This project provides a Python class, `GitOperations`, which encapsulates basic Git functionalities, including repository initialization and file management.

## File Structure
```
.
├── git_operations.py               # Main Git operations class
├── tests/                           # Directory containing unit tests
│   ├── test_git_operations.py       # Unit tests for GitOperations
│   └── ...                          # Additional test files
└── README.md                        # Project documentation
```

## GitOperations Class

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository in the specified directory.

- **Parameters:**
  - `repo_name` (str): Name of the repository to be created.
  
- **Returns:**
  - `bool`: True if the repository was successfully initialized, False otherwise.

#### `add_file(repo_name, file_name)`
Adds a file to the specified Git repository.

- **Parameters:**
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to add.

## Testing

### Unit Tests
The project includes unit tests for the `GitOperations` class using the `unittest` framework. Tests cover repository initialization and handling of existing repositories.

### Running Tests
To run the tests, execute the following command in the terminal:
```bash
python -m unittest discover -s tests
```

## Contributing
Contributions are welcome! Please create a fork of the repository and submit a pull request for any enhancements or bug fixes. 

## License
This project is licensed under the MIT License. See the LICENSE file for details.