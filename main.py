import sys
import requests
import json

# Pekne reseni!
# Chvalim:
#   - a dekuji za vcasne odevzdani
#   - pouziti konstant pro timeout a url
#   - pouziti funkce (s dokumentaci)


# TIMEOUT_SETTING = 0.001
TIMEOUT_SETTING = 5
WEB_API = "https://cat-fact.herokuapp.com/facts/random"


def from_hero_to_cat_facts(downloaded_data: dict):
    """Z poskytnutého dict vybere values pod klíčem "text" a vrátí list očíslovaných faktů."""
    cat_facts = []

    # no = 0
    # for each in downloaded_data:
    #     no += 1
    #     cat_facts.append(f"{no}. {each['text']}")

    # Alternativne (kratsi a stejne citelny kod):
    for index, fact in enumerate(downloaded_data):
        cat_facts.append(f"{index+1}. {fact['text']}")

    return cat_facts


try:
    # Parametry dotazu by se pri opakovanych dotazech pravdepodobne menily.
    # Proto bych je radsi umistil v kodu blizko mista, kde dotaz volame (a ne jako konstantu).
    request_params = {"amount": 10}

    response = requests.get(WEB_API, timeout=TIMEOUT_SETTING, params=request_params)
    response_json = response.json()

except requests.exceptions.Timeout as err:
    print(f"Jsi příliš nedočkavý*á! Nastala chyba: \n{err}")
    # V pripade, ze dojde k vyjimce a my vypiseme chybove hlaseni,
    # zrejme nechceme pokracovat s kodem nize; zapsal by se prazdny soubor.
    # Proto program radsi ukoncime.
    # Potom take nepotrebujeme deklarovat prazdne `response_json = {}` na zacatku programu.
    sys.exit(1)

with open("kocici_fakta.json", mode="w", encoding="utf-8") as output_file:
    json.dump(from_hero_to_cat_facts(response_json), output_file, indent=4)
