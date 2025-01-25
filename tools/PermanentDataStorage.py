from pathlib import Path


class PermanentDataStorage:

    instance = None

    @staticmethod
    def get_instance():
        if PermanentDataStorage.instance is None:
            PermanentDataStorage.instance = PermanentDataStorage()
        return PermanentDataStorage.instance

    @staticmethod
    def get_storage_path():
        storage_path = str(Path(__file__).parent.parent.resolve()) + "/.storage"
        Path(storage_path).mkdir(parents=True, exist_ok=True)
        return storage_path

    def get_room_list_path(self):
        return self.get_storage_path() + "/room_list.data"

    def get_door_list_path(self):
        return self.get_storage_path() + "/door_list.data"

    @staticmethod
    def write_file(path, content):
        f = open(path, "w")
        f.write(content)
        f.close()

    @staticmethod
    def read_file(path):
        file_path = Path(path)

        if file_path.exists():
            f = open(path, "r")
            return f.read()
        else:
            return None

    def store_room_list(self, text):
        self.write_file(self.get_room_list_path(), text)

    def store_door_list(self, text):
        self.write_file(self.get_door_list_path(), text)

    def get_room_list(self):
        return self.read_file(self.get_room_list_path())

    def get_door_list(self):
        return self.read_file(self.get_door_list_path())

