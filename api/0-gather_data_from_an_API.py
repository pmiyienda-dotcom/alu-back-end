#!/usr/bin/python3
"""Script that returns TODO list progress for a given employee ID.

This script uses the REST API to fetch employee information
and their TODO list, then displays the progress.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    ).json()
    employee_name = user.get("name")
    total = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    done = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done, total))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))