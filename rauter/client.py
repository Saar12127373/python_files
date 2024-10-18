
import socket





clint_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clint_socket.connect(("", 8000))

def recv_all(clint_socket, length):
    msg = ""
    msg += clint_socket.




while True:
    
    msg_recv_len = clint_socket.recv(2)
    message = clint_socket.recv(msg_recv_len)