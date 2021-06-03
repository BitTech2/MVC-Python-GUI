from tkinter import *

import Controller
import Model
import View

fenster = Tk()
Booksmodel = Model.Model("Kopiebooks.db", "Books")
warenkorbModel = Model.Model("Kopiebooks.db", "Warenkorb")
view = View.View(fenster)
controller = Controller.Controller(Booksmodel, warenkorbModel, view)
fenster.mainloop()