from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import logging

def get_price():
    url = 'https://shop.tcgplayer.com/magic/legends/the%20tabernacle%20at%20pendrell%20vale'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        marketPriceDiv = html.find('div', attrs={'class':'price-point--market'})
        marketPriceTD = marketPriceDiv.find('td', attrs={'class':'price-point__data'})
        marketPrice = marketPriceTD.string.strip()
        return marketPrice

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    logging.basicConfig(filename='error.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.error(e)

if __name__ == '__main__':
    print('Working...')
    print(get_price())
    print('Done')