class Controller:

    def __init__(self, model, warenkorbModel,view):
        self.view = view
        self.model = model
        self.warenkorbModel = warenkorbModel
        self.loadDbDataToListbox()
        self.loadWarenkorbListbox()
        self.view.listbox.bind("<<ListboxSelect>>", self.loadLbxDataToEntry)
        self.view.addButton["command"] = self.addData
        self.view.updateButton["command"] = self.updateData
        self.view.deleteButton["command"] = self.deleteData
        self.view.warenkorbAddButton["command"] = self.addWarenkorbData
        self.view.warenkorbDelButton["command"] = self.deleteWarenkorbData
        self.view.booksSearchEntry.bind("<Return>", self.searchBooks)
        self.view.warenkorbSearchEntry.bind("<Return>", self.searchWarenkorb)

    def searchWarenkorb(self, event):
        datenAusDemWarenkorbEingabeld = self.view.getWarenkorbSearchEntry()
        gefiltereWarenkorbBuecher = self.warenkorbModel.search(datenAusDemWarenkorbEingabeld)
        self.view.setWarenkorbListbox(gefiltereWarenkorbBuecher)

    def searchBooks(self, event):
        datenAusDemBooksEingagefeld = self.view.getBooksSearchEntry()
        gefiltereBooks = self.model.search(datenAusDemBooksEingagefeld)
        self.view.setListbox(gefiltereBooks)

    def deleteWarenkorbData(self):
        id = self.view.getWarenkorbListboxId()
        self.warenkorbModel.deleteEintrag(id)
        self.loadWarenkorbListbox()

    def addWarenkorbData(self):
        title = self.view.getListboxTitle()
        author = self.view.getListboxAuthor()
        self.warenkorbModel.addEintrag(title, author)
        self.loadWarenkorbListbox()

    def loadWarenkorbListbox(self):
        warenkorbTabellenDaten = self.warenkorbModel.getData()
        self.view.setWarenkorbListbox(warenkorbTabellenDaten)

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