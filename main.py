import sys
import json
import datetime
import os

class TaskHandler:
    def __init__(self):
        self.filename = "tasks.json"
        try:
            self.tasks = self.load()
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = {}
            self.save()
        
    def load(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def get_next_id(self):
        if not self.tasks:
            return "1"
        return str(max(int(task_id) for task_id in self.tasks.keys()) + 1)

    def add(self, task_desc):
        task_id = self.get_next_id()
        timestamp = datetime.datetime.now().isoformat()
        
        self.tasks[task_id] = {
            "id": int(task_id),
            "description": task_desc,
            "status": "todo",
            "createdAt": timestamp,
            "updatedAt": timestamp
        }
        self.save()
        print(f"Task added successfully (ID: {task_id})")

    def delete(self, task_id):
        if task_id not in self.tasks:
            print("Task doesn't exist.")
            return
        
        del self.tasks[task_id]
        self.save()
        print(f"Task {task_id} deleted successfully.")

    def update(self, task_id, task_desc):
        if task_id not in self.tasks:
            print("Task doesn't exist.")
            return
        
        self.tasks[task_id]['description'] = task_desc
        self.tasks[task_id]["updatedAt"] = datetime.datetime.now().isoformat()
        self.save()
        print(f"Task {task_id} updated successfully.")

    def mark_status(self, task_id, status):
        if task_id not in self.tasks:
            print("Task doesn't exist.")
            return
        
        self.tasks[task_id]['status'] = status
        self.tasks[task_id]["updatedAt"] = datetime.datetime.now().isoformat()
        self.save()
        print(f"Task {task_id} marked as {status}.")

    def list_tasks(self, status_filter=None):
        if not self.tasks:
            print("No tasks found.")
            return
        
        # Convert legacy numeric status to string status
        status_map = {0: "todo", 1: "in-progress", 2: "done"}
        
        filtered_tasks = self.tasks
        if status_filter:
            filtered_tasks = {}
            for k, v in self.tasks.items():
                task_status = v['status']
                # Handle legacy numeric status
                if isinstance(task_status, int):
                    task_status = status_map.get(task_status, "todo")
                if task_status == status_filter:
                    filtered_tasks[k] = v
        
        if not filtered_tasks:
            status_msg = f" with status '{status_filter}'" if status_filter else ""
            print(f"No tasks found{status_msg}.")
            return
        
        print(f"Tasks{' (' + status_filter + ')' if status_filter else ''}:")
        print("-" * 50)
        
        for task_id, task in sorted(filtered_tasks.items(), key=lambda x: int(x[0])):
            task_status = task['status']
            # Handle legacy numeric status
            if isinstance(task_status, int):
                task_status = status_map.get(task_status, "todo")
            
            status_symbol = {"todo": "[ ]", "in-progress": "[~]", "done": "[✓]"}
            symbol = status_symbol.get(task_status, "[ ]")
            
            print(f"{symbol} {task['id']}. {task['description']}")
            print(f"    Status: {task_status}")
            print(f"    Created: {task['createdAt']}")
            print(f"    Updated: {task['updatedAt']}")
            print()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [arguments]")
        print("\nCommands:")
        print("  add <description>           - Add a new task")
        print("  update <id> <description>   - Update task description")
        print("  delete <id>                 - Delete a task")
        print("  mark-in-progress <id>       - Mark task as in progress")
        print("  mark-done <id>              - Mark task as done")
        print("  list [status]               - List tasks (all, todo, in-progress, done)")
        sys.exit(1)

    tasks = TaskHandler()
    command = sys.argv[1]

    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Task description is required")
                sys.exit(1)
            task_desc = sys.argv[2]
            tasks.add(task_desc)
        
        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Task ID and new description are required")
                sys.exit(1)
            task_id = sys.argv[2]
            task_desc = sys.argv[3]
            tasks.update(task_id, task_desc)

        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                sys.exit(1)
            task_id = sys.argv[2]
            tasks.delete(task_id)

        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                sys.exit(1)
            task_id = sys.argv[2]
            tasks.mark_status(task_id, "in-progress")

        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                sys.exit(1)
            task_id = sys.argv[2]
            tasks.mark_status(task_id, "done")

        elif command == "list":
            status_filter = None
            if len(sys.argv) > 2:
                status_filter = sys.argv[2]
                if status_filter not in ["todo", "in-progress", "done"]:
                    print("Error: Invalid status. Use 'todo', 'in-progress', or 'done'")
                    sys.exit(1)
            tasks.list_tasks(status_filter)

        else:
            print(f"Error: Unknown command '{command}'")
            print("Use 'python main.py' without arguments to see available commands")
            sys.exit(1)

    except IndexError:
        print("Error: Missing required arguments")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()