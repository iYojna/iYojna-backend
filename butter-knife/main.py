import json
import os
import re
import time
from csv import writer

import httpcore
from bs4 import BeautifulSoup as soup
from googletrans import Translator
import requests


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

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


def get_field(scheme_div, pattern):
    scheme_field = [scheme_p for scheme_p in scheme_div.find_all("p") if
                    pattern.search(_translate_data(scheme_p.text))]
    if scheme_field:
        scheme_field = scheme_field[0].text
    else:
        return
    scheme_field = scheme_field.split(":")[-1]

    return scheme_field


def get_scheme_data(scheme_link):
    scheme_data = json.load(open(os.path.join(ROOT_DIR, "scheme_template.json"), "r"))

    response = requests.get(scheme_link)

    res_soup = soup(response.content, "html.parser")
    scheme_div = res_soup.find("div", {"class": "parishisht"})

    scheme_name = scheme_div.find("h2").text
    scheme_name = scheme_name.split(":")[-1]
    scheme_data["gu"]["name"] = scheme_name
    scheme_data["en"]["name"] = _translate_data(scheme_name)

    roi_pattern = re.compile(r"^rate of interest", re.IGNORECASE)
    scheme_roi = get_field(scheme_div, roi_pattern)
    if scheme_roi:
        scheme_data["gu"]["interest_rate"] = scheme_roi
        scheme_data["en"]["interest_rate"] = _translate_data(scheme_roi)

    income_pattern = re.compile(r"^income", re.IGNORECASE)
    scheme_income = get_field(scheme_div, income_pattern)
    if scheme_income:
        scheme_data["gu"]["income_limit"] = scheme_income
        scheme_data["en"]["income_limit"] = _translate_data(scheme_income)

    curr_ele = scheme_div.find("h6")
    curr_head = ""
    translated_head = ""
    while curr_ele:
        try:
            if curr_ele.name == "h6":
                curr_head = curr_ele.text
                translated_head = _translate_data(curr_head)
                scheme_data["gu"]["extra_data"][curr_head] = []
                scheme_data["en"]["extra_data"][translated_head] = []
            elif curr_ele != "\n":
                scheme_data["gu"]["extra_data"][curr_head].append(curr_ele.text)
                scheme_data["en"]["extra_data"][translated_head].append(_translate_data(curr_ele.text))

            curr_ele = curr_ele.nextSibling
        except httpcore._exceptions.ReadTimeout:
            print("Timed Out. Waiting for 5 seconds")
            time.sleep(5)

    scheme_data["link"] = scheme_link

    return scheme_data


def generate_csv(scheme_link):
    response = requests.get(scheme_link)

    res_soup = soup(response.content, "html.parser")
    scheme_div = res_soup.find("div", {"class": "parishisht"})

    items = scheme_div.find_all("li")
    items = [item.text for item in items]

    with open('bullets.csv', 'w', newline="") as f:
        writer_obj = writer(f)

        writer_obj.writerow(["Source", "Translated"])
        for item in items:
            if item.strip():
                writer_obj.writerow([item, _translate_data(item)])


def _translate_data(data):
    translated_data = translator.translate(data, dest="en")
    return translated_data.text


if __name__ == '__main__':
    schemes = get_schemes()
    test_scheme = list(schemes.values())[0]
    # scheme_data = get_scheme_data(test_scheme)
    generate_csv(test_scheme)
