tasks = []

def add_task(description, due_date=None):
    task={"id": len(tasks) + 1, "description": description, "due_date": due_date, "complete": False}
    tasks.append(task)
    print(f"task '{description}' added")
    return task

def list_tasks():
    print("\n---Current task---")
    if not tasks:
        print("No task available")
        return
    for task in tasks:
        status = "✓" if task["complete"] else ""
        due = f"(due:{task['due_date']})" if task["due_date"] else ""
        print(f"[{status}]{task['id']}. {task['description']}{due}")
    print("---------")

def mark_task_complete(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["complete"] = True
            print(f"task {task_id} marked as complete")
            return True
    print(f"task {task_id } not found")
    return False

def save_task_to_file(filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(f"{task['id']},{task['description']},{task["due_date"]},{task['complete']}\n")
        print(f"Tasks saved to {filename}")

if __name__ == "__main__":
    add_task("Learn Git", "2024-08-01")
    add_task("Practice OOP", "2024-08-05")
    list_tasks()
    mark_task_complete(1)
    list_tasks()
    save_task_to_file() 