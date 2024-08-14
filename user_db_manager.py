import json

class UserDbManager:
    def __init__(self, user_db_path):
        with open(user_db_path, 'r') as file:
            self.user_data_base = json.load(file)
            file.close()

    def close_db(self, user_db_path, data_base_updated):
        with open(user_db_path, 'w') as file:
            json.dump(data_base_updated, file, indent=4)
            file.close()