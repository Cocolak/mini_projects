from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QPlainTextEdit, QListWidget, QStackedWidget, \
    QListWidgetItem
from PyQt5 import uic
import sys
import res


class TODOAPP(QMainWindow):
    def __init__(self):
        super(TODOAPP, self).__init__()

        uic.loadUi('design.ui', self)
        self.setWindowTitle('TODO APP')

        self.stacked_widget = self.findChild(QStackedWidget, "stackedWidget")
        self.stacked_widget.setCurrentIndex(1)

        todos = ["Task Name", "Task Name", "Task Name", "Task Name", "Task Name", "Task Name", "Task Name"]

        for todo in todos:
            item = QListWidgetItem(todo)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.listWidget.addItem(item)

        self.show()


app = QApplication(sys.argv)
UIWindow = TODOAPP()
app.exec_()