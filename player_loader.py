import json

class PlayerLoader:
    def __init__(self):
        self.players = {}  # A dictionary to store player information

    def load_players(self):
        # Load player information from a file
        with open('user_list.json', 'r') as user_json:
            user_list = json.load(user_json)
            for user in user_list["user"]:
                self.players[user["username"]] = user["password"]

    def get_player(self, username):
        return self.players.get(username)

    def add_player(self, username, password):
        # Add player information to the dictionary and the file
        self.players[username] = password
        with open('user_list.json', 'r+') as user_json:
            user_list = json.load(user_json)
            user_list["user"].append({"username": username, "password": password})
            user_json.seek(0)
            json.dump(user_list, user_json, indent=4)
    def get_user_type(self, username):
        # Get the user type of the player
        with open('user_list.json', 'r') as user_json:
            user_list = json.load(user_json)            
            for user in user_list["user"]:
                if user["username"] == username:
                    return user["user_type"]
