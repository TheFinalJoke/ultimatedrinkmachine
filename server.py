import json
from lib.base import BaseDrinkClass
from lib.protocol import DrinkServerSocket
import pdb

class DrinkServer(BaseDrinkClass):
    def __init__(self) -> None:
        super().__init__()
        self.header = 10

    def parse(self, req):
        main_json = json.loads(req)
        print(type(main_json))
    def run(self):
        server = DrinkServerSocket()
        server_sock = server.bind_and_listen()
        self.info("Server listening...")
        while True:
            clientsocket, addr = server_sock.accept()
            data = clientsocket.recv(1024)
            self.info(f"Data Recvd {data}")
            clientsocket.send(bytes(f"Data Accepted from {addr}", "utf-8"))
            self.parse(data)
if __name__ == "__main__":
    alfred = DrinkServer()
    alfred.run()