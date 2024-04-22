#!/usr/bin/python3
"""For a given employee ID, returns information about their TODO"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    total_tasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(user_id):
            total_tasks += 1
            if task.get('completed'):
                completed += 1

    print(
        f'Employee {name} is done with tasks ({completed}/{total_tasks}):'
    )

    print(
        '\n'.join(
            ["\t " + task.get('title') for task in todos.json()
             if task.get('userId') == int(user_id) and task.get('completed')]
        )
    )
