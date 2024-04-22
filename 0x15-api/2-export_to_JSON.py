#!/usr/bin/python3
"""Exports user data in the JSON format"""

import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todo_user = {}
    task_list = []

    for task in todos:
        if task.get('userId') == int(user_id):
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.json().get('username')
            }
            task_list.append(task_dict)
    todo_user[user_id] = task_list

    filename = user_id + '.json'
    with open(filename, mode='w') as f:
        json.dump(todo_user, f)

# Newline character added here
