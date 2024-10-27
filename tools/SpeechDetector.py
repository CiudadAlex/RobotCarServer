import webrtcvad
from pydub import AudioSegment
import numpy as np
import io


class SpeechDetector:

    def __init__(self, aggressiveness=3):
        self.vad = webrtcvad.Vad(aggressiveness)

    @staticmethod
    def convert_to_pcm(audio_chunk):
        audio = AudioSegment.from_file(io.BytesIO(audio_chunk))
        audio = audio.set_channels(1)  # Mono
        audio = audio.set_frame_rate(16000)  # 16 kHz
        return np.array(audio.get_array_of_samples())

    def detect_voice(self, audio_chunk):

        audio_pcm = self.convert_to_pcm(audio_chunk)

        # Divide in segments of 30 ms (mandatory for VAD)
        frame_duration = 30  # ms
        sample_rate = 16000
        samples_per_frame = int(sample_rate * frame_duration / 1000)

        # Evaluate each frame to detect speech
        is_speech_detected = False
        for i in range(0, len(audio_pcm), samples_per_frame):
            frame = audio_pcm[i:i + samples_per_frame].tobytes()
            if self.vad.is_speech(frame, sample_rate):
                is_speech_detected = True
                break

        return is_speech_detected

