import socket

HOST = 'localhost'
PORT = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

try:
    # Solicitar nome do arquivo ao usuário
    nome_arquivo = input("Digite o nome do arquivo: ")
    
    # Enviar nome do arquivo
    sock.sendall(nome_arquivo.encode())

    # Enviar tamanho do arquivo
    tamanho_arquivo = len(open(nome_arquivo, 'rb').read())
    sock.sendall(str(tamanho_arquivo).encode())

    # Enviar bytes do arquivo
    with open(nome_arquivo, 'rb') as arquivo:
        bytes_arquivo = arquivo.read()
        sock.sendall(bytes_arquivo)

finally:
    sock.close()
