import requests
import json

print('####################')
print('### Digite A moeda ###')
print("####################")
print('Ex.: USD-BRL,EUR-BRL,BTC-BRL')

moeda= input('Digite o Cep para a consulta:')

requests= requests.get('https://economia.awesomeapi.com.br/json/{}'.format(moeda))

dadosMoeda= requests.json()

#print(dadosMoeda)
print(dadosMoeda)


