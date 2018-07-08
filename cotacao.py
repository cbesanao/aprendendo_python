import requests
import json
import time
import datetime


while True:
    requisicao = requests.get("http://api.promasters.net.br/cotacao/v1/valores")
    cotacao = json.loads(requisicao.text)

    print("="*10+" COTAÇÃO "+"="*10, datetime.datetime.now())
    print("Dólar: {:.2f}".format(cotacao["valores"]["USD"]["valor"]))
    print("Euro: {:.2f}".format(cotacao["valores"]["EUR"]["valor"]))
    print("Bitcoin: {:.2f}".format(cotacao["valores"]["BTC"]["valor"]))
    print("\n")
    time.sleep(2)

    print("Dólar:", cotacao["valores"]["USD"]["valor"])
    print("Euro:", cotacao["valores"]["EUR"]["valor"])
    print("Bitcoin:", cotacao["valores"]["BTC"]["valor"])
    break