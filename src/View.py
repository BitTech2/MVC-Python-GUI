from tkinter import *

class View:

    def __init__(self, root):
        self.root = root
        self.root.title("Bibliotheks Datenbank")
        self.titleLabel = Label(self.root, text="Title: ")
        self.titleLabel.grid(row=0, column=0, padx=5, pady=5)

        self.entryTitleTextVar = StringVar()
        self.entryTitle = Entry(self.root, textvariable=self.entryTitleTextVar)
        self.entryTitle.grid(row=0, column=1, padx=5, pady=5)

        self.authorLabel = Label(self.root, text="Author: ")
        self.authorLabel.grid(row=1, column=0, padx=5, pady=5)

        self.authorEntryTextVar = StringVar()
        self.authorEntry = Entry(self.root, textvariable=self.authorEntryTextVar)
        self.authorEntry.grid(row=1, column=1, padx=5, pady=5)

        self.addButton = Button(self.root, text="Add")
        self.addButton.grid(row=2, column=0, padx=5, pady=5)

        self.updateButton = Button(self.root, text="Update")
        self.updateButton.grid(row=2, column=1, padx=5, pady=5)

        self.deleteButton = Button(self.root, text="Delete")
        self.deleteButton.grid(row=2, column=2, padx=5, pady=5)

        self.listbox = Listbox(self.root)
        self.listbox.grid(row=3, column=1, padx=5, pady=5)

    def getTitle(self):
        return self.entryTitleTextVar.get()

    def getAuthor(self):
        return self.authorEntryTextVar.get()

    def setTitle(self, title):
        self.entryTitleTextVar.set(title)

    def setAuthor(self, author):
        self.authorEntryTextVar.set(author)

    def getListboxId(self):
        selectedLbData = self.listbox.curselection()
        id = self.listbox.get(selectedLbData)[0]
        return id

    def getListboxTitle(self):
        selectedLbData = self.listbox.curselection()
        title = self.listbox.get(selectedLbData)[1]
        return title

    def getListboxAuthor(self):
        selectedLbData = self.listbox.curselection()
        author = self.listbox.get(selectedLbData)[2]
        return author

    def setListbox(self, datenbankDaten):
        self.listbox.delete(0, END)
        for eintrage in datenbankDaten:
            self.listbox.insert(END, eintrage)