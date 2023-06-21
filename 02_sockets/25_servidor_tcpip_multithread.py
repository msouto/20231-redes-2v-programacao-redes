import socket
#para manipulação das threads
import threading

def handle_client(client_socket, address):
    print(f"Conexão aceita de {address[0]}:{address[1]}")
    client_socket.send(b"Bem-vindo ao servidor!")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        message=data.decode("utf-8")
        print(f"Mensagem do cliente {address[0]}:{address[1]}: {message}")

        if message.strip().lower() == "quit":
            break

        response = "Confirma recepção"
        client_socket.send(response.encode("utf-8"))

    client_socket.close()
    print(f"Conexão terminada em {address[0]}:{address[1]}")

def start_server():
    host = "0.0.0.0" #Escutando em qualquer interface, não apenas loopback
    port = 2000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host,port))

    server_socket.listen(10)

    print(f"Servidor em listen em {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()

        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()


start_server()
