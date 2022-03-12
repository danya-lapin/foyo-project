from sender import Sender
from receiver import Receiver
from audio_parser import Parser
from audiostream import get_output, AudioSample

server = Sender()
client = Receiver()
parser = Parser()

stream = get_output(channels=2, buffersize=1024*4, rate=44100)
sample = AudioSample()
stream.add_sample(sample)

sample.play()
data = parser.parse_audio()
server.send_audio(data)
client.receive_audio()
sample.write(client.data)