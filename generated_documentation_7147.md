# Project Documentation

## Overview
This project implements basic Git operations encapsulated within the `GitOperations` class. It provides functionalities such as initializing a repository and adding files.

## File Structure
- **Python Files (`.py`)**: 32
- **Markdown Files (`.md`)**: 22
- **Total Files**: 54
- **Total Lines**: 3216

## Class: `GitOperations`

### Methods

#### `initialize_repository(repo_name)`
Initializes a new Git repository.

- **Parameters**: 
  - `repo_name` (str): Name of the repository to be created.
- **Returns**: 
  - `bool`: True if successful, False otherwise.
- **Raises**: 
  - Exception if an error occurs during initialization.

#### `add_file(repo_name, file_name, content)`
Adds a file to the specified repository.

- **Parameters**:
  - `repo_name` (str): Name of the repository.
  - `file_name` (str): Name of the file to add.
  - `content` (str): Content to write to the file.
- **Returns**: 
  - `bool`: True if the file was added successfully, False otherwise.

## Testing
Unit tests for the `GitOperations` class are provided in separate files. Each test case validates the functionality of the methods.

### Test Cases
- **Test Initialization of Repository**: Validates successful creation of a repository.
- **Test Existing Repository**: Checks behavior when attempting to initialize an existing repository.

### Setup and Teardown
Tests create a temporary directory for isolation and remove it after execution to ensure a clean state.

## Usage
To utilize the `GitOperations` class, import it and call its static methods as needed in your application.