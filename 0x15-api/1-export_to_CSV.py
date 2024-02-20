#!/usr/bin/python3
"""
    A module that requests from API, returns TODO and exports data to CSV
"""
import csv
import requests
from sys import argv


def export_to_csv():
    """A funtion that returns API data"""
    json_user_info = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in json_user_info.json():
        if u.get('id') == int(argv[1]):
            USERNAME = (u.get('username'))
            break
    TASK_STATUS_TITLE = []
    task = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in task.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """exporting to csv"""
    name_of_file = "{}.csv".format(argv[1])
    with open(name_of_file, "w") as csvfile:
        users_all_info = ["USER_ID", "USERNAME",
                          "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        inputter = csv.DictWriter(csvfile, fieldnames=users_all_info,
                                  quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            inputter.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                               "TASK_COMPLETED_STATUS": task[0],
                               "TASK_TITLE": task[1]})


if __name__ == "__main__":
    export_to_csv()
