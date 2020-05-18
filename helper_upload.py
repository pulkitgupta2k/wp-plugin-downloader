from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json

def getHTML(link):
    with open("cookie_gpl.txt") as f:
        cookie = f.readline()
    headers = {'User-agent': 'Mozilla/5.0', 'Cookie': cookie, 'DNT': '1'}
    req = requests.get(link, headers=headers)
    html = req.content
    print(html)
    return html