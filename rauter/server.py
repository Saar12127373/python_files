
client1_ip = 
client1_mac = 
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen(2)
server_ip = 
server_mac = 
router_mac = 
while True:
    routerConnection, address = server.accept()
    if(routerConnection != None):
        print(routerConnection)
        break