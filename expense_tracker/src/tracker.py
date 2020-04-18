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

    def connections(self):
        pass

    def setup_file_menu(self):
        file_menu = self.menu.addMenu("File")

        add_icon = QtGui.QIcon(constants.ADD_ICON)
        add_expense_action = QtWidgets.QAction("Add Expense", self)
        add_expense_action.setIcon(add_icon)
        add_expense_action.setStatusTip("Add a new expense")
        add_expense_action.setShortcut("Ctrl+A")
        file_menu.addAction(add_expense_action)

        remove_icon = QtGui.QIcon(constants.REMOVE_ICON)
        remove_expense_action = QtWidgets.QAction("Remove Expense", self)
        remove_expense_action.setIcon(remove_icon)
        remove_expense_action.setStatusTip("Remove an existing expense")
        remove_expense_action.setShortcut("Ctrl+R")
        file_menu.addAction(remove_expense_action)

        exit_icon = QtGui.QIcon(constants.EXIT_ICON)
        exit_action = QtWidgets.QAction("Exit", self)
        exit_action.setIcon(exit_icon)
        exit_action.setStatusTip("Exit the application")
        exit_action.setShortcut("Ctrl+Q")
        file_menu.addSeparator()
        file_menu.addAction(exit_action)


def main():
    application = QtWidgets.QApplication(sys.argv)
    application.setStyle("Plastique")
    window = ExpenseTracker()
    window.setFocus()
    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
