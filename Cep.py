import requests
import json
import webbrowser


inputCep= input('Digite o cep:')

if len(inputCep) != 8:
    print('CEP invalido')
    exit()

requests = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(inputCep))

retornoCep = requests.json()
#openInBrowserMap= 'https://www.google.com/maps/search/?api=1&query={},{}'.format(input)
#print(retornoCep)
print("Cep:{}".format(retornoCep['cep']))
print("Rua:{}".format(retornoCep['address_name']))
print("Bairro:{}".format(retornoCep['district']))
print("Cidade:{}".format(retornoCep['city']))
print("Estado:{}".format(retornoCep['state']))
print('Latitude:{}'.format(retornoCep['lat']))
print('Longitude:{}'.format(retornoCep['lng']))

Latitude='{}'.format(retornoCep['lat'])
Longitude='{}'.format(retornoCep['lng'])

openInBrowserMap= 'https://www.google.com/maps/search/?api=1&query='+Latitude+','+Longitude+''

webbrowser.open_new(openInBrowserMap)





