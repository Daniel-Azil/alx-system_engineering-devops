#!/usr/bin/python3
"""
    A Python script that, using this REST API, for a given employee ID, returns
    information about his/her TODO list progress.
"""
import requests
from sys import argv


def view_progress():
    """
        A function that, using this REST API, for a given employee ID, returns
    """
    users_json = requests.get("http://jsonplaceholder.typicode.com/users")
    for user_info in users_json.json():
        if user_info.get('id') == int(argv[1]):
            EMPLOYEE_NAME = user_info.get('name')
            break
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    user_task_json = requests.get("http://jsonplaceholder.typicode.com/todos")
    for user_info in user_task_json.json():
        if user_info.get("userId") == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if user_info.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(user_info.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for titles in TASK_TITLE:
        print("\t {}".format(titles))


if __name__ == "__main__":
    view_progress()
