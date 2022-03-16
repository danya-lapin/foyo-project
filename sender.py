import socket
import threading

HEADER = 4 * 1024


class Sender:
    def __init__(self, ip='127.0.0.1', port=6000, backlog=5):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_address = (ip, port)
        self.backlog = backlog
        print("STARTING SERVER AT")
        self.server_socket.bind(self.socket_address)
        self.server_socket.listen(self.backlog)
        self.connected = False

    def send_audio(self, chunk_array) -> None:
        client_socket, address = self.server_socket.accept()
        self.connected = True
        print("GOT CONNECTION FROM: ", address)
        if client_socket:
            while self.connected:
                self.handle_client(chunk_array)
        else:
            return

    def handle_client(self, chunk_array):
        chunk = b''
        for i in range(0, len(chunk_array)):
            chunk += chunk_array[i]
            if i % HEADER == 0:
                self.server_socket.send(chunk)
                chunk = b''

    def close(self):
        self.server_socket.close()
