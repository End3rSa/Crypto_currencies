import sqlite3

class Price:
    def __init__(self, price, date, platformId, extractId, tickerId):
        self.price = price
        self.date = date
        self.platformId = platformId
        self.extractId = extractId
        self.tickerId = tickerId
        self.values = (self.price, self.date, self.platformId, self.extractId, self.tickerId) 
