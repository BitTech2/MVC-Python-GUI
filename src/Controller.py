class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.loadDbDataToListbox()
        self.view.listbox.bind("<<ListboxSelect>>", self.loadLbxDataToEntry)
        self.view.addButton["command"] = self.addData
        self.view.updateButton["command"] = self.updateData
        self.view.deleteButton["command"] = self.deleteData

    def loadDbDataToListbox(self):
        datenbankdaten = self.model.getData()
        self.view.setListbox(datenbankdaten)

    def loadLbxDataToEntry(self, event):
        title = self.view.getListboxTitle()
        author = self.view.getListboxAuthor()
        self.view.setTitle(title)
        self.view.setAuthor(author)

    def addData(self):
        title = self.view.getTitle()
        author = self.view.getAuthor()
        self.model.addEintrag(title, author)
        self.loadDbDataToListbox()

    def updateData(self):
        title = self.view.getTitle()
        author = self.view.getAuthor()
        id = self.view.getListboxId()
        self.model.updateEintrag(id, title, author)
        self.loadDbDataToListbox()

    def deleteData(self):
        id = self.view.getListboxId()
        self.model.deleteEintrag(id)
        self.loadDbDataToListbox()