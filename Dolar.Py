# cotação do dolar em tempo real(eu acho)

import requests
import json
valor = float(input('Digite a quantia em dinheiro que deseje converter:\t'))
requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = requisicao.json()

cotacao
{'USD': {'ask': '5.2962',
         'bid': '5.2947',
         'code': 'USD',
         'codein': 'BRL',
         'create_date': '2020-04-20 11:31:09',
         'high':'5.3003',
         'low':'5.2343',
         'name':'Dólar Comercial',
         'pctChange':'1.13',
         'timestamp':'1587393066',
         'varBid':'0.0591'}}
print('Valor atual do Dólar: R$' + cotacao['USD']['bid'])
vdolar=float(cotacao['USD']['bid'])
resultado=(valor/vdolar)
print('Valor da conversão para Dólar: U$ {}'.format(resultado))
