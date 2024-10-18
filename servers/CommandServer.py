from flask import Flask, jsonify, request
from managers.LedStripManager import LedStripManager

app = Flask(__name__)


@app.route('/led/<mode>', methods=['POST'])
def set_led(mode):
    print(f"Setting led mode: {mode}")
    return '', 204

# FIXME refactor-merge with KeyboardCommander
