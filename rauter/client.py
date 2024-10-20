
import socket
import time

client1_ip = "10.0.0.21"
client1_mac = "80-E8-2C-F9-8D-7F"

router = ("", 8200)


clint_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clint_socket.connect((router))

def recv_all(sock, length):
    msg = b""
    while len(msg) < length:
        add = sock.recv(length - len(msg))
        msg += add
    return msg



while True:
    
    msg_recv_len = int.from_bytes(recv_all(clint_socket, 2),"big")
    recv_message = recv_all(clint_socket, msg_recv_len).decode()
    source_mac = recv_message[0:17]
    destination_mac = recv_message[17:34]
    source_ip = recv_message[34:45]
    destination_ip =  recv_message[45:56]
    message = recv_message[56:]
    

    print("\nPacket integrity:\ndestination MAC address matches client 1 MAC address: {mac}".format(mac=(client1_mac == destination_mac)))
    print("\ndestination IP address matches client 1 IP address: {mac}".format(mac=(client1_ip == destination_ip)))
    print("\nThe packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac=source_mac, destination_mac=destination_mac))
 
    print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))
 
    print("\nMessage: " + message)


