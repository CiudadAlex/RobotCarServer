from servers.AbstractStreamServer import AbstractStreamServer
import pyaudio


class AudioStreamServer(AbstractStreamServer):

    listening = True

    def __init__(self, interval_record_secs=0.5):
        super().__init__(port=7998, check_collect_interval_millis=0, check_send_interval_millis=0)

        self.interval_record_secs = interval_record_secs

        # Variables
        self.chans = 1
        self.dev_index = 2
        self.rate = 16000
        self.audio_format = pyaudio.paInt16
        self.chunk_size = self.rate  # 1 second

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.audio_format, rate=self.rate, channels=self.chans,
                                  input_device_index=self.dev_index, input=True, frames_per_buffer=self.chunk_size)

    def get_new_item_metadata_and_bytes(self):

        if AudioStreamServer.listening is False:
            return None, None

        read_size = int(self.chunk_size * self.interval_record_secs)
        audio_chunk = self.stream.read(read_size, exception_on_overflow=False)
        item_metadata = bytes('Audio', 'utf-8')

        return item_metadata, audio_chunk

