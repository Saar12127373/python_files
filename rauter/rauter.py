
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.bind((socket.gethostname(), 8000))
print(socket.gethostname())
connection.listen(5)

while True:
    connectedsocket, address = connection.accept()
    print("Connection from {address} established".format(address = address))