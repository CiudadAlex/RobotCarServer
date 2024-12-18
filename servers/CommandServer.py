from flask import Flask, jsonify, request
from commanders.Commander import Commander
from tools.Text2SpeechEngine import Text2SpeechEngine
import threading

app = Flask(__name__)


@app.route('/led/<mode>', methods=['POST'])
def set_led(mode):
    print(f"Setting led mode: {mode}")
    success = Commander.execute(f"led {mode}")

    if success:
        return '', 204
    else:
        return f"Command {mode} not found", 400


@app.route('/move/<mode>', methods=['POST'])
def set_move(mode):
    print(f"Setting move mode: {mode}")
    success = Commander.execute(f"move {mode}")

    if success:
        return '', 204
    else:
        return f"Command {mode} not found", 400


@app.route('/look/<mode>', methods=['POST'])
def set_look(mode):
    print(f"Setting look mode: {mode}")
    success = Commander.execute(f"look {mode}")

    if success:
        return '', 204
    else:
        return f"Command {mode} not found", 400


@app.route('/listen/<mode>', methods=['POST'])
def set_listen(mode):
    print(f"Setting listen mode: {mode}")
    success = Commander.execute(f"listen {mode}")

    if success:
        return '', 204
    else:
        return f"Command {mode} not found", 400


@app.route('/say', methods=['POST'])
def set_say():

    data = request.get_json()
    text_to_say = data.text
    print(f"Say command: {text_to_say}")

    Commander.listen_off()
    Text2SpeechEngine.get_instance().say(text_to_say)
    Commander.listen_on()

    return '', 204


def run_server():
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8088, debug=False, use_reloader=False)).start()

