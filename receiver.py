import socket

HEADER = 4 * 1024
IP = '127.0.0.1'
PORT = 6000
ADDR = (IP, PORT)


class Receiver:
    def __init__(self, ip=IP, port=PORT):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_address = (ip, port)
        self.client_socket.connect(self.socket_address)
        print("CLIENT CONNECTED TO ", self.socket_address)
        self.data = b""

    def receive_audio(self):
        while True:
            package = self.client_socket.recv(HEADER)
            if package:
                self.data += package
            else:
                break

    def close_socket(self):
        self.client_socket.close()
