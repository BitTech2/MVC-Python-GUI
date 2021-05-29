import sqlite3

class Model:

    def __init__(self):
        self.con = sqlite3.connect("Kopiebooks.db")
        self.cur = self.con.cursor()

    def getData(self):
        self.cur.execute("Select * from Books")
        ergebnis = self.cur.fetchall()
        return ergebnis

    def addEintrag(self, title, author):
        self.values = (str(title), str(author), )
        self.cur.execute("Insert into Books (title, author) values (?, ?)", self.values) #Insert into Books (title, author) values ("Hallo", "Welt")
        self.con.commit()

    def updateEintrag(self, id, title, author):
        self.values = (str(title), str(author), int(id))
        self.cur.execute("Update Books set title = ?, author = ? WHERE id =?", self.values)
        self.con.commit()

    def deleteEintrag(self, id):
        self.values = (int(id),)
        self.cur.execute("Delete From Books Where id = ?", self.values)
        self.con.commit()