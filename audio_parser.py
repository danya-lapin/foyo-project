class Parser:
    def __init__(self, path='audio_sample.mp3'):
        self.filepath = path

    def parse_audio(self):
        data = open(self.filepath, 'rb').read().split('\\')
        data.pop(0)
        return data
