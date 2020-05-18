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
    return html

def single_page_plugins(link):
    links = []
    next_page = ""
    html = getHTML(link)
    soup = BeautifulSoup(html, "html.parser")
    products = soup.find("div", {"class": "shop-container"})
    products = products.findAll("div", {"class": "product-small box"})
    for product in products:
        links.append(product.find("a")['href'])
    
    try:
        next_page = soup.find("a",{"class": "next page-number"})['href']
    except:
        pass

    ret = {}
    ret["links"] = links
    ret["next_page"] = next_page
    return ret

def get_all_plugins(link):
    plugins = []
    while True:
        page_plugin = single_page_plugins(link)
        plugins.extend(page_plugin['links'])
        pprint(page_plugin['links'])
        if page_plugin['next_page'] == '':
            break
        link = page_plugin['next_page']
    return(plugins)

def get_download_link(page_link):
    html = getHTML(page_link)
    soup = BeautifulSoup(html, "html.parser")
    download_link = soup.find("a", {"class": "yith-wcmbs-download-button"})['href']
    return download_link

def download_file(link, name):
    name = "plugins/{}.zip".format(name)
    with open("cookie_gpl.txt") as f:
        cookie = f.readline()
    headers = {'User-agent': 'Mozilla/5.0', 'Cookie': cookie, 'DNT': '1'}
    d_file = requests.get(link, headers = headers)
    open(name, "wb").write(d_file.content)

def make_plugins_json():
    plugins = {}
    plugins['link'] = get_all_plugins("https://www.gplfamily.com/product-category/wordpress-plugins/")
    with open('plugins.json', 'w') as f:
        json.dump(plugins, f)

def make_downlinks_json():
    download_file = {}
    download_file["data"] = []
    with open('plugins.json', 'r') as f:
        plugins = json.load(f)
    for plugin in plugins['link']:
        download_link = get_download_link(plugin)
        name = plugin.replace("https://www.gplfamily.com/shop/", "").strip("/")
        product = []
        product.append(name)
        product.append(download_link)
        pprint(product)
        download_file['data'].append(product)

    with open('download_links.json', 'w') as f:
        json.dump(download_file, f)

def download_driver():
    with open('download_links.json', 'r') as f:
        download_infs = json.load(f)
    download_infs = download_infs['data']
    for download_inf in download_infs:
        pprint(download_inf[0])
        download_file(download_inf[1], download_inf[0])

# make_downlinks_json()
# download_file("https://www.gplfamily.com/?protected_file=b12bd9a0-24fc-4692-922b-f6e0b5beac19&product_id=784", "test")
# get_download_link("https://www.gplfamily.com/shop/5sec-snow/")
# pprint(get_all_plugins())