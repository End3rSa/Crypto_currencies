import sqlite3

class Platform:
    def __init__(self, name, nbrcryptoCurrencies, extractId):
        self.name = name
        self.nbcryptoCurrencies = nbrcryptoCurrencies
        self.extractId = extractId
        self.values = (self.name, self.nbcryptoCurrencies, self.extractId)
