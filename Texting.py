from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import CardSearch

app = Flask(__name__)

@app.route('/sms', methods=['GET','POST'])
def sms():
    allCards = CardSearch.getAllCards()
    cardName = request.form['Body'].lower()
    message_body = CardSearch.getCardPrice(cardName,allCards)

    resp = MessagingResponse()
    resp.message('The card price is {}'.format(message_body))
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)