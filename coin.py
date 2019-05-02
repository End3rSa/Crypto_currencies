import sqlite3

class Coin:
    def __init__(self, tickerId, name, coinId, extractId):
        self.tickerId = tickerId
        self.name = name
        self.coinId = coinId
        self.extractId = extractId

    def insertIntoDb(self):
        query = '''INSERT INTO Coins (ticker_id, name, coin_id, extract_id ) VALUES (?,?,?,?)'''
        values = (self.tickerId, self.name,self.coinId, self.extractId)

        conn = sqlite3.connect("DBProject.sql")
        c = conn.cursor()
        c.execute(query,values)
        conn.commit()
        
        
        


