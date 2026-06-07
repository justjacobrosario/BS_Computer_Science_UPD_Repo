from model import Model
from view import View
from controller import Controller

width = 250
height = 250

model = Model(width, height)  # logic
view = View()  # what the user sees
controller = Controller(model, view)  # glues model & view

controller.start_game()
