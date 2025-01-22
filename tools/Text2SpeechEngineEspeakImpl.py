import espeak


class Text2SpeechEngineEspeakImpl:

    instance = None

    @staticmethod
    def get_instance():
        if Text2SpeechEngineEspeakImpl.instance is None:
            Text2SpeechEngineEspeakImpl.instance = Text2SpeechEngineEspeakImpl()
        return Text2SpeechEngineEspeakImpl.instance

    def __init__(self):

        espeak.init()
        self.speaker = espeak.Espeak()

    def say(self, text):

        self.speaker.say(text)

