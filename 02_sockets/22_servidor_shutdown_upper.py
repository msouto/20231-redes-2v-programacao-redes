import socket

HOST = socket.gethostbyname('localhost')
PORT = 2000

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind reuse
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_server_socket.bind((HOST, PORT))
tcp_server_socket.listen()

print('Servidor iniciado. Aguardando conexões...')

while True:
    client, addr = tcp_server_socket.accept()
    print('Conexão recebida de:', addr)

    while True:
        data = client.recv(1024).decode('utf-8').strip()
        if not data:
            break

        print('Mensagem recebida:', data)

        if data.lower() == 'shutdown':
            response = 'Bye bye'
            client.send(response.encode('utf-8'))
            client.close()
            tcp_server_socket.close()
            exit(0)

        response = data.upper()
        client.send(response.encode('utf-8'))

    client.close()