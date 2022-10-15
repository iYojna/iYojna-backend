import json

from bs4 import BeautifulSoup as soup
from googletrans import Translator
import requests


translator = Translator()
ROOT_URL = "https://gueedc.gujarat.gov.in/"

BLACKLIST = ["#", "javascript:void(0);", "javascript:void(0)", "javascript:void();", "javascript:void()"]


def get_schemes():
    response = requests.get(ROOT_URL)
    page_soup = soup(response.text, "html.parser")

    scheme_eles = page_soup.find("ul", {"class": "wsmenu-list"}).find("ul", {"class": "wsmenu-submenu"}).find_all("li")

    schemes_dict = {scheme.find("a").text: f"{ROOT_URL}{scheme.find('a').get('href')}"
                    for scheme in scheme_eles
                    if scheme.find("a").get("href") not in BLACKLIST}

    return schemes_dict


def get_scheme_data(scheme_link):
    scheme_data = json.load(open("scheme_data.json", "r"))

    response = requests.get(scheme_link)

    res_soup = soup(response.content, "html.parser")
    scheme_div = res_soup.find("div", {"class": "parishisht"})

    return scheme_div


def _translate_data(data):
    translated_data = translator.translate(data, dest="en")
    return translated_data.text


schemes = get_schemes()

