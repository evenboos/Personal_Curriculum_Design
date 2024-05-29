# login_gui_system.py
from PyQt6 import QtWidgets, QtCore, QtGui
from player_loader import PlayerLoader
import qfluentwidgets as qfw
class LoginWindow(QtCore.QObject):
    login_success = QtCore.pyqtSignal()  # Define a new signal

    def __init__(self):
        super().__init__()  # Call the init method of the super class
        self.player_loader = PlayerLoader()
        self.player_loader.load_players()
        self.reSize = (900, 700)

    def login(self, username, password):
        if self.player_loader.get_player(username) == password:
            self.login_success.emit()  # Emit the signal when login is successful
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
        self.login_system = LoginWindow()

        self.username_input = qfw.LineEdit(self)
        self.username_input.setPlaceholderText("example")
        self.password_input = qfw.PasswordLineEdit(self)
        self.password_input.setPlaceholderText("12345678")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.register_button = qfw.PrimaryPushButton('注册', self)
        self.register_button.clicked.connect(self.register)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.register_button)

        #self.setLayout(self.layout)
        self.reSize = (900, 700)

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

class LoginGuiSystem(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginGuiSystem, self).__init__(parent)
        self.login_system = LoginWindow()
        
        self.setWindowTitle('登录系统')
        self.setObjectName("Login_System")

        self.username_input = qfw.LineEdit(self)
        self.password_input = qfw.PasswordLineEdit(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.login_button = qfw.PrimaryPushButton('Login', self)
        self.login_button.clicked.connect(self.login)

        self.register_button = qfw.PrimaryPushButton('Register', self)
        self.register_button.clicked.connect(self.show_register_dialog)
        
        # 添加退出按钮
        self.exit_button = qfw.PrimaryPushButton('退出', self)  # 创建一个退出按钮
        self.exit_button.clicked.connect(self.exit_program)  # 连接按钮的点击信号和退出函数
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)
        self.layout.addStretch(1)  # 添加一个弹性空间，将退出按钮推到底部
        self.layout.addWidget(self.exit_button)
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)
        self.reSize = (900, 700)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.login_system.login(username, password):
            QtWidgets.QMessageBox.information(self, 'Login', '登录成功！')
        else:
            QtWidgets.QMessageBox.warning(self, 'Login', '登录失败，账号或密码不正确！')

    def show_register_dialog(self):
        self.register_dialog = RegisterDialog(self)
        self.register_dialog.registered.connect(self.reload_users)  # Connect the signal to the slot
        self.register_dialog.show()
        
    def reload_users(self):
        self.login_system.player_loader.load_players()  # Reload the user list
        
            # 添加退出函数
    def exit_program(self):
        sys.exit()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = LoginGuiSystem()
    main.show()
    sys.exit(app.exec())