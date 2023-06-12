#Exemplo de protocolo simples
#Na mesma conexão, o cliente pode solicitar várias operações de cálculo.
#Cada operação deve ser enviada como uma string finalizada com o caractere de nova linha (\n). 
#O primeiro token da linha indica a operação (soma ou raiz quadrada). Os tokens seguintes indicam os argumentos da operação.
#A operação de soma necessita de dois argumentos.
#A operação de raiz quadrada necessita de um argumento.
#Mensagens desconhecidas são respondidas com “Mensagem invalida”.
#Após solicitar as operações, o cliente encerra a conexão.
#O servidor responde cada operação com o resultado do cálculo.
#Após ler todas as operações solicitadas (linhas), o servidor encerra a conexão.

import socket
import math

def handle_request(request):
    tokens = request.split()
    if tokens[0] == 'soma':
        if len(tokens) != 3:
            return "Mensagem inválida"
        try:
            num1 = float(tokens[1])
            num2 = float(tokens[2])
            return str(num1+num2)
        except ValueError:
            return "Mensagem inválida"
    elif tokens[0] == 'raiz':
        if len(tokens != 2):
            return "Mensagem inválida"
        try:
            num = float(tokens[1])
            return str(math.sqrt(num))
        except ValueError:
            return "Mensagem inválida"
    else:
        return "Mensagem inválida"

def start_server(host,port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Tratamento para reutilização do bind
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host,port))
    server_socket.listen(1)
    print("Servidor inicializado. Aguardando conexões...")
    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexão com o IP cliente: ", client_address)
        while True:
            try:
                request = client_socket.recv(1024).decode().strip()
                # Restante do código para processar a requisição
            except OSError as e:
                # Lidar com a desconexão do cliente
                print("Ocorreu um erro de conexão:", e)
                # Outras ações necessárias, como fechar o socket ou encerrar o servidor
            if not request:
                break
            #Resposta da rquest ao cliente, tem que ser tratado conforme o protocolo de aplicação
            response = handle_request(request)
            client_socket.send((response + '\n').encode())
            client_socket.close()
            print("Conexão encerrada com: ", client_address)

if __name__=='__main__':
    host = 'localhost'
    port=2000
    start_server(host,port)
