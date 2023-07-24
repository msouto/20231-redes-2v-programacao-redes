import socket
import threading

# Constantes do protocolo MQTT
MQTT_BROKER_HOST = '127.0.01'
MQTT_BROKER_PORT = 1883

# Comandos MQTT
MQTT_CONNECT = b'\x10\x0e\x00\x06MQIsdp\x03\x02\x00\x3c\x00\x0a'
MQTT_SUBSCRIBE = b'\x82\x0c\x00\x01\x00\x05topic'
MQTT_DISCONNECT = b'\xe0\x00'

def create_mqtt_socket():
    # Criar um socket TCP
    mqtt_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return mqtt_socket

def connect_to_broker(socket):
    # Conectar ao broker MQTT
    socket.connect((MQTT_BROKER_HOST, MQTT_BROKER_PORT))

def send_mqtt_message(socket, message):
    # Enviar mensagem MQTT
    socket.sendall(message)

def receive_mqtt_message(socket):
    # Receber mensagem MQTT
    data = socket.recv(1024)
    return data

def subscribe_to_topic(socket):
    # Inscrever-se em um tópico MQTT
    send_mqtt_message(socket, MQTT_SUBSCRIBE)

def handle_received_messages(socket):
    while True:
        try:
            # Receber a resposta do broker
            response = receive_mqtt_message(socket)

            # Verificar se é uma mensagem de publicação
            if response[0] & 0xF0 == 0x30:
                topic_length = response[3]
                topic = response[4:4 + topic_length]
                message = response[4 + topic_length:]
                print(f"Nova mensagem recebida no tópico {topic.decode()}: {message.decode()}")

        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            break

def close_mqtt_socket(socket):
    # Fechar o socket MQTT
    socket.close()

if __name__ == '__main__':
    try:
        # Criar socket MQTT
        mqtt_socket = create_mqtt_socket()

        # Conectar ao broker
        connect_to_broker(mqtt_socket)
        print("Conexão estabelecida com o broker MQTT.")

        # Enviar uma mensagem MQTT de conexão
        send_mqtt_message(mqtt_socket, MQTT_CONNECT)
        print("Conexão MQTT estabelecida.")

        # Inscrever-se em um tópico MQTT
        subscribe_to_topic(mqtt_socket)
        print("Inscrito no tópico MQTT.")

        # Criar uma thread para lidar com mensagens recebidas
        message_handler_thread = threading.Thread(target=handle_received_messages, args=(mqtt_socket,))
        message_handler_thread.start()

        # Aguardar a thread de manipulação de mensagens terminar
        message_handler_thread.join()

        # Desconectar do broker
        send_mqtt_message(mqtt_socket, MQTT_DISCONNECT)
        print("Desconectado do broker MQTT.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Fechar o socket MQTT
        close_mqtt_socket(mqtt_socket)
