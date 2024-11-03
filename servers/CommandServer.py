from flask import Flask, jsonify, request
from commanders.Commander import Commander
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


def run_server():
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8088, debug=False, use_reloader=False)).start()

