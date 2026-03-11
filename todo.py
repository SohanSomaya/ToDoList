
from storage import load_tasks, save_tasks

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet")
        return
    for task in tasks:
        status = "Completed" if task["done"] else "Pending"
        print(f"[{status}] {task['id']}.{task['title']}")

def add_task(tasks, title):
    new_id = max((t["id"] for t in tasks), default = 0) + 1
    tasks.append({"id":new_id, "title":title, "done":False})
    save_tasks(tasks)

def complete_tasks(tasks, task_id):
    for task in tasks:
        if task["id"] == task.id:
            task["done"] = True
            save_tasks(tasks)
            return
    print("Task not found")

def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task.id:
            tasks.remove(task)
            save_tasks(task)
            return
    print("Task not found")

def main():
    tasks = load_tasks()
    while True:
        user_input - input("\n> ").strip()
        parts = user_input.split(" ", 1)
        command = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""
        if command == "list":
            list_tasks(tasks)
        elif command == "add":
            add_tasks(tasks, arg)
        elif command == "complete"|"finish":
            complete_tasks(tasks, int(arg))
        elif command == "delete"|"remove":
            delete_task(tasks, int(arg))
        elif command == "quit"|"exit":
            break
            
if __name__ == "__main__":
    main()
