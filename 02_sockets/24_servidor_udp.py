import socket

def main():

    #criar o socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 8000)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(server_address)

    print(f"Servidor UDP iniciado em {server_address[0]}:{server_address[1]}")

    #Loop principal do servidor
    while True:
        data, client_address = server_socket.recvfrom(1024)

        message = data.decode('utf-8')

        print(f"Mensagem recebida do cleinte {client_address}: {message}" )
        
        if message == "quit":
            break

    server_socket.close()
    print("Servidor encerrado.")

if __name__ == '__main__':
    main()