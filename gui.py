
# 导入所需的模块
from PyQt6 import QtWidgets, QtCore, QtGui  # PyQt6模块用于创建GUI应用程序
import pandas as pd  # 用于数据处理的模块
import sys

# 创建主窗口类
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):  # 初始化方法
        super(MainWindow, self).__init__(parent)  # 调用父类的初始化方法
        self.table = QtWidgets.QTableView(self)  # 创建表视图部件

        # 读取Excel文件并创建数据模型
        df = pd.read_excel('your_file.xlsx')  # 从Excel文件中读取数据
        model = QtGui.QStandardItemModel(self)  # 创建Qt的标准项数据模型

        model.setHorizontalHeaderLabels(df.columns)  # 设置数据模型的水平标题标签
        for i in df.index:  # 遍历数据框的行索引
            count_j = 0  # 计数器，用于设置列索引
            for j in df.columns:  # 遍历数据框的列标签
                item = QtGui.QStandardItem(str(df.at[i, j]))  # 创建Qt标准项对象
                model.setItem(i, count_j, item)  # 在数据模型中设置项的值
                count_j += 1  # 计数器加1

        self.table.setModel(model)  # 将数据模型应用到表视图
        self.table.setSortingEnabled(True)  #启用表格排序

        self.button = QtWidgets.QPushButton('Submit', self)  # 创建按钮部件
        self.button.clicked.connect(self.submit)  # 连接按钮的点击事件到submit方法

        self.layout = QtWidgets.QVBoxLayout()  # 创建垂直布局管理器
        self.layout.addWidget(self.table)  # 将表视图部件添加到布局
        self.layout.addWidget(self.button)  # 将按钮部件添加到布局

        self.widget = QtWidgets.QWidget()  # 创建部件
        self.widget.setLayout(self.layout)  # 将布局应用到部件
        # 设置表格的垂直表头不可见
        self.table.verticalHeader().setVisible(False)

        self.setCentralWidget(self.widget)  # 设置中心部件为自定义部件

    def submit(self):  # 提交数据的方法
        model = self.table.model()  # 获取表视图的数据模型
        

        data = []  # 创建一个空的数据列表
        for row in range(model.rowCount()):  # 遍历数据模型的行
            rowData = []  # 创建一个空的行数据列表
            for column in range(model.columnCount()):  # 遍历数据模型的列
                item = model.item(row, column)  # 获取特定位置的项
                if item is not None:  # 如果项不为空
                    rowData.append(item.text())  # 将项的文本值添加到行数据列表
                else:
                    rowData.append('')  # 否则在行数据列表中添加空字符串
            data.append(rowData)  # 将行数据列表添加到数据列表

        df = pd.DataFrame(data, columns=[model.horizontalHeaderItem(i).text() for i in range(model.columnCount())])  # 创建数据框
        df.to_excel('your_file.xlsx', index=False)  # 将数据框写入Excel文件

def show_main_window():
    app = QtWidgets.QApplication(sys.argv)  # 创建Qt应用程序对象
    main = MainWindow()  # 创建主窗口对象
    main.show()  # 显示主窗口
    sys.exit(app.exec())  # 运行应用程序并进入主事件循环
    
if __name__ == '__main__':  # 程序执行入口
    import sys  # 导入sys模块
    app = QtWidgets.QApplication(sys.argv)  # 创建Qt应用程序对象
    main = MainWindow()  # 创建主窗口对象
    main.show()  # 显示主窗口
    sys.exit(app.exec())  # 运行应用程序并进入主事件循环