import socket

HOST = ''
PORT = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

try:
    # Solicitar nome do arquivo ao usuário
    nome_arquivo = input("Digite o nome do arquivo: ")
    
    # Enviar nome do arquivo
    nome_arquivo_encoded = nome_arquivo.encode('utf-8')
    tamanho_nome_arquivo_encoded = len(nome_arquivo_encoded).to_bytes(4, 'big')
    sock.sendall(tamanho_nome_arquivo_encoded + nome_arquivo_encoded)

    # Enviar tamanho do arquivo
    tamanho_arquivo = len(open(nome_arquivo, 'rb').read())
    tamanho_arquivo_encoded = tamanho_arquivo.to_bytes(4, 'big')
    sock.sendall(tamanho_arquivo_encoded)

    # Enviar bytes do arquivo
    with open(nome_arquivo, 'rb') as arquivo:
        bytes_arquivo = arquivo.read()
        sock.sendall(bytes_arquivo)

finally:
    sock.close()
