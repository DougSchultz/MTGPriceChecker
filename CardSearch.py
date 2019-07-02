import requests
import json
import matplotlib.pyplot as plt
import sqlite3
from sqlite3 import Error

def getAllCards():
    print('Getting Json...')

    try:
        allCardsJSON = requests.get('https://mtgjson.com/json/AllCards.json')
    except:
        print('There was an error getting json')

    print('Creating Object...')
    
    allCards = allCardsJSON.json()
    allCards = dict((k.lower(),v) for k,v in allCards.items())

    return allCards

def createConnection():
    try:
        conn = sqlite3.connect('AllSets.sqlite')
        return conn
    except Error as e:
        print(e)
    
    return None

def getCardPrice(conn, setName, cardName, priceType):
    cur = conn.cursor()
    cur.execute("SELECT prices FROM sets INNER JOIN cards ON setCode=code WHERE sets.name='{}' and cards.name='{}'".format(setName,cardName))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    # if cardName not in cardDict:
    #     print('Card Name Not Found')
    #     return False

    # if 'prices' in cardDict[cardName]:
    #     return(cardDict[cardName]['prices']['paper'])
    # else: 
    #     print('Prices not found')

def createGraph(priceObj):
    dates = list(priceObj.keys())
    prices = list(priceObj.values())
    
    plt.xticks(rotation=90)
    plt.plot(dates,prices)
    plt.savefig('priceGraph.png')

if __name__ == '__main__':
    conn =  createConnection()

    while True:
        setName = input('Enter Set Name: ')#.lower()
        cardName = input('Enter Card Name: ')#.lower()
        priceType = input('(R)egular or (F)oil? ')

        if priceType == 'F':
            priceType = 'paperFoil'
        else:
            priceType = 'paper'

        # priceObject =
        getCardPrice(conn, setName, cardName, priceType)

        # if priceObject:
        #     createGraph(priceObject)
        
        if input('Continue? (Y/N)').lower() == 'n':
            break
        
    conn.close()
