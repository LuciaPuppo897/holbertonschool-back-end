#!/usr/bin/python3
"""
    task 0 api getter
"""
import requests
from sys import argv

if __name__ == '__main__':
    """ api function """

api_url = f'https://jsonplaceholder.typicode.com/'

user_id = int(argv[1])
user_data = requests.get(api_url + f'users/{user_id}').json()
user_task = requests.get(api_url + f'users/{user_id}/todos').json()
user_completed_task = [task for task in user_task if task['completed']]

print(f'Employee{user_data["name"]} is done with', end='')
print(f'task({len(user_completed_task)}/{len(user_task)}):')

for tasks in user_completed_task:
    print("\task" + tasks["title"])
