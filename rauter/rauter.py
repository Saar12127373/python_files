
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.bind(("", 8000))
connection.listen(5)

while True:
    connectedsocket, address = connection.accept()
    print("Connection from {address} established".format(address = address))