import subprocess


class Text2SpeechEngineEspeakImpl:

    instance = None

    @staticmethod
    def get_instance():
        if Text2SpeechEngineEspeakImpl.instance is None:
            Text2SpeechEngineEspeakImpl.instance = Text2SpeechEngineEspeakImpl()
        return Text2SpeechEngineEspeakImpl.instance

    def __init__(self):
        self.process = None

    def stop(self):

        if self.process is not None:
            self.process.terminate()

        self.process = None

    def say(self, text):

        self.stop()

        self.process = subprocess.Popen(["espeak", f"{text}"])
        return self.process.wait()
