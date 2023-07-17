import requests
from bs4 import BeautifulSoup

#Define a url de consulta
url = 'http://ifrn.edu.br'

#requsiição HTTP
response = requests.get(url)

#Verificar se requisicao foi valida e bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    #Ecnontrar o elemento section que contém as noticias
    noticias_section = soup.find('section', class_='noticias')

    #Encontrar o elemento final com as noticias
    noticias = noticias_section.find_all('div', class_='grid-item')

    #iterar sobre as noticias e extrair o titulo e o link de cada noticia
    for noticia in noticias:
        titulo = noticia.find('h3').text.strip()
        link = noticia.find('a')['href']
        subtitulo = noticia.find('p', class_='subtitulo')
        subtitulo = subtitulo.text.strip() if subtitulo else ""
        data = noticia.find('p', class_='date').text.strip()

        print(f"Título: {titulo}")
        print(f"Subtítulo: {subtitulo}")
        print(f"Data: {data}")
        print(f"Link: {link}")
        print("-" * 50)

else:
    print(f"Erro ao obter as notícias. Código de status: {response.status_code}")
    