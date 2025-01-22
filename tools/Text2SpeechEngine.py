from tools.Text2SpeechEngineEspeakImpl import Text2SpeechEngineEspeakImpl


class Text2SpeechEngine:

    instance = None

    @staticmethod
    def get_instance():
        if Text2SpeechEngine.instance is None:
            Text2SpeechEngine.instance = Text2SpeechEngine()
        return Text2SpeechEngine.instance

    def __init__(self):
        self.engine = Text2SpeechEngineEspeakImpl.get_instance()

    def say(self, text):
        self.engine.say(text)
