import socket
import threading

bind_ip = '127.0.0.1'
# bind_ip = '192.168.1.129'
bind_port = 1256

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(2)  # max backlog of connections

print ('Listening on {}:{}'.format(bind_ip, bind_port))

def handle_client_connection(client_socket):
    print('entered thread\n')
    client_socket.sendall('-------------------------------------------\n +++ WELCOME TO G9 SERVER +++\n--------------------------------'.encode())

    request = client_socket.recv(1024)

    while request != 'stop'.encode():
        print('\r')
        print(request)
        request = client_socket.recv(1024)

    client_socket.close()

while True:
    client_sock, address = server.accept()
    print ('Accepted connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    client_handler.start()
    print('past new thread\n')


    
