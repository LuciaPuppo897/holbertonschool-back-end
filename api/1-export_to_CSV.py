#!/usr/bin/python3
"""
    task 1 export in CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    """ 
        api function 
    """

api_url = f'https://jsonplaceholder.typicode.com/'

user_id = (argv[1])
user_data = requests.get(api_url + f'users/{user_id}').json()
user_task = requests.get(api_url + f'users/{user_id}/todos').json()
user_completed_task = [task for task in user_task if task['completed']]


with open(user_id, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    for task in user_task:
        writer.writerow([user_id,
                          user_data['username'],
                          task['completed'],
                          task['title'],
                          ])
