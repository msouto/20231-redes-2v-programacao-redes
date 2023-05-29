import socket

#informações para comunicação
HOST = socket.gethostbyname('localhost') #127.0.0.1
PORT = 2000 #0 - 65535

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen()

client, addr = tcp_server_socket.accept()
print('Conexão recebida de: ', addr)

while True:
    data = client.recv(1024)
    if not data:
        break
    message = 'Recebida'
    byte_msg = message.encode('utf-8')
    client.send(byte_msg)
    print('Mensagem recebida: ',data)

client.close()
tcp_server_socket.close()

