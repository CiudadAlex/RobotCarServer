import pyaudio
import wave
import queue
import speech_recognition as sr


class AudioCommanderProcessor:

    def __init__(self):

        # Initialize PyAudio
        self.p = pyaudio.PyAudio()

        # Initialize recognizer
        self.recognizer = sr.Recognizer()

        # Variables
        self.chans = 1
        self.dev_index = 2
        # self.rate = 44100
        self.rate = 16000
        self.audio_format = pyaudio.paInt16
        self.chunk_size = self.rate  # 1 seconds

        self.queue_of_chunks = queue.Queue()
        self.recognized_text = None

    def process_audio_chunk(self, audio_chunk, function_with_recognized_text):
        audio_data = sr.AudioData(audio_chunk, self.rate, self.p.get_sample_size(self.audio_format))

        try:
            text = self.recognizer.recognize_google(audio_data)
            print(f"Recognized Text: {text}")

            if self.recognized_text is None:
                self.recognized_text = text
            else:
                self.recognized_text = self.recognized_text + " " + text

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            if self.recognized_text is not None:
                function_with_recognized_text(self.recognized_text)

                print("Back waiting for commands...")

                with self.queue_of_chunks.mutex:
                    self.queue_of_chunks.queue.clear()

            self.recognized_text = None

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            self.recognized_text = None

    def store_audio_file(self, audio_chunk):

        # creates wave file with audio read in
        # Code is from the wave file audio tutorial as referenced below
        wav_output_filename = 'test1.wav'
        wavefile = wave.open(wav_output_filename, 'wb')
        wavefile.setnchannels(self.chans)
        wavefile.setsampwidth(self.p.get_sample_size(self.audio_format))
        wavefile.setframerate(self.rate)
        wavefile.writeframes(audio_chunk)
        wavefile.close()

    def store_and_recognize_audio(self, record_secs, function_with_recognized_text):

        # setup audio input stream
        stream = self.p.open(format=self.audio_format, rate=self.rate, channels=self.chans, input_device_index=self.dev_index,
                             input=True, frames_per_buffer=self.chunk_size)
        print("recording")
        frames = []

        for ii in range(0, int((self.rate/self.chunk_size)*record_secs)):
            data = stream.read(self.chunk_size, exception_on_overflow=False)
            frames.append(data)

        print("finished recording")

        stream.stop_stream()
        stream.close()
        self.p.terminate()

        audio_chunk = b''.join(frames)

        self.store_audio_file(audio_chunk)
        self.process_audio_chunk(audio_chunk, function_with_recognized_text)
        print("finished")


def action_on_text(text):
    print("You said: ", text)


record_secs = 10     # record time
audio_commander_processor = AudioCommanderProcessor()
audio_commander_processor.store_and_recognize_audio(record_secs, action_on_text)