import requests
from bs4 import BeautifulSoup

#Define a url de consulta
url = 'http://ifrn.edu.br'

#requsiição HTTP
response = requests.get(url)

#Verificar se requisicao foi valida e bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    #encontrar as noticias
#    noticias = soup.find_all('div', class_='grid-container noticias')
    noticias = soup.find_all('div', class_='grid-item')

    print(noticias)

    #ßiterar sobre as noticias e extrair informacoes de cada
    for noticia in noticias:
         titulo = noticia.find('h3').text_strip()

         print(f"Titulo: {titulo}")

else:
    print(f"Erro ao obter as notícias. Código de status: {response.status_code}")
    