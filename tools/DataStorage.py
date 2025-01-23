

class DataStorage:

    instance = None

    @staticmethod
    def get_instance():
        if DataStorage.instance is None:
            DataStorage.instance = DataStorage()
        return DataStorage.instance

    def __init__(self):

        self.selected_room_id = None
        self.selected_room_name = None

        self.selected_door_id = None
        self.selected_door_name = None

        self.room_list = None
        self.door_list = None

        self.last_text_command = None

