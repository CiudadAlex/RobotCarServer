from threading import Thread
from tools.SpeechDetector import SpeechDetector
import threading
import pyaudio
import wave
import queue
import speech_recognition as sr


class Speech2TextProcessor(Thread):

    def __init__(self, interval_record_secs, function_with_recognized_text, use_speech_detection=True,
                 should_store_audio_file=False):
        super().__init__()

        self.interval_record_secs = interval_record_secs
        self.function_with_recognized_text = function_with_recognized_text
        self.use_speech_detection = use_speech_detection
        self.should_store_audio_file = should_store_audio_file

        # Initialize PyAudio
        self.p = pyaudio.PyAudio()

        # Initialize recognizer
        self.recognizer = sr.Recognizer()

        self.speech_detector = SpeechDetector()

        # Variables
        self.chans = 1
        self.dev_index = 2
        self.rate = 16000
        self.audio_format = pyaudio.paInt16
        self.chunk_size = self.rate  # 1 second

        self.queue_of_chunks = queue.Queue()
        self.recognized_text = None

        self.stream = None
        self.active = False

    def process_audio_queue(self):

        try:
            while True:
                audio_chunk = self.queue_of_chunks.get()
                self.process_audio_chunk(audio_chunk)
                self.queue_of_chunks.task_done()

        except KeyboardInterrupt:
            print("Stopping audio capture...")

    def local_detection_of_speech(self, audio_chunk):

        if self.use_speech_detection:
            is_speech_detected = self.speech_detector.detect_voice(audio_chunk)
            print(f"Speech detected: {is_speech_detected}")

            if not is_speech_detected:
                raise sr.UnknownValueError

    def process_audio_chunk(self, audio_chunk):

        try:

            self.local_detection_of_speech(audio_chunk)

            audio_data = sr.AudioData(audio_chunk, self.rate, self.p.get_sample_size(self.audio_format))

            text = self.recognizer.recognize_google(audio_data)
            print(f"Recognized Text: {text}")

            if self.recognized_text is None:
                self.recognized_text = text
            else:
                self.recognized_text = self.recognized_text + " " + text

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            if self.recognized_text is not None:
                self.function_with_recognized_text(self.recognized_text)

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

    def run(self):

        self.active = True

        # Start recognizing audio in a separate thread
        recognizing_thread = threading.Thread(target=self.process_audio_queue)
        recognizing_thread.start()

        # setup audio input stream
        self.stream = self.p.open(format=self.audio_format, rate=self.rate, channels=self.chans,
                                  input_device_index=self.dev_index, input=True, frames_per_buffer=self.chunk_size)

        while self.active:
            print("recording")
            frames = []

            for ii in range(0, int((self.rate/self.chunk_size)*self.interval_record_secs)):
                data = self.stream.read(self.chunk_size, exception_on_overflow=False)
                frames.append(data)

            audio_chunk = b''.join(frames)

            if self.should_store_audio_file:
                self.store_audio_file(audio_chunk)

            self.queue_of_chunks.put(audio_chunk)
            print("finished recording")

        self.stream.stop_stream()
        self.stream.close()
        print("Speech2TextProcessor finished")

    def stop(self):
        self.active = False
