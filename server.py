import socket 
import pickle

class DrinkServer():
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), 29888))
        sock.listen(5)
        print("Server listening on port 29888...")
        while True:
            (con, address) = sock.accept()
            data = con.recv(1024)
            
            con.send(b"Connected to server")
            
            print(data)

if __name__ == "__main__":
    alfred = DrinkServer()
    alfred.run()