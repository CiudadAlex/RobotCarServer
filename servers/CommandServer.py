from flask import Flask, jsonify, request, render_template, make_response
from commanders.Commander import Commander
from tools.Text2SpeechEngine import Text2SpeechEngine
from tools.DataStorage import DataStorage
from tools.PermanentDataStorage import PermanentDataStorage
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

    try:
        data = request.get_json()
        selected_room_id = data['selected_room_id']
        selected_room_name = data['selected_room_name']
        print(f"Store room: {selected_room_id} >> {selected_room_name}")

        DataStorage.get_instance().selected_room_id = selected_room_id
        DataStorage.get_instance().selected_room_name = selected_room_name

    except Exception:
        traceback.print_exc(file=sys.stdout)

    return '', 204


@app.route('/room', methods=['GET'])
def get_room():

    selected_room_id = DataStorage.get_instance().selected_room_id
    selected_room_name = DataStorage.get_instance().selected_room_name

    data = {
        'selected_room_id': selected_room_id,
        'selected_room_name': selected_room_name
    }

    print(f"Retrieved room: {data}")

    return make_response(jsonify(data), 200)


@app.route('/door', methods=['POST'])
def set_door():

    try:
        data = request.get_json()
        selected_door_id = data['selected_door_id']
        selected_door_name = data['selected_door_name']
        print(f"Store door: {selected_door_id} >> {selected_door_name}")

        DataStorage.get_instance().selected_door_id = selected_door_id
        DataStorage.get_instance().selected_door_name = selected_door_name

    except Exception:
        traceback.print_exc(file=sys.stdout)

    return '', 204


@app.route('/door', methods=['GET'])
def get_door():

    selected_door_id = DataStorage.get_instance().selected_door_id
    selected_door_name = DataStorage.get_instance().selected_door_name

    data = {
        'selected_door_id': selected_door_id,
        'selected_door_name': selected_door_name
    }

    print(f"Retrieved door: {data}")

    return make_response(jsonify(data), 200)


@app.route('/room_list', methods=['POST'])
def set_room_list():

    try:
        data = request.get_json()
        room_list = data
        print(f"Store room_list: {room_list}")

        PermanentDataStorage.get_instance().store_room_list(room_list)

    except Exception:
        traceback.print_exc(file=sys.stdout)

    return '', 204


@app.route('/room_list', methods=['GET'])
def get_room_list():

    room_list = PermanentDataStorage.get_instance().get_room_list()

    data = room_list
    print(f"Retrieved room_list: {data}")

    return data, 200


@app.route('/door_list', methods=['POST'])
def set_door_list():

    try:
        data = request.get_json()
        door_list = data
        print(f"Store door_list: {door_list}")

        PermanentDataStorage.get_instance().store_door_list(door_list)

    except Exception:
        traceback.print_exc(file=sys.stdout)

    return '', 204


@app.route('/door_list', methods=['GET'])
def get_door_list():

    door_list = PermanentDataStorage.get_instance().get_door_list()

    data = door_list
    print(f"Retrieved door_list: {data}")

    return data, 200


def run_server():
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8088, debug=False, use_reloader=False)).start()

