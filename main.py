todos = [
    {
        "id":1,
        "title": "Learn python",
        "completed": False
    }
]

title = input("What do you want to do? ")

new_todo = {
    "id":2,
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