from PyQt6.QtWidgets import QApplication
from login_gui_system import LoginGuiSystem

import json
import gui

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
    
class MainWin:
    def __init__(self):
        self.login_gui_system = LoginGuiSystem()
        self.login_gui_system.login_system.login_success.connect(self.open_main_window)  # Connect the signal to the slot

    def open_main_window(self):
        self.login_gui_system.close()  # Close the login window
        self.main_window = gui.MainWindow()  # Create the main window
        self.main_window.show()  # Show the main window

if __name__ == '__main__':
    app = QApplication([])
    main_win = MainWin()
    main_win.login_gui_system.show()
    app.exec()