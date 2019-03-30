import requests
import json

url = 'http://data.fixer.io/api/latest?access_key=643653920cdcebb255294ba6b33f4b0f'
print('Acessando base de dados...')
response = requests.get(url)
if response.status_code == 200:
	print('Conseguiu acessar base de dados!')
	print('Buscando informaões das moedas...')
	dados = response.json()
	euro_real = dados['rates']['BRL']/dados['rates']['EUR']
	dollar_real = dados['rates']['BRL']/dados['rates']['USD']
	btc_real = dados['rates']['BRL']/dados['rates']['BTC']
	print('%.2f' % euro_real)
	print('%.2f' % dollar_real)
	print('%.2f' % btc_real)
else:
	print("Site com problema!")
