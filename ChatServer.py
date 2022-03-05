import socket
import threading


class Server:
    def __init__(self):
        self.host = ""
        self.port = 50000
        self.clients_list = {}

    def connect(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv_sock.bind((self.host, self.port))
        print('The Server is Up')

        while True:
            serv_sock.listen(1)
            client, address = serv_sock.accept()
            client.send('NAME:'.encode())
            name = client.recv(1024).decode()
            print('New member {} connected'.format(name))
            listen_thread = threading.Thread(target = self.listen, args = (client,))
            listen_thread.start()
            self.clients_list[name] = address
            print(name)

    def listen(self, client):
            while True:
                message = client.recv(1024).decode()
                if message:
                    print("says {!r}".format(message))




if __name__ == '__main__':
    server = Server()
    server.connect()


