#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    ).json()

    done_tasks = [task for task in todos if task.get("completed")]
    employee_name = user.get("name")
    total = len(todos)
    done = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({done}/{total}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")