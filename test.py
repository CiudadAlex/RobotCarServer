from tools.Text2SpeechEngine import Text2SpeechEngine
import sys
import traceback


def say_test():

    text_to_say = "This robot has been engineered by Alejandro"

    try:
        Text2SpeechEngine.get_instance().say(text_to_say)
    except Exception:
        traceback.print_exc(file=sys.stdout)


say_test()
