#!/usr/bin/python3
"""
    A module that requests API, returns TODO and export contents to JSON.
"""
from sys import argv
import json
import requests


def export_to_json():
    """return API content"""
    usesrs_info = requests.get("http://jsonplaceholder.typicode.com/users")
    for info in usesrs_info.json():
        if info.get('id') == int(argv[1]):
            USERNAME = (info.get('username'))
            break
    TASK_STATUS_TITLE = []
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos")
    for info_2 in tasks.json():
        if info_2.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((info_2.get('completed'), info_2.get('title')))

    """exporting to json"""
    info_2 = []
    for info3 in TASK_STATUS_TITLE:
        info_2.append({"task": info3[1], "completed": info3[0], "username": USERNAME})
    content = {str(argv[1]): info_2}
    name_of_file = "{}.json".format(argv[1])
    with open(name_of_file, "w") as f:
        json.dump(content, f)


if __name__ == "__main__":
    export_to_json()
