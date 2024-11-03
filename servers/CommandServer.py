from flask import Flask, jsonify, request
from commanders.Commander import Commander

app = Flask(__name__)


@app.route('/led/<mode>', methods=['POST'])
def set_led(mode):
    print(f"Setting led mode: {mode}")
    success = Commander.execute(f"led {mode}")

    if success:
        return '', 204
    else:
        return f"Command {mode} not found", 400


app.run(host='0.0.0.0', port=8088)

