import socket
import threading
# import RPi.GPIO as GPIO
import time


bind_ip = '127.0.0.1'
# bind_ip = '192.168.1.129'
bind_port = 1256

# my_init_PWM()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(2)  # max backlog of connections

print ('Listening on {}:{}'.format(bind_ip, bind_port))

def handle_client_connection(client_socket):
    print('entered thread\n')
    client_socket.sendall('\n +++ WELCOME TO G9 SERVER +++\n'.encode())

    request = client_socket.recv(7).decode("utf-8")
    print(request)
    dial0 = 0
    dial1 = 0
    dial2 = 0
    dial3 = 0
    dial4 = 0
    dial5 = 0
    dial6 = 0
    dial7 = 0
    dial8 = 0
    dial9 = 0
    dial10 = 0
    dial11 = 0
    dial12 = 0

    while request != 'stop'.encode():
        #request = client_socket.recv(7).decode("utf-8)")
        dial0 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial1 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial2 = int.from_bytes(client_socket.recv(1), byteorder = 'big')                
        dial3 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial4 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial5 = int.from_bytes(client_socket.recv(1), byteorder = 'big')                
        dial6 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial7 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial8 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial9 = int.from_bytes(client_socket.recv(1), byteorder = 'big')                
        dial10 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial11 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial12 = int.from_bytes(client_socket.recv(1), byteorder = 'big')                

        # print(request)

        # dc = dial1
        # pwm = GPIO.PWM(18, 100)
        # pwm.start(dc)

        print('input: {}\toutput: {}\tlo: {}\tmid: {}\thi: {}\tlo_freq: {}\tmid_freq: {}\thi_freq: {}\tcmp_1: {}\tcmp_2: {}\trev_1: {}\trev_2: {}\n'.format(dial0, dial1, dial2, dial3, dial4, dial5, dial6, dial7, dial8, dial9, dial10, dial11, dial12 ))

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


def my_init_PWM():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    











    
