import requests

#url a para solicitacao
url = 'http://www.ifrn.edu.br'

#Requisição HTTP GET
response = requests.get(url)

#imprimir o código de status e o conteudo
print('Status code:', response.status_code)
print('Response:')
print(response.text)