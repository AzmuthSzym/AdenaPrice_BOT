import requests
from bs4 import BeautifulSoup
import json


url = 'https://adenacharts.northeurope.cloudapp.azure.com/api/currentPrice'


def price_request():
    response = requests.get(url)
    soup = str(BeautifulSoup(response.text, 'html.parser'))
    json_decode = json.loads(soup)
    return json_decode["price"]["now"]
