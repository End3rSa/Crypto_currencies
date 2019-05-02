import sqlite3

class Coin:
    def __init__(self, platformId, name, nbrcryptoCurrencies, extractId):
        self.platformId = platformId
        self.name = name
        self.nbcryptoCurrencies = nbrcryptoCurrencies
        self.extractId = extractId

    def insertIntoDb(self):
        query = '''INSERT INTO Platforms (platform_id, name, nb_crypto_currencies, extract_id ) VALUES (?,?,?,?)'''
        values = (self.platformId, self.name, self.nbcryptoCurrencies, self.extractId)

        conn = sqlite3.connect("DBProject.sql")
        c = conn.cursor()
        c.execute(query,values)
        conn.commit()
