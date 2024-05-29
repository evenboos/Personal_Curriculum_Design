import json


class Player:
    def __init__(self, name):
        self.name = name
        self.weapon_list = []


class Weapon:
    def __init__(self, name, damage, magazines_capacity, magazines_amounts, rest_bullets):
        self.name = name
        self.damage = damage
        self.magazines_capacity = magazines_capacity
        self.magazines_amounts = magazines_amounts
        self.rest_bullets = rest_bullets


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
            user_list["user"].append(
                {"username": username, "password": password})
            user_json.seek(0)
            json.dump(user_list, user_json, indent=4)

    def get_user_type(self, username):
        # Get the user type of the player
        with open('user_list.json', 'r') as user_json:
            user_list = json.load(user_json)
            for user in user_list["user"]:
                if user["username"] == username:
                    return user["user_type"]

    def get_all_players(self):
        with open('user_list.json', 'r') as f:
            data = json.load(f)

        players = []
        for player_data in data['user']:
            player = Player(player_data['username'])
            for weapon_data in player_data['weapon_list']:
                weapon = Weapon(weapon_data['name'], weapon_data['damage'], weapon_data['magazines_capacity'],
                                weapon_data['magazines_amounts'], weapon_data['rest_bullets'])
                player.weapon_list.append(weapon)
            players.append(player)

        return players
