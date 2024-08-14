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

    def retrieve_data_for_login(self, user_name, password):
        all_users = list(self.user_data_base.keys())
        if user_name in all_users:
            if self.user_data_base[user_name]['password'] == password:
                print("Login Successful")
                print("-- -- Welcome",user_name, "-- --")

                return self.user_data_base[user_name]
            else:
                print("Login Unsuccessful, Wrong password")
        else:
            print("User name doesn't exist")

