import socket 

from lib.base import BaseDrinkClass

class DrinkServer(BaseDrinkClass):
    def __init__(self) -> None:
        super().__init__()
        self.header = 10
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 29888))
        sock.listen(5)
        self.info("Server Listening on port 29888...")
        while True:
            (con, address) = sock.accept()
            data = con.recv(1024)
            msg = "Connected to server for the love of god"
            msg_back = f'{len(msg):<{self.header}}' + msg 
            con.send(bytes(msg_back, 'utf-8'))
            
            self.debug(str(data))
            self.debug(str(address))

if __name__ == "__main__":
    alfred = DrinkServer()
    alfred.run()