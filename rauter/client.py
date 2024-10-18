
import socket

clint_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clint_socket.connect(("", 8000))

while True:

    message = clint_socket.recv(1024)