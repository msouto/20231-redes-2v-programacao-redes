import socketserver
import threading

# Defina as configurações do servidor MQTT
MQTT_BROKER_HOST = "localhost"
MQTT_BROKER_PORT = 1883

# Callback quando o cliente envia uma mensagem MQTT
def handle_mqtt_message(data):
    # Aqui você pode implementar a lógica para lidar com as mensagens MQTT recebidas
    print("Mensagem MQTT recebida:", data)

# Crie uma classe para o servidor MQTT
class MQTTHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        handle_mqtt_message(self.data)

# Inicie o servidor MQTT em uma thread separada
def run_server():
    mqtt_server = socketserver.TCPServer((MQTT_BROKER_HOST, MQTT_BROKER_PORT), MQTTHandler)
    mqtt_server.serve_forever()

server_thread = threading.Thread(target=run_server)
server_thread.start()

try:
    # Mantenha o servidor em execução (pode ser alterado para um loop enquanto verdadeiro, por exemplo)
    while True:
        pass
except KeyboardInterrupt:
    # Encerre o servidor quando o usuário pressionar Ctrl+C
    server_thread.join()
    print("\nServidor MQTT encerrado.")
