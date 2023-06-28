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

# Solicita ao usuário que insira a URL
url = input("Digite a URL: ")

# Obtem a lista de arquivos disponíveis
nomes_arquivos = obter_arquivos_disponiveis(url)

# Solicita ao usuário que escolha um arquivo para salvar
arquivo_escolhido = solicitar_escolha_usuario(nomes_arquivos)

if arquivo_escolhido:
    print(f"Você escolheu salvar o arquivo '{arquivo_escolhido}'.")
    # Faça algo com o arquivo escolhido, como fazer o download ou processamento adicional
else:
    print("Nenhum arquivo selecionado. O programa será encerrado.")
