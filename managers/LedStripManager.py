import threading


class LedStripManager:

    audio_thread = threading.Thread(target=self.capture_audio, args=(save_audio_files,))
    audio_thread.start()