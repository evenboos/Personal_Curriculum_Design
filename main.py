from PyQt6.QtWidgets import QApplication
from login_gui_system import LoginGuiSystem
import pandas as pd

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
def syn_weapon_list():
    # 读取 Excel 文件
    df = pd.read_excel('your_file.xlsx')

    # 读取 user_list.json 文件
    with open('user_list.json') as f:
        data = json.load(f)
    users = data['user']

    # 将 DataFrame 转换为 weapon 对象，并添加到对应的用户的武器列表中
    for _, row in df.iterrows():
        weapon = {
            'name': row['Weapon_Name'],
            'damage': row['Damage'],
            'magazines_capacity': row['Magazines_capacity'],
            'magazines_amounts': row['Magazines_amounts'],
            'firing_mode': row['FiringMode'],
            'rest_bullets': row['rest_bullets']
        }
        owner = str(row['OWNER'])
        for user in users:
            if user['username'] == owner:
                # Check if the 'weapon_list' key exists in the user dictionary
                if 'weapon_list' not in user:
                    user['weapon_list'] = []  # If not, create a new list
                if 'user_type' not in user:
                    user['user_type'] = 'Player'

                # Check if the weapon is already in the user's weapon list
                if weapon not in user['weapon_list']:
                    user['weapon_list'].append(weapon)
                break

    # 将更新后的用户列表保存到 user_list.json 文件中
    with open('user_list.json', 'w') as f:
        json.dump({'user': users}, f)
if __name__ == '__main__':
    syn_weapon_list()
    
    app = QApplication([])
    main_win = MainWin()
    main_win.login_gui_system.show()
    app.exec()