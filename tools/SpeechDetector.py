import webrtcvad


class SpeechDetector:

    def __init__(self, aggressiveness=3):
        self.vad = webrtcvad.Vad(aggressiveness)

    def detect_voice(self, audio_pcm):

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

