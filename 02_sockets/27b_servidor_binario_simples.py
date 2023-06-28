import socket
import os

HOST = ''
PORT = 2000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Servidor iniciado. Aguardando conexões...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Conexão estabelecida com {address[0]}:{address[1]}")

    try:
        # Receber tamanho do nome do arquivo
        tamanho_nome_arquivo_bytes = client_socket.recv(4)
        tamanho_nome_arquivo = int.from_bytes(tamanho_nome_arquivo_bytes, 'big')

        # Receber nome do arquivo
        nome_arquivo_bytes = client_socket.recv(tamanho_nome_arquivo)
        nome_arquivo = nome_arquivo_bytes.decode('utf-8')

        # Receber tamanho do arquivo
        tamanho_arquivo_bytes = client_socket.recv(4)
        tamanho_arquivo = int.from_bytes(tamanho_arquivo_bytes, 'big')

        # Receber bytes do arquivo
        bytes_arquivo = b''
        bytes_recebidos = 0
        while bytes_recebidos < tamanho_arquivo:
            dados = client_socket.recv(4096)
            if not dados:
                break
            bytes_arquivo += dados
            bytes_recebidos += len(dados)

        # Salvar arquivo recebido
        with open(f"copia_{nome_arquivo}", "wb") as arquivo:
            arquivo.write(bytes_arquivo)

        print(f"Arquivo '{nome_arquivo}' recebido e salvo com sucesso!")

    finally:
        client_socket.close()
        print(f"Conexão encerrada com {address[0]}:{address[1]}")
