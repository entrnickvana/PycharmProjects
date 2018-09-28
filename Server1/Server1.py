import socket
import threading
import RPi.GPIO as GPIO
import time


bind_ip = '127.0.0.1'
# bind_ip = '192.168.1.129'
bind_port = 1256

my_init_PWM()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(2)  # max backlog of connections

print ('Listening on {}:{}'.format(bind_ip, bind_port))

def handle_client_connection(client_socket):
    print('entered thread\n')
    client_socket.sendall('-------------------------------------------\n +++ WELCOME TO G9 SERVER +++\n--------------------------------'.encode())

    request = client_socket.recv(3).decode("utf-8")
    print(request)
    dial1 = 0
    dial2 = 0
    dial3 = 0

    while request != 'stop'.encode():
        # request = client_socket.recv(3).decode("utf-8)")
        dial1 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial2 = int.from_bytes(client_socket.recv(1), byteorder = 'big')
        dial3 = int.from_bytes(client_socket.recv(1), byteorder = 'big')                
        # print(request)

        dc = dial1
        pwm = GPIO.PWM(18, 100)
        pwm.start(dc)


        print('dial1: {},    dial2: {},   dial3: {} \n'.format(dial1, dial2, dial3))

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
    











    
