import socket
import audiostream
from audiostream import get_output
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from sender import Sender
from receiver import Receiver
from audio_parser import Parser

HEADER = 1024 * 4
CHANNELS = 2
FREQUENCY = 44100
BACKLOG = 5
PORT = 6000


class MainApp(MDApp):
    RequestDevice1 = ''
    RequestDevice2 = ''
    RequestDevice3 = ''
    ConnectedDevice1 = ''
    ConnectedDevice2 = ''
    WIFIDevice1 = ''
    WIFIDevice2 = ''
    deviceIP = ''

    def build(self):
        self.audio_stream = audiostream.get_output(channels=CHANNELS, buffersize=HEADER, rate=FREQUENCY)
        track = audiostream.AudioSample()

        self.server = Sender(ip='127.0.0.1', port=PORT, backlog=BACKLOG)
        self.client = Receiver(ip='127.0.0.1', port=PORT)
        self.audio_parser = Parser()

        self.title = 'App'
        self.theme_cls.theme_style = "Dark"
        self.data_table = MDDataTable(
            pos_hint={'center_x': 0.4, 'center_y': 0.495},
            size_hint=(0.8, 0.8),
            column_data=[
                ('name', dp(60)),
                ('request', dp(60)),
            ],
            row_data=[]
        )

    def connect_receiver(self):
        self.client.client_socket.close()
        self.client.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.client_socket.connect((self.deviceIP, PORT))
        print(f"CLIENT CONNECTED TO {self.deviceIP}")
        self.server.send_audio(self.audio_parser.parse_audio())


MainApp().run()
