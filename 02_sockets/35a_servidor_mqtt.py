import socket
import threading

# Constantes do protocolo MQTT
MQTT_BROKER_HOST = '0.0.0.0'  # Ou coloque o IP desejado
MQTT_BROKER_PORT = 1883

def create_mqtt_socket():
    # Criar um socket TCP
    mqtt_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mqtt_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return mqtt_socket

def bind_socket(socket):
    # Associar o socket a um endereço e porta
    socket.bind((MQTT_BROKER_HOST, MQTT_BROKER_PORT))

def listen_for_clients(socket):
    # Aguardar conexões de clientes
    socket.listen(5)
    print(f"Servidor MQTT ouvindo em {MQTT_BROKER_HOST}:{MQTT_BROKER_PORT}")

def handle_client(client_socket):
    while True:
        try:
            # Receber a mensagem do cliente
            data = client_socket.recv(1024)
            if not data:
                break

            # Simplesmente imprimir a mensagem recebida para fins de demonstração
            print(f"Mensagem recebida do cliente: {data.decode()}")

            # Enviar PUBACK de confirmação
            # Aqui, normalmente você processaria a mensagem e tomaria ação apropriada
            puback = b'\x40\x02\x00\x01'
            client_socket.sendall(puback)

        except Exception as e:
            print(f"Erro ao lidar com o cliente: {e}")
            break

    # Fechar o socket do cliente quando a conexão for encerrada
    client_socket.close()

if __name__ == '__main__':
    try:
        # Criar socket MQTT e associá-lo ao endereço e porta
        mqtt_socket = create_mqtt_socket()
        bind_socket(mqtt_socket)

        # Aguardar conexões de clientes em uma thread separada
        client_listener_thread = threading.Thread(target=listen_for_clients, args=(mqtt_socket,))
        client_listener_thread.start()

        # Aceitar e lidar com cada cliente em uma nova thread
        while True:
            client_socket, client_addr = mqtt_socket.accept()
            print(f"Cliente conectado: {client_addr}")

            client_handler_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler_thread.start()

    except KeyboardInterrupt:
        print("Servidor MQTT encerrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Fechar o socket MQTT
        mqtt_socket.close()
