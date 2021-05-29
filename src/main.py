from tkinter import *

import Controller
import Model
import View

fenster = Tk()
model = Model.Model()
view = View.View(fenster)
controller = Controller.Controller(model, view)
fenster.mainloop()