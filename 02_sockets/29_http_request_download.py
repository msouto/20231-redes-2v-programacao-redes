import os
import requests
from bs4 import BeautifulSoup

def obter_arquivos_disponiveis(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links_arquivos = soup.find_all('a', href=True)
    nomes_arquivos = [link['href'] for link in links_arquivos]

    return nomes_arquivos

def solicitar_escolha_usuario(nomes_arquivos):
    print("Arquivos disponíveis para download:")
    for i, nome_arquivo in enumerate(nomes_arquivos):
        print(f"{i + 1}. {nome_arquivo}")

    while True:
        escolha = input("Digite o número do arquivo que deseja salvar (ou '0' para sair): ")
        try:
            escolha = int(escolha)
            if escolha == 0:
                return None
            elif 1 <= escolha <= len(nomes_arquivos):
                return nomes_arquivos[escolha - 1]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def tratar_download_arquivo(url, nome_arquivo):
    response = requests.head(url + nome_arquivo)
    if response.status_code != 200:
        print("Arquivo não encontrado.")
        return
    
    if nome_arquivo.endswith('/'):
        tratar_download_diretorio(url, nome_diretorio)
    else:
        fazer_download_arquivo(url, nome_arquivo)

def tratar_download_diretorio(url, nome_diretorio):
    url_diretorio = url + nome_diretorio
    nomes_arquivos = obter_arquivos_disponiveis(url_diretorio)

    if not nomes_arquivos:
        print("Diretório vazio.")
        return
    
    nome_local_diretorio = nome_diretorio.rstrip('/')
    os.makedirs(nome_local_diretorio, exist_ok=True)

    for nome_arquivo in nomes_arquivos:
        fazer_download_arquivo(url_diretorio, nome_arquivo, destino=nome_local_diretorio)

def fazer_download_arquivo(url, nome_arquivo, destino=''):
    url_arquivo = url + nome_arquivo
    response = requests.get(url_arquivo, stream=True, enconding='utf-8')

    if response.status_code != 200:
        print(f"Não foi possível fazer o download do arquivo '{nome_arquivo}'." )
        return
    
    nome_local_arquivo = os.path.join(destino, nome_arquivo) if destino else nome_arquivo
    with open(nome_local_arquivo, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f"Arquivo '{nome_arquivo}' salvo com sucesso como '{nome_local_arquivo}' ")

# Solicita ao usuário que insira a URL
url = input("Digite a URL: ")

# Obtem a lista de arquivos disponíveis
nomes_arquivos = obter_arquivos_disponiveis(url)

# Solicita ao usuário que escolha um arquivo para salvar
arquivo_escolhido = solicitar_escolha_usuario(nomes_arquivos)

if arquivo_escolhido:
    print(f"Você escolheu salvar o arquivo '{arquivo_escolhido}'.")
    tratar_download_arquivo(url, arquivo_escolhido)

else:
    print("Nenhum arquivo selecionado. O programa será encerrado.")
