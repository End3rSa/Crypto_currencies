import sqlite3

class Coin:
    def __init__(self, tickerId, name, coinId, extractId):
        self.tickerId = tickerId
        self.name = name
        self.coinId = coinId
        self.extractId = extractId
        self.values =  (self.tickerId, self.name,self.coinId, self.extractId)

        
    
        


