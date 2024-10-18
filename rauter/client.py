
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
    message = recv_all(clint_socket, msg_recv_len).decode()
