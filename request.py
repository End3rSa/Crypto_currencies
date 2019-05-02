import requests
import json
from coin import *
from datetime import datetime
from tables import create_connection, execute_query
from platforms import *


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
        coinList = []
        coinsData = response.json()
        for i in range(len(coinsData)):
            coinData = coinsData[i]
            c = Coin(coinData["symbol"], coinData["name"], coinData["id"], lastExtractId)
            coinList.append(c)

        for i in range(300): #for coin in coinList:
            #coin.insertIntoDb()
            coinList[i].insertIntoDb()

def getDataPlatforms():
    request_tickers = "https://api.coinpaprika.com/v1/exchanges"
    response = requests.get(request_tickers)
    lastExtractId = addExtraction(response)
    return (response,lastExtractId)

def insertPlatforms(response, lastExtractId):
    if response.status_code: # Data successfully retrieved 
        platformList = []
        platformsData = response.json()
        for i in range(len(platformsData)):
            platformData = platformsData[i]
            p = Platforms(platformData["symbol"], platformData["name"], platformData["id"], lastExtractId)
            platformList.append(p)
           #"url"+ c.coinId+"url" -> pour les prix, faire une boucle sur coin et modifier l'URL

        for platform in platformList:
            platform.insertIntoDb()
        



response, lastExtractId = getDataCoins()
insertCoins(response, lastExtractId)

response, lastExtractId = getDataPlatforms()
insertPlatforms(response, lastExtractId)



   

   
