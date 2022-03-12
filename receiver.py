import socket


class Receiver:
    def __init__(self, ip='127.0.0.1', port=6000):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_address = (ip, port)
        self.client_socket.connect(self.socket_address)
        print("CLIENT CONNECTED TO ", self.socket_address)
        self.data = b""

    def receive_audio(self):
        while True:
            package = self.client_socket.recv(4*1024)
            if package:
                self.data += package
            else:
                break

    def close_socket(self):
        self.client_socket.close()
