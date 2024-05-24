# login_gui_system.py
from PyQt6 import QtWidgets, QtCore, QtGui
from player_loader import PlayerLoader

class LoginSystem:
    def __init__(self):
        self.player_loader = PlayerLoader()
        self.player_loader.load_players()

    def login(self, username, password):
        if self.player_loader.get_player(username) == password:
            return True
        return False

    def register(self, username, password):
        if self.player_loader.get_player(username) is None:
            self.player_loader.add_player(username, password)
            return True
        return False

class RegisterDialog(QtWidgets.QDialog):
    registered = QtCore.pyqtSignal()  # Define a new signal

    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.login_system = LoginSystem()

        self.username_input = QtWidgets.QLineEdit(self)
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.register_button = QtWidgets.QPushButton('Register', self)
        self.register_button.clicked.connect(self.register)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.register_button)

        self.setLayout(self.layout)

    def register(self):
        # 注册用户的方法
        username = self.username_input.text()  # 获取输入的用户名
        password = self.password_input.text()  # 获取输入的密码
        if self.login_system.register(username, password):  # 调用登录系统的注册方法
            QtWidgets.QMessageBox.information(self, 'Register', 'Registration successful.')  # 弹出注册成功的消息框
            self.registered.emit()  # 当注册成功时发射信号
            self.accept()  # 关闭注册窗口
        else:
            QtWidgets.QMessageBox.warning(self, 'Register', 'Registration failed.')  # 弹出注册失败的消息框

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.login_system = LoginSystem()

        self.username_input = QtWidgets.QLineEdit(self)
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.login_button = QtWidgets.QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)

        self.register_button = QtWidgets.QPushButton('Register', self)
        self.register_button.clicked.connect(self.show_register_dialog)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.login_system.login(username, password):
            QtWidgets.QMessageBox.information(self, 'Login', 'Login successful.')
        else:
            QtWidgets.QMessageBox.warning(self, 'Login', 'Login failed.')

    def show_register_dialog(self):
        self.register_dialog = RegisterDialog(self)
        self.register_dialog.registered.connect(self.reload_users)  # Connect the signal to the slot
        self.register_dialog.show()
        
    def reload_users(self):
        self.login_system.player_loader.load_players()  # Reload the user list


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())