from scapy.all import *
import os

# Dicionários para manter o contador de pacotes por IP de origem, IP de destino e tipo de protocolo
packet_count_src_ip = {}
packet_count_dst_ip = {}
packet_count_protocol = {}

# Função para atualizar os contadores de pacotes
def update_packet_counts(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        # Incrementa o contador de pacotes por IP de origem
        if src_ip in packet_count_src_ip:
            packet_count_src_ip[src_ip] += 1
        else:
            packet_count_src_ip[src_ip] = 1

        # Incrementa o contador de pacotes por IP de destino
        if dst_ip in packet_count_dst_ip:
            packet_count_dst_ip[dst_ip] += 1
        else:
            packet_count_dst_ip[dst_ip] = 1

        # Incrementa o contador de pacotes por tipo de protocolo
        if protocol in packet_count_protocol:
            packet_count_protocol[protocol] += 1
        else:
            packet_count_protocol[protocol] = 1

# Função para exibir as contagens em tempo real
def display_packet_counts():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
        print("Contagem de pacotes por IP de origem:")
        for ip, count in packet_count_src_ip.items():
            print(f"{ip}: {count} pacotes")

        print("\nContagem de pacotes por IP de destino:")
        for ip, count in packet_count_dst_ip.items():
            print(f"{ip}: {count} pacotes")

        print("\nContagem de pacotes por tipo de protocolo:")
        for protocol, count in packet_count_protocol.items():
            print(f"Protocolo {protocol}: {count} pacotes")

        # Espera por 1 segundo antes de atualizar novamente as contagens
        time.sleep(1)

# Inicia uma thread para exibir as contagens em tempo real
import threading
display_thread = threading.Thread(target=display_packet_counts)
display_thread.daemon = True
display_thread.start()

# Captura de pacotes em tempo real
sniff(prn=update_packet_counts, store=0)
