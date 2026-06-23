#!/usr/bin/python3
"""Script that returns TODO list progress for a given employee ID."""
import requests
import sys
if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com"
    employee = requests.get(
        BASE_URL + "/users/{}".format(sys.argv[1])).json()
    EMPLOYEE_NAME = employee.get("name")
    employee_todos = requests.get(
        BASE_URL + "/users/{}/todos".format(sys.argv[1])).json()
    done_tasks = [t for t in employee_todos if t.get("completed")]
    COMPLETED_LEN = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, COMPLETED_LEN, len(employee_todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))