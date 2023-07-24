#!/usr/bin/python3
"""
Extends 0*.py to export employee data in JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    totalTodos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTodos = totalTodos.json()
    employee = {}
    totTasks = []

    for task in totalTodos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            totTasks.append(taskDict)

    employee[userId] = totTasks
    userJn = userId + '.json'
    with open(userJn, mode='w') as f:
        json.dump(employee, f)
