"""
TODO
Quand tache est crée : 
- Description de la tache = variable task
- Id incrémental (si id existe alors +1)
- status auto sur todo
- createdAt = date de création
- updatedAt = dernière fois que le task a été toucher"""


import cmd
import json
import os
from datetime import datetime

path = r'C:\Nicolas\dev\python\task tracker\tasksData.json' #Replace with your json file path

class taskTracker(cmd.Cmd):
    prompt = 'task-cli >> '
    intro = 'Welcome to the Task Tracker! Type help to list commands.\n'

    def __init__(self):
        super().__init__()
        emptyJson = {} #Empty JSON object 
        emptyJson = json.dumps(emptyJson, indent=4)
        if os.path.exists(path):
            #print('File already exist.')
            return 
        else:
            with open(path, 'w') as file:
                file.write(emptyJson)
            #print('File created successfully.')

    def do_add(self, task):
        """Add a new task"""

        id = 0
        description = task
        status = 'todo'
        createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updatedAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

        if task:
            with open(path, 'r+') as file:
                data = json.load(file)
                if len(data) == 0:
                    id = 1
                else:
                    id = max([int(k) for k in data.keys()]) + 1
                data[id] = {
                    'description': description,
                    'status': status,
                    'createdAt': createdAt,
                    'updatedAt': updatedAt
                }
                file.seek(0)
                json.dump(data, file, indent=4)
                print(f'Task added with ID: {id}')
        else:
            print('Please provide a task to add.')
        return 

    def do_delete(self, taskId):
        """Delete an existing task"""

        if taskId:
            with open(path, 'r+') as file:
                data = json.load(file)
                if taskId in data:
                    del data[taskId]
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                    print(f'Task with ID {taskId} deleted successfully.')
                else:
                    print(f'Task with ID {taskId} not found.')
            return
        else:
            print('Please provide a task ID to delete.')
            return
    
    def do_update(self, line):
        """Update an existing task"""
        return

    def do_exit(self, line):
        """Exit the application"""
        print('Goodbye!')
        return True

if __name__ == '__main__':
    taskTracker().cmdloop()