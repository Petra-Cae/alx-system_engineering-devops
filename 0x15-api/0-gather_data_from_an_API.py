#!/usr/bin/python3
"""
Returns info about an employee's TODO list
progress using his/her employee ID
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    user = get("https://jsonplaceholder.typicode.com/users/{}"
               .format(userId))
    name = user.json().get('name')
    totalTodos = get('https://jsonplaceholder.typicode.com/todos')
    allTasks = 0
    tasksDone = 0

    for task in totalTodos.json():
        if task.get('userId') == int(userId):
            allTasks += 1
            if task.get('completed'):
                tasksDone += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, tasksDone, allTasks))

    print('\n'.join(["\t " + task.get('title') for task in totalTodos.json()
          if task.get('userId') == int(userId) and task.get('tasksDone')]))
