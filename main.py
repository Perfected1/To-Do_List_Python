todos = [
    {
        "id":1,
        "title": "Learn python",
        "completed": False
    },
    {
        "id":2,
        "title": "Visit Uyo",
        "completed": True
    }
]


# Add Task

title = input("What do you want to do? ")

new_todo = {
    "id":3,
    "title": title,
    "completed": False
}
todos.append(new_todo)

for todo in todos:
    if todo["completed"]:
        status = "Done"
    else:
        status = "Not Done"
    print(todo["id"], todo["title"], "-", status)


# Mark Task

found = False

todo_id = int(input("Enter ID of Completed Task: "))

for todo in todos:

    if todo["id"] == todo_id:

        todo["completed"] = True
        found = True

if not found:
        print("Task not Available!")

# print(todo["id"], todo["title"], "-", status)


# Edit Existing Task
found = False

todo_id = int(input("Enter ID of Task to be Edited: "))
for todo in todos:
    if todo["id"] == todo_id:
            
        new_title = input("Enter New Title: ")
        todo["title"] = new_title
        found = True
        print("Task updated successfully!")
if not found:
    print("Task not Available!")
