    # -*- coding: utf-8 -*-

import json
import requests
import re
from json.decoder import JSONDecoder

from bs4 import BeautifulSoup
# Gets the website we want.
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '^\\^Opera^\\^;v=^\\^77^\\^, ^\\^Chromium^\\^;v=^\\^91^\\^, ^\\^;Not',
    'sec-ch-ua-mobile': '?0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}
list_of_dicts1 = []
lik = "https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/"
links= []
for i in range(1, 13):
    if i < 2:
        res = lik
    else:
        res = lik+"?PAGEN_1="+str(i)
    links.append(res)
for link in links:
    res = requests.get(link, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    containers = soup.find_all(class_="bx_catalog_item_container gtm-impression-product")
    list_of_dicts = []
    for container in containers:
        data = json.loads(container["data-product"].encode("utf-8"))
        name = re.split(", ",data["name"])
        dictionary = {
            "name" : data["name"].replace("Смартфон ", ""),
            "articul" : data["id"],
            "price" : data["price"],
            "memory-size" : name[1]
        }
        list_of_dicts.append(dictionary)
    list_of_dicts1.append(list_of_dicts)
j = json.dumps(list_of_dicts1, indent = 4,ensure_ascii=False)
with open("smartphones.json", "w", encoding='utf-8') as outfile:
    outfile.write(j)
    outfile.close()
