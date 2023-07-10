import requests
import json

def obter_informacoes_usuario_github(username):
    url = f"https://api.github.com/users/{username}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados_usuario = resposta.json()
        return dados_usuario
    else:
        return None

#Exemplo 
username = "msouto"
informacoes = obter_informacoes_usuario_github(username)

#print(informacoes)

if informacoes is not None:
    print("Informações do usuário:")
    print("Nome: ", informacoes["name"])
    print("Bio: ", informacoes["bio"])
    print("Empresa: ", informacoes["company"])
    print("Número de repositórios: ", informacoes["public_repos"])
else:
    print("Não foi possível obter informações do usuário")