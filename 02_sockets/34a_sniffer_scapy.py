from scapy.all import *

# Dicionários para manter o contador de pacotes por IP de origem, IP de destino e tipo de protocolo
packet_count_src_ip = {}
packet_count_dst_ip = {}
packet_count_protocol = {}

# Função para processar os pacotes capturados
def process_packet(packet):
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

        # Exibe o conteúdo do pacote
        print(packet.summary())

# Captura de pacotes em tempo real
sniff(prn=process_packet, store=0)

# Imprime a contagem de pacotes por IP de origem
print("\nContagem de pacotes por IP de origem:")
for ip, count in packet_count_src_ip.items():
    print(f"{ip}: {count} pacotes")

# Imprime a contagem de pacotes por IP de destino
print("\nContagem de pacotes por IP de destino:")
for ip, count in packet_count_dst_ip.items():
    print(f"{ip}: {count} pacotes")

# Imprime a contagem de pacotes por tipo de protocolo
print("\nContagem de pacotes por tipo de protocolo:")
for protocol, count in packet_count_protocol.items():
    print(f"Protocolo {protocol}: {count} pacotes")