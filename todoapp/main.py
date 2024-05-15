from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QPlainTextEdit, QListWidget, QStackedWidget, \
    QListWidgetItem, QDesktopWidget
from PyQt5 import uic
import sys
import sqlite3
import res
from dbManager import DBManager


class TODOAPP(QMainWindow):
    def __init__(self):
        super(TODOAPP, self).__init__()

        uic.loadUi('design.ui', self)
        self.setWindowTitle('TODO APP')
        self.setFixedSize(380, 520)
        self.center()
        self.stackedWidget.setCurrentIndex(0)

        self.dbManger = DBManager("database.db")

        self.load_todos()

        self.listWidget.itemClicked.connect(self.task_checked)
        self.addTaskButton.clicked.connect(self.add_task_clicked)
        self.confirmButton.clicked.connect(self.confirm_clicked)
        self.cancelButton.clicked.connect(self.cancel_clicked)

        self.show()

    def load_todos(self):
        self.listWidget.clear()
        tasks = self.dbManger.get_tasks()

        for task in tasks:
            item = QListWidgetItem(task[0])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            if task[1] == 2:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            self.listWidget.addItem(item)

    def task_checked(self, item):
        self.dbManger.checked_is_changed(item.text(), item.checkState())

    def add_task_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def confirm_clicked(self):
        # Print info that task is added
        task_name = self.taskNameTextEdit.toPlainText()
        self.dbManger.add_task(task_name)
        self.taskNameTextEdit.clear()
        self.stackedWidget.setCurrentIndex(0)
        self.load_todos()

    def cancel_clicked(self):
        self.taskNameTextEdit.clear()
        self.stackedWidget.setCurrentIndex(0)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIWindow = TODOAPP()
    app.exec_()
