import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return[]
    with open(FILE, 'r') as f:
        return json.load(f)                 '''json.load converts JSON to python list'''

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=2)       '''json.dump converts python list to JSON'''
