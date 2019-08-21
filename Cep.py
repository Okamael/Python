import requests
import json


inputCep= input('Digite o cep:')

if len(inputCep) != 8:
    print('CEP invalido')
    exit()

requests = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(inputCep))

retornoCep = requests.json()

print("Cep:{}".format(retornoCep['cep']))
print("Rua:{}".format(retornoCep['address_name']))
print("Bairro:{}".format(retornoCep['district']))
print("Cidade:{}".format(retornoCep['city']))
print("Cidade:{}".format(retornoCep['state']))


