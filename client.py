import socket
import pickle
import time
class hello_server():
    def __init__(self) -> None:
        super().__init__()
    def hello(self):
        return "hello From stuff"
while True:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((socket.gethostname(), 29888))
    hello = bytes("hello from client 1", "utf-8")
    server_socket.sendall(hello)
    data = server_socket.recv(1024)
    print(repr(data))
    time.sleep(1)
    continue

server_socket.close()