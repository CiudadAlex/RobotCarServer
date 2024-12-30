from flask import Flask, jsonify, request, render_template, make_response
from commanders.Commander import Commander
from tools.Text2SpeechEngine import Text2SpeechEngine
from tools.DataStorage import DataStorage
import threading
import sys
import traceback

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


@app.route('/move_a_bit/<mode>/<secs>', methods=['POST'])
def set_move_a_bit(mode, secs):
    print(f"Setting move a bit mode: {mode}, secs: {secs}")
    success = Commander.execute_move_for_given_seconds(f"move {mode}", float(secs))

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
    text_to_say = data
    print(f"Say command: {text_to_say}")

    Commander.listen_off()

    try:
        Text2SpeechEngine.get_instance().say(text_to_say)
    except Exception:
        traceback.print_exc(file=sys.stdout)

    Commander.listen_on()

    return '', 204


@app.route('/ui', methods=['GET'])
def get_ui():
    return render_template('ui.html')


@app.route('/room', methods=['POST'])
def set_room():

    data = request.get_json()
    selected_room_id = data.selected_room_id
    selected_room_name = data.selected_room_name
    print(f"Store room: {selected_room_name}")

    DataStorage.get_instance().selected_room_id = selected_room_id
    DataStorage.get_instance().selected_room_name = selected_room_name

    return '', 204


@app.route('/room', methods=['GET'])
def get_room():

    selected_room_id = DataStorage.get_instance().selected_room_id
    selected_room_name = DataStorage.get_instance().selected_room_name

    data = {
        'selected_room_id': selected_room_id,
        'selected_room_name': selected_room_name
    }

    return make_response(jsonify(data), 200)


@app.route('/door', methods=['POST'])
def set_door():

    data = request.get_json()
    selected_door_id = data.selected_door_id
    selected_door_name = data.selected_door_name
    print(f"Store door: {selected_door_name}")

    DataStorage.get_instance().selected_room_id = selected_door_id
    DataStorage.get_instance().selected_room_name = selected_door_name

    return '', 204


@app.route('/door', methods=['GET'])
def get_door():

    selected_door_id = DataStorage.get_instance().selected_door_id
    selected_door_name = DataStorage.get_instance().selected_door_name

    data = {
        'selected_door_id': selected_door_id,
        'selected_door_name': selected_door_name
    }

    return make_response(jsonify(data), 200)


def run_server():
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8088, debug=False, use_reloader=False)).start()

