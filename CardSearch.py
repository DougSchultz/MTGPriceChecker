import requests
import json

def getAllCards():
    print('Getting Json...')

    try:
        allCardsJSON = requests.get('https://mtgjson.com/json/AllCards.json')
    except:
        print('There was an error getting json')

    print('Creating Object...')
    
    allCards = allCardsJSON.json()

    return allCards
    

def getCardPrice(cardName):
    allCards = getAllCards()

    if 'prices' in allCards[cardName]:
        print(allCards[cardName]['prices'])
    else: 
        print('Prices not found')

if __name__ == '__main__':
    cardName = input('Enter Card Name:')
    getCardPrice(cardName)