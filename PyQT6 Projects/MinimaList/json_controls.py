import json
import os
from datetime import datetime

JSON_FILE = "mini_list_database.json"

def init_db():
	''' Create an empty list of JSON file is empty '''
	if not os.path.exists(JSON_FILE):
		with open(JSON_FILE, "w") as f:
			json.dump([], f)

def get_tasks():
	''' return the list of task dictionaries in the database'''

	init_db()

	with open(JSON_FILE, "r") as f:
		return json.load(f)

def add_task(task_name):
	''' adds a task dictionary in the database '''

	tasks_lis = get_tasks()

	if tasks_lis:
		new_idx = tasks_lis[-1]['idx'] + 1
	else:
		new_idx = 1

	if "!" in task_name:
		# if there are explicit due dates
		title, due = task_name.split("!")
		due = format_date(due.strip())
		new_task = {'idx' : new_idx, 'task' : title, 'due' : due, 'is_complete' : False}

	else:
		new_task = {'idx' : new_idx, 'task' : task_name, 'due' : "", 'is_complete' : False}

	tasks_lis.append(new_task)

	with open(JSON_FILE, "w") as f:
		json.dump(tasks_lis, f, indent = 4)

	print(f"Task added : {task_name}")

def delete_task(task_idx):
	''' delete a task of a certain idx'''
	tasks_lis = get_tasks()

	new_tasks_lis = [task_dic for task_dic in tasks_lis if task_dic["idx"] != task_idx]

	with open(JSON_FILE, "w") as f:
		json.dump(new_tasks_lis, f, indent = 4)

	print(f"Task idx deleted : {task_idx}")



def format_date(date_inpt):
	formats = [
		"%m/%d/%Y",
		"%d/%m/%Y",
		"%m-%d-%Y",
		"%d-%m-%Y",
		"%Y/%m/%d",
		"%Y-%m-%d"	
	]
	for fmt in formats:
		try:
			date = datetime.strptime(date_inpt, fmt)
			return date.strftime("%b %d, %Y")
		except (ValueError, TypeError):
			pass

	return ""



#print(format_date("02-03-2026"))