import paho.mqtt.client as mqtt
import time

# Defina as configurações do servidor MQTT
MQTT_BROKER_HOST = "localhost"
MQTT_BROKER_PORT = 1883

# Callback quando o cliente se conecta ao servidor MQTT
def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao servidor MQTT com código de resultado: {rc}")

# Crie um cliente MQTT
mqtt_client = mqtt.Client()

# Atribua as funções de callback
mqtt_client.on_connect = on_connect

# Conecte-se ao servidor MQTT
mqtt_client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

# Inicie o loop de eventos do cliente MQTT
mqtt_client.loop_start()

try:
    while True:
        # Envie uma mensagem para o tópico "meu_topico"
        mensagem = "Hello, servidor MQTT!"
        mqtt_client.publish("meu_topico", mensagem)

        # Aguarde um pouco antes de enviar a próxima mensagem (intervalo de 5 segundos)
        time.sleep(5)
except KeyboardInterrupt:
    # Encerre o cliente MQTT quando o usuário pressionar Ctrl+C
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    print("\nCliente MQTT encerrado.")
