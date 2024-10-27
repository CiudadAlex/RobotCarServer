import pyaudio
import webrtcvad
import collections

# Configuraciones
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_DURATION_MS = 30
CHUNK_SIZE = int(RATE * CHUNK_DURATION_MS / 1000)
NUM_SILENT_CHUNKS = 10
NUM_VOICE_CHUNKS = 3

# Inicializa PyAudio y el VAD
audio = pyaudio.PyAudio()
vad = webrtcvad.Vad()
vad.set_mode(1)  # 0-3, con 3 siendo el más agresivo

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK_SIZE)

buffer = collections.deque(maxlen=NUM_SILENT_CHUNKS)

print("Listening...")

try:
    while True:
        chunk = stream.read(CHUNK_SIZE)
        is_speech = vad.is_speech(chunk, RATE)
        buffer.append((chunk, is_speech))

        if sum(1 for _, speech in buffer if speech) > NUM_VOICE_CHUNKS:
            print("Voice detected!")
            buffer.clear()  # Clear the buffer to start fresh

except KeyboardInterrupt:
    print("Stopping...")

finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()

