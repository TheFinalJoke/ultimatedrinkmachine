import socket
import pickle

class hello_server():
    def __init__(self) -> None:
        super().__init__()
    def hello(self):
        return "hello From stuff"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((socket.gethostname(), 29888))
hello = hello_server()

server_socket.sendall(pickle.dumps(hello))
data = server_socket.recv(1024)

print(repr(data))
server_socket.close()