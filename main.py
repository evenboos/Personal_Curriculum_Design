import openpyxl
import json


class user:
    name = ""
    password = ""
    weapon_list = []
    user_type = ""

    def __init__(self, Name, Password, Weapon_List, User_Type="Player") -> None:
        self.name = Name
        self.password = Password
        self.weapon_list = Weapon_List
        self.user_type = User_Type


class weapon:
    name = ""
    damage = 0
    ammo = 0
    rest_ammo = 0
    type = ""
    firing_mode = []

    def __init__(self, Name, Damage, Ammo, Rest_Ammo, Type, Firing_Mode):
        self.name = Name
        self.damage = Damage
        self.ammo = Ammo
        self.rest_ammo = Rest_Ammo
        self.type = Type
        self.firing_mode = Firing_Mode
    def change_weapon_state(self):
        pass

def initialize_weapon():
    pass
    
