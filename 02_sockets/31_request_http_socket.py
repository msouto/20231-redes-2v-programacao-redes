import socket
import urllib.parse import urlparse


#define as informações para acessar
url = 'http://www.ifrn.edu.br'
parser_url = urlparsel(url)
host = parser_url.netloc
resource = parser_url.path if parser_url.path else '/'
port = 80

#Descritor do socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #conectar ao servidor
    sock.connect((host,port))

    #Enviar a solicitação HTTP
    request = f"GET {resource} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    sock.sendall(request.encode())

    #Receber e imprimir a resposta
    response = b''
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data

    response_str = response.decode()

    #verificar se houve redirecionamento
    if '301 Moved Permnantly' in response_str:
        #Extrai a nova url do cabeçalho location
        location_start = response_str.find('Location: ') + len('Location: ')
        location_end = response_str.find('\r\n', location_start)
        new_url = response_str[location_start:location_end]
        print(f"Redirecionado para: {new_url}")

        #Atualizar as informações do host e resource
        parsed_new_url = urlparse(new_url)
        host = parsed_new_url.netloc
        resource = parsed_new_url.path if parsed_new_url.path else '/'

        continue
    
    print(response_str)
    break


finally:
    #fecha o socket
    sock.close()