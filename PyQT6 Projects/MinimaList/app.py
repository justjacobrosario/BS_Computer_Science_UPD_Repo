import sys
import os
import json
import json_controls
from PyQt6.QtWidgets import QComboBox, QFrame, QApplication, QLabel, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from mini_list_themes import color_themes
from datetime import datetime
from enum import Enum, auto

'''
1. widgets:
 - QLineEdit() as text input box
 	- qlineedit_obj.returnPressed.connect(self.func_name) to call functions when click enter

 - QPushButton() as button
 	- qpushbutton_obj.setStyleSheet({CSS styles})
	- qpushbutton_obj.clicked.connect(self.func_name)

2. CSS classes like property (for qpushbutton or any other widgets)
 - qpushbutton_obj.setObjectName("some_name") is like id="some_name"
 - app.setStyleSheet({
	QPushButton#some_name {...}
 })

 - qpushbutton_obj.setProperty("class", "some_class_name")
 - app.setStyleSheet({
	QPushButton[class="taskItem"] {...}
 })
'''


class Mode(Enum):
	Display_Settings = auto()
	Display_Tasks = auto()

class SortingMethod(Enum):
	By_Due_Date = auto()
	By_Task_Name = auto()
	By_Index = auto()

if getattr(sys, 'frozen', False):
	ICON_PATH = os.path.join(sys._MEIPASS, "mini_list_logo.ico")  # use sys._MEIPASS to get the path of the exe file
else:
	ICON_PATH = "mini_list_logo.ico"

class MyApp(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("MinimaList") # window title
		self.setWindowIcon(QIcon(ICON_PATH))
		self.resize(500, 500) # size ng widget

		# LAYOUT
		main_layout = QVBoxLayout()
		self.setLayout(main_layout)

		# MODES
		self.mode = Mode.Display_Tasks
		self.sort_by = SortingMethod.By_Index # default sorting method

		# INPUT FIELD AND UPDATE BUTTON

		self.inputField = QLineEdit()
		self.inputField.returnPressed.connect(self.update) # call update when typed enter

		button = QPushButton("✎", clicked = self.update_display) # call update_display when clicked

		main_layout.addWidget(self.inputField)
		main_layout.addWidget(button)

		# TASKS WRAPPER
		self.scrollArea = QScrollArea() # wrap the tasks here to make it scrollable
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)

		self.tasks_wrapper = QWidget()
		self.tasks_layout = QVBoxLayout(self.tasks_wrapper) # organize buttons vertically
		self.tasks_layout.setAlignment(Qt.AlignmentFlag.AlignTop) # accumulate tasks from up to down

		self.scrollArea.setWidget(self.tasks_wrapper)
		main_layout.addWidget(self.scrollArea)

		# initialize database if there is no currently existing database
		json_controls.init_db()

		# render tasks initially
		self.display_tasks()



	def change_color_theme(self, theme):
		if theme in color_themes:
			self.setStyleSheet(color_themes[theme])

	def delete_task_from_btn(self, task_idx):
		json_controls.delete_task(task_idx)
		self.display_tasks()

	def display_tasks(self):
		''' display each task as a button'''

		# remove currently displaye buttons
		while self.tasks_layout.count():
			child = self.tasks_layout.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

		tasks_list = json_controls.get_tasks()


		#sorting part
		if self.sort_by == SortingMethod.By_Due_Date:
			tasks_list.sort(key=lambda x: datetime.strptime(x["due"], "%b %d, %Y") if x["due"] else datetime.max)
		elif self.sort_by == SortingMethod.By_Task_Name:
			tasks_list.sort(key=lambda x: x["task"])
		elif self.sort_by == SortingMethod.By_Index:
			tasks_list.sort(key=lambda x: x["idx"])

		for task in tasks_list:
			task_idx = task["idx"]
			task_name = task["task"]
			task_due = task["due"]

			# only present 25 chars for the task title
			btn = QPushButton(f"{task_idx}: {task_name[:25]:^25} | {task_due}")
			btn.setProperty("class", "task_btn")
			btn.clicked.connect(lambda checked, idx = task_idx: self.delete_task_from_btn(idx))
			self.tasks_layout.addWidget(btn)


	def update(self):
		'''update the database or color theme based on the input field'''
		inputted = self.inputField.text().strip()
				
		# check if there is a letter in the text
		letter_exists = False
		for char in inputted:
			if char.isalpha():
				letter_exists = True
				break

		if (not letter_exists): # if the text is purely an int
			try:
				selected_idx = int(inputted)
				json_controls.delete_task(selected_idx)
				self.display_tasks()

			except Exception:

				pass

		elif inputted.startswith("$c"):
			parts = inputted.split(maxsplit=1)
			if len(parts) == 2:
				self.change_color_theme(parts[1])


		elif inputted != "":
			json_controls.add_task(inputted)
			self.display_tasks()

		self.inputField.setText("") # clear up the input field

	def settings(self):
		''' display settings page '''

		#remove currently displayed buttons
		while self.tasks_layout.count():
			child = self.tasks_layout.takeAt(0)
			if child.widget():
				child.widget().deleteLater()
				
		# add sort by text and is adjacent to a dropdown menu to select the sorting method
		sort_label = QLabel("Sort by:")
		self.tasks_layout.addWidget(sort_label)

		sort_dropdown = QComboBox()
		sort_dropdown.addItems(["Index", "Due Date", "Task Name"])

		sort_dropdown.setCurrentIndex(0) # sort by index is default

		# connect the dropdown to a function to update the sorting method
		sort_dropdown.currentTextChanged.connect(self.change_sorting_method)
		self.tasks_layout.addWidget(sort_dropdown)

	def change_sorting_method(self, method):
		if method == "Index":
			self.sort_by = SortingMethod.By_Index
		elif method == "Due Date":
			self.sort_by = SortingMethod.By_Due_Date
		elif method == "Task Name":
			self.sort_by = SortingMethod.By_Task_Name


	def update_display(self):
		''' switch between tasks display and setting display'''
		if self.mode == Mode.Display_Tasks:
			self.mode = Mode.Display_Settings
			self.settings()
		elif self.mode == Mode.Display_Settings:
			self.mode = Mode.Display_Tasks
			self.display_tasks()


'''INSTANTIATIONS'''

# app = QApplication([]) defaul instantiation of the app
# by activating the app in the cmd prompt, we use sys.argv
app = QApplication(sys.argv)
app.setStyleSheet('''
	QWidget {
		background-color : #0C0C0C;
		font-size : 20px;
		font-family : "Cascadia Mono", "Consolas", monospace;
		font-weight : 400;
	}
	QPushButton {
		background-color: #1E1E1E;
	}
	QPushButton[class="task_btn"]{
		text-align: left; padding: 10px;
		background-color: #202020;
		color : white;
	}
	''')


window = MyApp()
window.show()

# to run the app
app.exec()