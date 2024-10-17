import speech_recognition as sr
from threading import Thread


class Speech2TextListener(Thread):

    def __init__(self, action_on_text):
        super().__init__()

        # Initialize the recognizer
        self.r = sr.Recognizer()
        self.action_on_text = action_on_text

    def run(self):

        # Loop infinitely for user to speak

        while True:

            # Exception handling to handle exceptions at the runtime
            try:

                # use the microphone as source for input.
                with sr.Microphone() as source2:

                    # wait for a second to let the recognizer adjust the energy
                    # threshold based on the surrounding noise level
                    self.r.adjust_for_ambient_noise(source2, duration=0.2)

                    # listens for the user's input
                    audio2 = self.r.listen(source2)

                    # Using google to recognize audio
                    my_text = self.r.recognize_google(audio2)
                    my_text = my_text.lower()

                    self.action_on_text(my_text)

            except sr.RequestError as e:
                print("Speech2TextListener: Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                print("Speech2TextListener: unknown error occurred")