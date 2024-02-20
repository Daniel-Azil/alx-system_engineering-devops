#!/usr/bin/python3
"""
A module that requests from API; Return TODO list and
    export this content to JSON.
"""
import json
import requests


def export_data_to_json():
    """A function that returns API content"""
    USERS = []
    user_info = requests.get("http://jsonplaceholder.typicode.com/users")
    for info1 in user_info.json():
        USERS.append((info1.get('id'), info1.get('username')))
    TASK_STATUS_TITLE = []
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos")
    for info2 in tasks.json():
        TASK_STATUS_TITLE.append((info2.get('userId'),
                                  info2.get('completed'),
                                  info2.get('title')))

    """exporting to json"""
    content = dict()
    for info1 in USERS:
        info2 = []
        for objct in TASK_STATUS_TITLE:
            if objct[0] == info1[0]:
                info2.append({"objct": objct[2], "completed": objct[1],
                              "username": info1[1]})
        content[str(info1[0])] = info2
    name_of_file = "todo_all_employees.json"
    with open(name_of_file, "w") as f:
        json.dump(content, f, sort_keys=True)


if __name__ == "__main__":
    export_data_to_json()
