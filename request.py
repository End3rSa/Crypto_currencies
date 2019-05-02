import requests
import json
from datetime import datetime
from tables import create_connection, execute_query

from coin import *
from platforms import *
from prices import *


def addExtraction(response):
    date = datetime.now()
    status = response.status_code
    query = '''INSERT INTO Extractions (date,status) VALUES (?,?)'''
    conn = sqlite3.connect("DBProject.sql")
    c = conn.cursor()
    c.execute(query,(date, status))
    conn.commit()
    return c.lastrowid
    
def getDataCoins():
    request_tickers = "https://api.coinpaprika.com/v1/tickers"
    response = requests.get(request_tickers)
    lastExtractId = addExtraction(response)
    return (response,lastExtractId)

def insertCoins(response, lastExtractId):
    if response.status_code: # Data successfully retrieved 
        conn = sqlite3.connect("DBProject.sql")
        cursor = conn.cursor()
        sql = '''DELETE FROM Coins'''
        cursor.execute(sql)
        conn.commit()

        coinList = []
        coinListValues = []
        coinsData = response.json()
        #for i in range(len(coinsData)):
        for i in range(300):
            coinData = coinsData[i]
            c = Coin(coinData["symbol"], coinData["name"], coinData["id"], lastExtractId)
            coinList.append(c)
            coinListValues.append(c.values)

        query = '''INSERT INTO Coins (ticker_id, name, coin_id, extract_id ) VALUES (?,?,?,?)'''
        cursor.executemany(query,coinListValues)
        conn.commit()
        return coinList

def getDataPlatforms():
    request_tickers = "https://api.coinpaprika.com/v1/exchanges"
    response = requests.get(request_tickers)
    lastExtractId = addExtraction(response)
    return (response,lastExtractId)

def insertPlatforms(response, lastExtractId):
    if response.status_code: # Data successfully retrieved 
        conn = sqlite3.connect("DBProject.sql")
        cursor = conn.cursor()
        sql = '''DELETE FROM Platforms'''
        cursor.execute(sql)
        conn.commit()

        platformList = []
        platformListValues = []
        platformsData = response.json()
        for i in range(len(platformsData)):
            platformData = platformsData[i]
            p = Platform(platformData["name"], platformData["currencies"], lastExtractId)
            platformList.append(p)
            platformListValues.append(p.values)

        query = '''INSERT INTO Platforms (name, nb_crypto_currencies, extract_id ) VALUES (?,?,?)'''
        cursor.executemany(query,platformListValues)
        conn.commit()
        

def getDataPrices(coinList):
    conn = sqlite3.connect("DBProject.sql")
    cursor = conn.cursor()
    sql = '''DELETE FROM Prices_platforms_coins'''
    cursor.execute(sql)
    conn.commit()

    priceListValues = []
    for coin in coinList:
        request_tickers = "https://api.coinpaprika.com/v1/coins/"+coin.coinId +"/markets"
        response = requests.get(request_tickers)
        lastExtractId = addExtraction(response)
        insertPrices(response, priceListValues, lastExtractId, coin.tickerId)
    
    query = '''INSERT INTO Prices_platforms_coins(price, date, platform_id, extract_id, ticker_id ) VALUES (?,?,?,?,?)'''
    cursor.executemany(query,priceListValues)
    conn.commit()
        

def getPlatformId(platformName, conn, cursor):
    sql = "SELECT platform_id FROM Platforms WHERE name LIKE \"" + platformName +"\""
    cursor.execute(sql)
    platformId = cursor.fetchall() # Retrieve the data returned by the SELECT (from the db)
    return platformId[0][0] #Because we have something like : [(414,415,417)] after cursor.fetchall() 

def insertPrices(response, priceListValues, lastExtractId, tickerId):
    if response.status_code: # Data successfully retrieved 
        conn = sqlite3.connect("DBProject.sql")
        cursor = conn.cursor()

        priceList = []
        #priceListValues = []
        pricesData = response.json()
        print(len(pricesData))
        for i in range(len(pricesData)):
            priceData = pricesData[i]
            platformId = getPlatformId(priceData["exchange_name"], conn, cursor)
            pr = Price(priceData["quotes"]["USD"]["price"] , priceData["last_updated"], platformId, lastExtractId, tickerId)
            priceList.append(pr)
            priceListValues.append(pr.values)

        


response, lastExtractId = getDataCoins()
coinList = insertCoins(response, lastExtractId)

response, lastExtractId = getDataPlatforms()
insertPlatforms(response, lastExtractId)

getDataPrices(coinList)




   

   
