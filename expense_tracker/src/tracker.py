import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import expense_tracker.src.constants as constants
from expense_tracker.src.widgets import TrackerWidget


class ExpenseTracker(TrackerWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()
        self.connections()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def initUI(self):
        self.setWindowTitle("Expense Tracker")
        self.center()
        self.setup_file_menu()

    # noinspection PyTypeChecker
    def connections(self):
        self.exit_action.triggered.connect(self.close)

    def setup_file_menu(self):
        file_menu = self.menu.addMenu("File")

        add_icon = QtGui.QIcon(constants.ADD_ICON)
        self.add_expense_action = QtWidgets.QAction("Add Expense", self)
        self.add_expense_action.setIcon(add_icon)
        self.add_expense_action.setStatusTip("Add a new expense")
        self.add_expense_action.setShortcut("Ctrl+A")
        file_menu.addAction(self.add_expense_action)

        remove_icon = QtGui.QIcon(constants.REMOVE_ICON)
        self.remove_expense_action = QtWidgets.QAction("Remove Expense", self)
        self.remove_expense_action.setIcon(remove_icon)
        self.remove_expense_action.setStatusTip("Remove an existing expense")
        self.remove_expense_action.setShortcut("Ctrl+R")
        file_menu.addAction(self.remove_expense_action)

        exit_icon = QtGui.QIcon(constants.EXIT_ICON)
        self.exit_action = QtWidgets.QAction("Exit", self)
        self.exit_action.setIcon(exit_icon)
        self.exit_action.setStatusTip("Exit the application")
        self.exit_action.setShortcut("Ctrl+Q")
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)


def main():
    application = QtWidgets.QApplication(sys.argv)
    application.setStyle("Plastique")
    window = ExpenseTracker()
    window.setFocus()
    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
