#!/usr/bin/python3
"""
Retrieves all employee data in the JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoTotal = {}

    for user in users:
        totTasks = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                totTasks.append(taskDict)
        todoTotal[user.get('id')] = totTasks
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoTotal, f)
