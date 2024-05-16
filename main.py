import requests
import json


TIMEOUT_SETTING = 0.001
WEB_API = "https://cat-fact.herokuapp.com/facts/random"
AMOUNT = {"amount": 10}
response_json = {}


def from_hero_to_cat_facts(downloaded_data):
    """Z poskytnutého dict vybere values pod klíčem "text" a vrátí list očíslovaných faktů"""
    cat_facts = []
    no = 0
    for each in downloaded_data:
        no += 1
        cat_facts.append(f"{no}. {each["text"]}")
    return cat_facts


try:
    response = requests.get(WEB_API, timeout=TIMEOUT_SETTING, params=AMOUNT)
    response_json = response.json()

except requests.exceptions.Timeout as err:
    print(f"Jsi příliš nedočkavý*á! Nastala chyba: \n{err}")

with open("kocici_fakta.json", mode="w", encoding="utf-8") as output_file:
    json.dump(from_hero_to_cat_facts(response_json), output_file, indent=4)
