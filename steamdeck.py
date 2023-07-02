import requests
from bs4 import BeautifulSoup
import csv
import random

def getSteamdeck():
    url = 'https://www.steamdeck.com/en/'

    ua_list = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'}

    user_agent = random.choice(list(ua_list))

    headers = {'User Agent': user_agent}

    response = requests.get(url, headers=headers)
    #print(response.status_code)

    soup = BeautifulSoup(response.content, 'lxml')

    steam_title = soup.find('h1', {'class': 'product-info__title h2'})
    steam_price = soup.find('div', {'class': 'deck_price_final'})

    print('SteamDeck 64gb version')
    print(steam_price.get_text())



