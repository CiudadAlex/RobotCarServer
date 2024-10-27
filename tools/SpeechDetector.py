import webrtcvad


class SpeechDetector:

    def __init__(self, aggressiveness=3):
        self.vad = webrtcvad.Vad(aggressiveness)

    @staticmethod
    def divide_bytearray(byte_array, piece_size):
        return [byte_array[i:i + piece_size] for i in range(0, len(byte_array), piece_size)]

    def detect_voice(self, audio_chunk):

        # Divide in segments of 30 ms (mandatory for VAD)
        frame_duration = 30  # ms
        sample_rate = 16000
        samples_per_frame = int(sample_rate * frame_duration / 1000)

        list_frames = self.divide_bytearray(audio_chunk, samples_per_frame)

        # Evaluate each frame to detect speech
        is_speech_detected = False
        for frame in list_frames:

            if self.vad.is_speech(frame, sample_rate):
                is_speech_detected = True
                break

        return is_speech_detected

