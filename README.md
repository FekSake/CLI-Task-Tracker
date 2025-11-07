# CLI Task Tracker

A simple command-line task management application built in Python. Track your tasks, mark their progress, and stay organized without any external dependencies.

## Features

- Add, update, and delete tasks
- Mark tasks as in-progress or done
- List all tasks or filter by status
- Persistent storage using JSON
- Clean, intuitive command-line interface
- Error handling and validation

## Installation

No installation required! Just ensure you have Python 3.6+ installed on your system.

## Usage

Run the application using Python:

```bash
python main.py <command> [arguments]
```

### Available Commands

#### Adding Tasks
```bash
python main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

python main.py add "Complete project documentation"
# Output: Task added successfully (ID: 2)
```

#### Updating Tasks
```bash
python main.py update 1 "Buy groceries and cook dinner"
# Output: Task 1 updated successfully.
```

#### Deleting Tasks
```bash
python main.py delete 1
# Output: Task 1 deleted successfully.
```

#### Marking Task Status
```bash
# Mark as in progress
python main.py mark-in-progress 2
# Output: Task 2 marked as in-progress.

# Mark as done
python main.py mark-done 2
# Output: Task 2 marked as done.
```

#### Listing Tasks
```bash
# List all tasks
python main.py list

# List only todo tasks
python main.py list todo

# List only in-progress tasks
python main.py list in-progress

# List only completed tasks
python main.py list done
```

### Task Properties

Each task contains the following information:

- **id**: Unique identifier (auto-generated)
- **description**: Task description
- **status**: Current status (`todo`, `in-progress`, `done`)
- **createdAt**: Creation timestamp (ISO format)
- **updatedAt**: Last modification timestamp (ISO format)

### Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the script. The file is created automatically if it doesn't exist.

Example JSON structure:
```json
{
  "1": {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2024-01-15T10:30:00.123456",
    "updatedAt": "2024-01-15T10:30:00.123456"
  }
}
```

## Error Handling

The application handles common errors gracefully:

- Missing arguments
- Invalid task IDs
- Invalid status values
- File system errors
- JSON parsing errors

## Examples

Here's a complete workflow example:

```bash
# Add some tasks
python main.py add "Write project proposal"
python main.py add "Review code changes"
python main.py add "Update documentation"

# Start working on a task
python main.py mark-in-progress 1

# Complete a task
python main.py mark-done 2

# Update a task description
python main.py update 3 "Update documentation and README"

# List all tasks to see current status
python main.py list

# List only pending tasks
python main.py list todo
```

## Requirements

- Python 3.6 or higher
- No external dependencies required
- Works on Windows, macOS, and Linux