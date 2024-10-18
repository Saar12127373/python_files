
import socket





clint_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clint_socket.connect(("", 8000))

def recv_all(sock, length):
    msg = b""
    while len(msg) < length:
        add = sock.recv(length - len(msg))
        msg += add
    return msg



while True:
    
    msg_recv_len = recv_all(clint_socket, 2)
    message = recv_all(clint_socket, msg_recv_len).decode()