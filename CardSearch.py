import requests
import matplotlib.pyplot as plt
import sqlite3
from sqlite3 import Error
import ast

def createConnection():
    """ 
    Creates connection to AllSets.sqlite
    """
    try:
        conn = sqlite3.connect('AllSets.sqlite')
        conn.row_factory = sqlite3.Row
        return conn
    except Error as e:
        print(e)
    
    return None

def getCardPrice(setName, cardName, priceType):
    """ 
    Uses sqlite connection to query card prices of given Set and Card Name
    """
    conn = createConnection()
    cur = conn.cursor()
    cur.execute("SELECT prices FROM sets INNER JOIN cards ON setCode=code WHERE sets.name=? and cards.name=?", (setName,cardName))
    rows = cur.fetchone()

    if not rows:
        print("No results found")
        return

    pricesDict = ast.literal_eval(rows[0])
    conn.close()

    return(pricesDict[priceType])

def createGraph(priceObj):
    """
    Plots a price object and saves as priceGraph.png
    """
    dates = list(priceObj.keys())
    prices = list(priceObj.values())
    
    plt.xticks(rotation=90)
    plt.plot(dates,prices)
    plt.savefig('priceGraph.png')
    plt.show()

if __name__ == '__main__':
    while True:
        setName = input('Enter Set Name: ')
        cardName = input('Enter Card Name: ')
        priceType = input('paper or paperFoil? ')

        priceObject = getCardPrice(setName, cardName, priceType)

        if priceObject:
            createGraph(priceObject)
        
        if input('Continue? (Y/N)').lower() == 'n':
            break
