# login_gui_system.py
from PyQt6 import QtWidgets, QtCore, QtGui
from player_loader import PlayerLoader
import qfluentwidgets as qfw
import random
import string

class NullError(Exception):
    def __init__(self, message):
        self.message = message

class LoginWindow(QtCore.QObject):
    login_success = QtCore.pyqtSignal()  # Define a new signal

    def __init__(self):
        super().__init__()  # Call the init method of the super class
        self.player_loader = PlayerLoader()
        self.player_loader.load_players()

    def login(self, username, password):
        if self.player_loader.get_player(username) == password:
            self.login_success.emit()  # Emit the signal when login is successful
            return True
        
        return False

    def register(self, username, password):
            try:
                if not username or not password:
                    raise ValueError("用户名或密码不能为空")
                if len(password) < 6:
                    raise ValueError("密码长度必须至少为6位")
                if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
                    raise ValueError("密码必须包含至少一个数字和一个字母")
                if self.player_loader.get_player(username):
                    return False
                self.player_loader.add_player(username, password)
                return True
            except ValueError as e:
                pass
class RegisterDialog(QtWidgets.QDialog):
    registered = QtCore.pyqtSignal()  # Define a new signal

    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.login_system = LoginWindow()

        self.username_input = qfw.LineEdit(self)
        self.username_input.setPlaceholderText("请输入用户名")
        self.password_input = qfw.PasswordLineEdit(self)
        self.password_input.setPlaceholderText("请输入密码")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.register_button = qfw.PrimaryPushButton('注册', self)
        self.register_button.clicked.connect(self.register)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.register_button)

        self.setLayout(self.layout)
        self.reSize = (800, 350)
        
        # 设置窗口的固定大小
        self.setFixedSize(self.reSize[0], self.reSize[1])
        

    def register(self):
        # 注册用户的方法
        username = self.username_input.text()  # 获取输入的用户名
        password = self.password_input.text()  # 获取输入的密码
        if self.login_system.register(username, password):  # 调用登录系统的注册方法
            QtWidgets.QMessageBox.information(self, 'Register', '注册成功！')  # 弹出注册成功的消息框
            self.registered.emit()  # 当注册成功时发射信号
            self.accept()  # 关闭注册窗口
        else:
            self.register_button.clicked.connect(lambda: self.showErrorMessage('注册失败，用户名已存在！'))
            #QtWidgets.QMessageBox.warning(self, 'Register', '注册失败，用户名已存在！')  # 弹出用户名已存在的警告框

    def showErrorMessage(self,content):
        qfw.TeachingTip.create(
            target=self.register_button,
            icon=qfw.InfoBarIcon.ERROR,
            title='错误！',
            content=str(content),
            isClosable=True,
            tailPosition=qfw.TeachingTipTailPosition.BOTTOM,
            duration=2000,
            parent=self
        )
class LoginGuiSystem(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginGuiSystem, self).__init__(parent)
        self.login_system = LoginWindow()
        
        
        self.setWindowTitle('登录系统')
        self.setObjectName("Login_System")

        self.username_input = qfw.LineEdit(self)
        self.username_input.setMinimumWidth(450)
        self.username_input.setPlaceholderText("请输入用户名")  # 设置提示文字
        self.password_input = qfw.PasswordLineEdit(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setMinimumWidth(450)
        self.password_input.setPlaceholderText("请输入密码")  # 设置提示文字
        
                # 添加验证码输入框
        self.captcha_input = qfw.LineEdit(self)
        self.captcha_input.setMinimumWidth(250)
        self.captcha_input.setPlaceholderText("请输入验证码")

        # 添加验证码按钮
        self.captcha_button = qfw.PrimaryPushButton(self)
        self.captcha_button.clicked.connect(self.generate_captcha)
        self.generate_captcha()  # 生成初始验证码
        
        # 创建一个新的水平布局，并将验证码输入框和验证码按钮添加到这个布局中
        self.captcha_layout = QtWidgets.QHBoxLayout()
        self.captcha_layout.addWidget(self.captcha_input)
        self.captcha_layout.addWidget(self.captcha_button)

        self.login_button = qfw.PrimaryPushButton('登录', self)
        self.login_button.clicked.connect(self.login)

        self.register_button = qfw.PrimaryPushButton('注册', self)
        self.register_button.clicked.connect(self.show_register_dialog)
        
        # 添加退出按钮
        self.exit_button = qfw.PrimaryPushButton('退出', self)  # 创建一个退出按钮
        self.exit_button.clicked.connect(self.exit_program)  # 连接按钮的点击信号和退出函数
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addLayout(self.captcha_layout)  # 将新的水平布局添加到主布局中
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)
        self.layout.addStretch(1)  # 添加一个弹性空间，将退出按钮推到底部
        self.layout.addWidget(self.exit_button)
        self.layout.setSpacing(30)
        self.layout.addWidget(self.captcha_input)
        self.layout.addWidget(self.captcha_button)
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)
        self.reSize = (900, 700)
        
        # 设置窗口的固定大小
        self.setFixedSize(self.reSize[0], self.reSize[1])


    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.login_system.login(username, password):
            QtWidgets.QMessageBox.information(self, '登录', '登录成功！')
        else:
            self.login_button.clicked.connect(lambda: self.showErrorMessage('登录失败，用户名或密码错误！'))
            self.password_input.clear()  # 清空密码输入框
            self.generate_captcha()  # 重新生成验证码
    def showErrorMessage(self,content):
        qfw.TeachingTip.create(
            target=self.register_button,
            icon=qfw.InfoBarIcon.ERROR,
            title='错误！',
            content=str(content),
            isClosable=True,
            tailPosition=qfw.TeachingTipTailPosition.BOTTOM,
            duration=2000,
            parent=self
        )

    def show_register_dialog(self):
        self.register_dialog = RegisterDialog(self)
        self.register_dialog.registered.connect(self.reload_users)  # Connect the signal to the slot
        self.register_dialog.show()
        
    def reload_users(self):
        self.login_system.player_loader.load_players()  # Reload the user list
        
            # 添加退出函数
    def exit_program(self):
        sys.exit()
        
        # 添加生成验证码的函数
    def generate_captcha(self):
        captcha = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        self.captcha_button.setText(captcha)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = LoginGuiSystem()
    main.show()
    sys.exit(app.exec())