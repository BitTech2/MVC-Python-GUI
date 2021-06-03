import sqlite3

class Model:

    def __init__(self, db, dbTabelle):#db:Kopiebooks.db dbTabelle:Warenkorb
        self.db = db #Kopiebooks.db
        self.dbTabelle = dbTabelle #Warenkorb
        self.con = sqlite3.connect(self.db)#Kopiebooks.db
        self.cur = self.con.cursor()

    def getData(self):
        self.cur.execute("Select * from "+self.dbTabelle)#Warenkorb
        ergebnis = self.cur.fetchall()
        return ergebnis

    def addEintrag(self, title, author):
        self.values = (str(title), str(author), )
        self.cur.execute("Insert into "+self.dbTabelle+" (title, author) values (?, ?)", self.values) #Insert into Warenkorb (title, author) values ("Hallo", "Welt")
        self.con.commit()

    def updateEintrag(self, id, title, author):
        self.values = (str(title), str(author), int(id))
        self.cur.execute("Update "+self.dbTabelle+" set title = ?, author = ? WHERE id =?", self.values)
        self.con.commit()

    def deleteEintrag(self, id):
        self.values = (int(id),)
        self.cur.execute("Delete From "+self.dbTabelle+" Where id = ?", self.values)
        self.con.commit()

    def search(self, searchString):
        self.values = (("%"+searchString+"%"), ("%"+searchString+"%"))
        self.cur.execute("Select * from "+self.dbTabelle+" Where title LIKE ? or author = ?", self.values)
        getfilterenDaten = self.cur.fetchall()
        return getfilterenDaten
