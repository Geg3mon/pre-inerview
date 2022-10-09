from dataclasses import dataclass
import datetime
import json


@dataclass
class Todo:
    todo: str
    time_finished: str = ''
    todo_file: str = 'task_2/todo.json'
    done_file: str = 'task_2/done.json'

    def load_json(filename):
        """Load json file"""
        with open(filename, 'r') as f:
            json_data: dict = json.load(f)
            return json_data

    def write_to_todo(self, data: dict, json_data: load_json) -> str:
        """Write into todo file"""
        with open(self.todo_file, 'w') as f:
            flag = True
            if self.todo in json_data['tasks']:
                flag = False
            json_data['tasks'].update(data)
            json.dump(json_data, f, indent=4)
            return flag

    def write_to_done(self, data: dict, json_data: load_json) -> str:
        """Write into done file"""
        flag = True
        with open(self.done_file, 'w') as f:
            if self.todo in json_data['tasks']:
                flag = False
            else:
                json_data['count'] += 1
            json_data['tasks'].update(data)
            data_count = {
                str(datetime.date.today()).replace('-', '.'): json_data['count']
            }
            json_data['done'].update(data_count)
            json.dump(json_data, f, indent=4)
        return flag

    def remove_from_todo(self, data: dict, json_data: load_json) -> str:
        """Remove from json file"""
        flag = True
        with open(self.todo_file, 'w') as f:
            remove = json_data['tasks'].pop(data, None)
            json.dump(json_data, f, indent=4)
            if remove == None:
                flag = False
        return flag

    def add_task(self) -> str:
        """Add item to todo list"""
        data = {self.todo: "in progress"}
        json_data = Todo.load_json(self.todo_file)
        response = self.write_to_todo(data, json_data)
        return response

    def add_tasks(*args):
        tasks = args
        for task in tasks:
            task = Todo(task)
            data = {task.todo:"in progress"}
            json_data = Todo.load_json(Todo.todo_file)
            response = Todo.write_to_todo(task, data, json_data)
        return response

    def remove_task(self) -> str:
        """Remove item from todo list"""
        data = self.todo
        json_data = Todo.load_json(self.todo_file)
        response = self.remove_from_todo(data, json_data)
        return response

    def remove_tasks(*args):
        """Remove tasks from todo list"""
        tasks = args
        for task in tasks:
            task = Todo(task)
            data = task.todo
            json_data = Todo.load_json(Todo.todo_file)
            Todo.remove_from_todo(task, data, json_data)
            print(f'Task "{task.todo}" removed')

    def show_todo() -> list:
        """Show todo list"""
        json_data = Todo.load_json(Todo.todo_file)
        values = list(json_data['tasks'].keys())
        if len(values) > 0:
            return print(values)
        else:
            return print('Add your first task')

    def show_done() -> list:
        """Show done list"""
        json_data = Todo.load_json(Todo.done_file)
        values = list(json_data['tasks'].keys())
        if len(values) > 0:
            return print(values)
        else:
            return print('You have not completed any task yet')

    def done_task(self):
        data = self.todo
        json_data = Todo.load_json(self.todo_file)
        r_response = self.remove_from_todo(data, json_data)
        data = {
            self.todo: str(datetime.date.today()).replace('-', '.')
        }
        if r_response:
            json_data = Todo.load_json(self.done_file)
            response = self.write_to_done(data, json_data)
        else:
            response = False
        return response

    def done_tasks(*args):
        r_resonse = []
        tasks = args
        for task in tasks:
            task = Todo(task)
            response = task.done_task()
            if response:
                r_resonse.append('+')
            else:
                r_resonse.append('-')
        return r_resonse
