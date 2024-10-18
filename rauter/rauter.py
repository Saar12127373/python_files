
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.bind(("", 8000))
connection.listen(5)

while True:
    server_sock, address = connection.accept()
    print("Connection from {address} established".format(address = address))
    
    msg = "got it?"
    server_sock.sendall(len(msg).to_bytes(2, byteorder='big'))
    server_sock.sendall(msg.encode())
    