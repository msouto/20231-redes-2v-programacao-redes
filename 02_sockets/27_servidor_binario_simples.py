import socket

HOST = ''
PORT = 2000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

client_socket, address = server_socket.accept()

try:
    nome_arquivo = client_socket.recv(1024).decode().strip()
    tamanho_arquivo = client_socket.recv(1024).decode().strip()
    if tamanho_arquivo:
        tamanho_arquivo = int(tamanho_arquivo)
        bytes_arquivo = client_socket.recv(tamanho_arquivo)

        with open(f"copia_{nome_arquivo}", "wb") as arquivo:
            arquivo.write(bytes_arquivo)

finally:
    server_socket.close()
