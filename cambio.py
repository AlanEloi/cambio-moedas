import requests
import json
import pandas as pd

url = 'http://data.fixer.io/api/latest?access_key=643653920cdcebb255294ba6b33f4b0f'
print('Acessando base de dados...')
response = requests.get(url)
if response.status_code == 200:
	print('Conseguiu acessar base de dados!')
	print('Buscando informações das moedas...')
	dados = response.json()
	day = dados["date"] 
	print("Acessando dados dos dia %s / %s / %s" % (day[8:], day[5:7], day[0:4]))
	euro_real = round(dados['rates']['BRL']/dados['rates']['EUR'],2)
	dollar_real = round(dados['rates']['BRL']/dados['rates']['USD'],2)
	btc_real = round(dados['rates']['BRL']/dados['rates']['BTC'],2)
	print('%.2f' % euro_real)
	print('%.2f' % dollar_real)
	print('%.2f' % btc_real)
	df = pd.DataFrame({'moedas':['Euro','Dollar','Bitcoin'],'Valores':[euro_real,dollar_real,btc_real]})
	df.to_csv('valores.csv', index=False, sep=";") 

	print("Arquivo importado com sucesso")

else:
	print("Site com problema!")

