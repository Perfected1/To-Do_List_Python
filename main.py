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

print(title)