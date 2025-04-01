import sys, json, datetime

class TaskHandler():
    def __init__(self) -> None:
        try:
            self.tasks = self.load()
        except:
            self.tasks = {}
            self.save()
        
    def load(self) -> None:
        with open("tasks.json", "r") as f:
            self.tasks = json.load(f)

    def save(self) -> None:
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def add(self, taskDesc):
        id: str = str(int(max("0", *self.tasks.keys())) + 1)
        self.tasks[id] = {
            "id":id,
            "description":taskDesc,
            "status":0,
            "createdAt":datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            "updatedAt":datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        }
        self.save()

    def delete(self, taskID):
        try:
            self.tasks.pop(taskID)
            self.save()
        except KeyError:
            print("Task doesnt exist.")

    def update(self, taskID, taskDesc):
        try:
            self.tasks[taskID]['description'] = taskDesc
            self.tasks[taskID]["updatedAt"] = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            self.save()
        except KeyError:
            print("Task doesnt exist.")

tasks = TaskHandler()


def main():

    if len(sys.argv) <= 1:
        print("Usage: python main.py <operation>")
        sys.exit(1)

    operation = sys.argv[1]

    if operation == "add":
        taskDesc = sys.argv[2]
        tasks.add(taskDesc)
    
    elif operation == "update":
        taskID = sys.argv[2]
        taskDesc = sys.argv[3]
        taskTimeStamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        tasks.update(taskID, taskDesc)

    elif operation == "delete":
        taskID = sys.argv[2]
        tasks.delete(taskID)    




    else:
        print("Usage: python main.py <operation>")

if __name__ == "__main__":
    main()