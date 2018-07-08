import requests
import json
import datetime

requisicao = requests.get("http://api.promasters.net.br/cotacao/v1/valores")
cotacao = json.loads(requisicao.text)



nome = " DESAFIO 010 "
print('{:=^60}\n'.format(nome), "               ", datetime.datetime.now())

print('Vamos transformar em outras moedas o que você tem na carteira????\n')
grana = float(input('Digite quanto você tem na carteira: R$ '))

print('\nVocê tem R${:.2f} reais, que valem US$ {:.2f} dólares! '
      ':)'.format(grana, (grana/cotacao["valores"]["USD"]["valor"])))
print('Você tem R${:.2f} reais, que valem € {:.2f} Euros!'
      ' :)'.format(grana, (grana/cotacao["valores"]["EUR"]["valor"])))
print('Você tem R${:.2f} reais, que valem BTC {:.2f} Bitcoins!'
      ' :)'.format(grana, (grana/cotacao["valores"]["BTC"]["valor"])))
piada = " E aí, vamos para uma casa de câmbio??? "
print('\n{:=^60}'.format(piada))
