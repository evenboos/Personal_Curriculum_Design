from PyQt6 import QtWidgets, QtCore, QtGui
import pandas as pd
import sys
import qfluentwidgets as qfw
from PyQt6.QtGui import QIcon
from player_loader import PlayerLoader

class MainWindow(qfw.FluentWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.resize(900, 700)
        self.setWindowTitle("PUBG武器管理系统")
        self.TableEditWidget = Table_Edit_Widget(self)
        self.BulletSumViewWidget = BulletWindow(self)
        self.addSubInterface(self.TableEditWidget, qfw.FluentIcon.FOLDER, '全用户武器管理系统', qfw.NavigationItemPosition.SCROLL)
        self.addSubInterface(BulletWindow(self.BulletSumViewWidget), qfw.FluentIcon.FOLDER, '剩余子弹数', qfw.NavigationItemPosition.SCROLL)

class Table_Edit_Widget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Table_Edit_Widget, self).__init__(parent=parent)
        self.table = qfw.TableView(self)
        self.resize(800, 450)
        self.setWindowTitle('全用户武器管理系统')
        self.setObjectName("TableEditWidget")

        self.setup_table()
        self.setup_buttons()
        self.setup_layout()

    def setup_table(self):
        df = pd.read_excel('your_file.xlsx')
        model = QtGui.QStandardItemModel(self)

        model.setHorizontalHeaderLabels(df.columns)
        for i in df.index:
            count_j = 0
            for j in df.columns:
                item = QtGui.QStandardItem(str(df.at[i, j]))
                model.setItem(i, count_j, item)
                count_j += 1

        self.table.setModel(model)
        self.table.setSortingEnabled(True)
        self.table.verticalHeader().setVisible(False)

    def setup_buttons(self):
        self.button = qfw.PrimaryPushButton(qfw.FluentIcon.SAVE, '提交', self)
        self.button.clicked.connect(self.submit)

        self.add_row_button = qfw.PrimaryPushButton(qfw.FluentIcon.ADD, '添加行', self)
        self.add_row_button.clicked.connect(self.add_row)

        self.exit_button = qfw.PrimaryPushButton(qfw.FluentIcon.CLOSE, '退出', self)
        self.exit_button.clicked.connect(self.exit_program)

    def setup_layout(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.add_row_button)
        self.layout.addWidget(self.exit_button)

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def contextMenuEvent(self, event):
        context_menu = QtWidgets.QMenu(self)
        delete_action = context_menu.addAction("删除行")
        delete_action.triggered.connect(self.delete_row)
        add_action = context_menu.addAction("添加行")
        add_action.triggered.connect(self.add_row)
        context_menu.exec(event.globalPos())

    def delete_row(self):
        current_index = self.table.currentIndex()
        if current_index.isValid():
            self.table.model().removeRow(current_index.row())

    def add_row(self):
        model = self.table.model()
        numbers = [model.item(i, 0).text() for i in range(model.rowCount())]
        numbers = list(map(int, numbers))

        next_number = 1
        while next_number in numbers:
            next_number += 1

        new_row = [QtGui.QStandardItem(str(next_number))] + [QtGui.QStandardItem('') for _ in range(1, model.columnCount())]
        model.appendRow(new_row)

    def submit(self):
        model = self.table.model()

        data = []
        for row in range(model.rowCount()):
            rowData = []
            for column in range(model.columnCount()):
                item = model.item(row, column)
                if item is not None:
                    rowData.append(item.text())
                else:
                    rowData.append('')
            data.append(rowData)

        df = pd.DataFrame(data, columns=[model.horizontalHeaderItem(i).text() for i in range(model.columnCount())])
        df.to_excel('your_file.xlsx', index=False)

    def exit_program(self):
        sys.exit()

class BulletWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.player_loader = PlayerLoader()

        self.table = qfw.TableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["玩家名", "剩余子弹数"])
        self.setObjectName("BulletSumViewWidget")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.table)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setWindowTitle("剩余子弹数查看")
        self.resize(400, 300)

        self.load_data()

    def load_data(self):
        players = self.player_loader.get_all_players()
        self.table.setRowCount(len(players))

        for i, player in enumerate(players):
            bullet_count = sum(weapon.magazines_capacity * weapon.magazines_amounts + weapon.rest_bullets for weapon in player.weapon_list)
            
            name_item = QtWidgets.QTableWidgetItem(player.name)
            name_item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            
            bullet_count_item = QtWidgets.QTableWidgetItem(str(bullet_count))
            bullet_count_item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            
            self.table.setItem(i, 0, name_item)
            self.table.setItem(i, 1, bullet_count_item)
def show_main_window():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    show_main_window()
