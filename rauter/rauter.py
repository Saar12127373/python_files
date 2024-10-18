
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.bind(("", 8000))
connection.listen(5)

while True:
    server_sock, address = connection.accept()
    print("Connection from {address} established".format(address = address))
    
    msg = "got it?"
    msg_len = len("got it?")
    server_sock.sendall(msg_len.encode())
    