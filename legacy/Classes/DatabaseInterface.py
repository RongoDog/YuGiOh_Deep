import sqlite3
from sqlite3 import Error

class Card(object):

    ID = 0
    NAME = 1
    DESCRIPTION = 2
    TYPE = 3
    ATK = 4
    DEF = 5
    LEVEL = 6
    RACE = 7
    ATTRIBUTE = 8

class DatabaseInterface(object):

    def __init__(self, file_path):
        try:
            self.conn = sqlite3.connect(file_path)
        except Error as e:
            print(e)

    def fetchCard(self, cardId):
        cur = self.conn.cursor()
        try:
            cur.execute('SELECT texts.id, texts.name, texts.desc, datas.type, datas.atk, datas.def, datas.level,'
                        ' datas.race, datas.attribute FROM texts '
                        'JOIN datas ON texts.id = datas.id '
                        'WHERE datas.id=%d' % int(cardId))
        except Error as e:
            print(e)
            return

        rows = cur.fetchall()
        if not rows:
            print "Rows are empty, dumping deck"
            return None

        return rows[0]

    def fetchAllCards(self):
        cur = self.conn.cursor()
        cur.execute('SELECT texts.id, texts.name, texts.desc, datas.type, datas.atk, datas.def, datas.level,'
                    ' datas.race, datas.attribute FROM texts '
                    'JOIN datas ON texts.id = datas.id')

        return cur.fetchall()


