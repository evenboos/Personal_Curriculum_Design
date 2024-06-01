import json
import hashlib

class Player:
    def __init__(self, name,password):
        self.name = name
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        self.weapon_list = []

    def to_dict(self):
        return {
            "username": self.name,
            "password": self.password,  # Return the hashed password
            "weapon_list": [weapon.to_dict() for weapon in self.weapon_list],
        }


class Weapon:
    def __init__(self, name, damage, magazines_capacity, magazines_amounts, rest_bullets,firing_mode):
        self.name = name
        self.damage = damage
        self.magazines_capacity = magazines_capacity
        self.magazines_amounts = magazines_amounts
        self.rest_bullets = rest_bullets
        self.firing_mode = list(set(firing_mode.strip("{}").split(",")))  # Convert firing_mode to a list

    def to_dict(self):
        return {
            "name": self.name,
            "damage": self.damage,
            "magazines_capacity": self.magazines_capacity,
            "magazines_amounts": self.magazines_amounts,
            "rest_bullets": self.rest_bullets,
            "firing_mode": self.firing_mode
        }

class PlayerLoader:
    def __init__(self):
        self.players = {}  # A dictionary to store player objects

    def load_players(self):
        # Load player information from a file
        with open('user_list.json', 'r') as user_json:
            user_list = json.load(user_json)
            for user in user_list["user"]:
                player = Player(user["username"],user["password"])
                for weapon_data in user["weapon_list"]:
                    weapon = Weapon(weapon_data['name'], weapon_data['damage'], weapon_data['magazines_capacity'],
                                    weapon_data['magazines_amounts'], weapon_data['rest_bullets'], weapon_data['firing_mode'])  # Add firing_mode parameter
                    player.weapon_list.append(weapon)
                self.players[user["username"]] = player

    def get_player(self, username):
        return self.players.get(username)

    def add_player(self, player):
        # Add player information to the dictionary and the file
        self.players[player.name] = player
        with open('user_list.json', 'r+') as user_json:
            user_list = json.load(user_json)
            user_list["user"].append(player.to_dict())
            user_json.seek(0)
            json.dump(user_list, user_json, indent=4)

    def get_all_players(self):
        return list(self.players.values())