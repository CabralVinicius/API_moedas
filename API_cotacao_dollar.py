import requests
import json
import time
import datetime

while True:
    requisic = requests.get(
        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    cotacao = json.loads(requisic.text)
    print("=== Cotações de moeda ===", datetime.datetime.now())
    print(cotacao['USDBRL']['name'])
    print(cotacao['USDBRL']['high'])
    print(cotacao['USDBRL']['low'])
    print(cotacao['USDBRL']['create_date'])
    print("\n")
    print(cotacao['EURBRL']['name'])
    print(cotacao['EURBRL']['high'])
    print(cotacao['EURBRL']['low'])
    print(cotacao['EURBRL']['create_date'])
    print("\n")
    print(cotacao['BTCBRL']['name'])
    print(cotacao['BTCBRL']['high'])
    print(cotacao['BTCBRL']['low'])
    print(cotacao['BTCBRL']['create_date'])
    time.sleep(5)
    print("\n")
    print("\n")
