import socket


class Sender:
    def __init__(self, ip='127.0.0.1', port=6000, backlog=5):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_address = (ip, port)
        self.backlog = backlog
        print "STARTING SERVER AT"
        self.server_socket.bind(self.socket_address)
        self.server_socket.listen(self.backlog)

    def send_audio(self, chunk_array):
        client_socket, address = self.server_socket.accept()
        print("GOT CONNECTION FROM: ", address)
        if client_socket:
            for i in range(0, len(chunk_array)):
                client_socket.sendall(chunk_array[i])
        else:
            return
