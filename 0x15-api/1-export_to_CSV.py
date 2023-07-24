#!/usr/bin/python3
"""
Extends 0-*.py to export data in the CSV format
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    name = user.json().get('username')
    totalTodos = requests.get('https://jsonplaceholder.typicode.com/todos')

    userData = userId + '.csv'
    with open(userData, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in totalTodos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, name, str(task.get('completed')),
                                 task.get('title')])
