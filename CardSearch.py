import requests
import json
import matplotlib.pyplot as plt

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
    

def getCardPrice(cardName, cardDict):
    if cardName not in cardDict:
        print('Card Name Not Found')
        return False

    if 'prices' in cardDict[cardName]:
        return(cardDict[cardName]['prices']['paper'])
    else: 
        print('Prices not found')

def createGraph(priceObj):
    dates = list(priceObj.keys())
    prices = list(priceObj.values())
    
    plt.xticks(rotation=90)
    plt.plot(dates,prices)
    plt.savefig('priceGraph.png')

if __name__ == '__main__':
    allCards = getAllCards()

    while True:
        cardName = input('Enter Card Name:').lower()
        priceObject = getCardPrice(cardName, allCards)

        if priceObject:
            createGraph(priceObject)
        
        if input('Continue? (Y/N)').lower() == 'n':
            break
