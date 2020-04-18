import sys
import time

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
        self.setWindowTitle("Expense Jar")
        self.center()
        self.setup_file_menu()
        self.setup_currency_menu()

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

    def setup_currency_menu(self):
        currency_menu = self.menu.addMenu("Currency")

        rupee_icon = QtGui.QIcon(constants.RUPEE_ICON)
        self.rupee_action = QtWidgets.QAction("Rupee", self)
        self.rupee_action.setIcon(rupee_icon)
        self.rupee_action.setStatusTip("Rupee")
        currency_menu.addAction(self.rupee_action)

        dollar_icon = QtGui.QIcon(constants.DOLLAR_ICON)
        self.dollar_action = QtWidgets.QAction("Dollar", self)
        self.dollar_action.setIcon(dollar_icon)
        self.dollar_action.setStatusTip("Dollar")
        currency_menu.addAction(self.dollar_action)

        euro_icon = QtGui.QIcon(constants.EURO_ICON)
        self.euro_action = QtWidgets.QAction("Euro", self)
        self.euro_action.setIcon(euro_icon)
        self.euro_action.setStatusTip("Euro")
        currency_menu.addAction(self.euro_action)

        british_pound_icon = QtGui.QIcon(constants.BRITISH_POUND_ICON)
        self.british_pound_action = QtWidgets.QAction("British Pound", self)
        self.british_pound_action.setIcon(british_pound_icon)
        self.british_pound_action.setStatusTip("British Pound")
        currency_menu.addAction(self.british_pound_action)

        japanese_yen_icon = QtGui.QIcon(constants.JAPANESE_YEN_ICON)
        self.japanese_yen_action = QtWidgets.QAction("Japanese Yen", self)
        self.japanese_yen_action.setIcon(japanese_yen_icon)
        self.japanese_yen_action.setStatusTip("Japanese Yen")
        currency_menu.addAction(self.japanese_yen_action)


def main():
    application = QtWidgets.QApplication(sys.argv)
    application.setStyle("Plastique")
    pixmap = QtGui.QPixmap(constants.SPLASH_SCREEN_IMAGE)
    splash_screen = QtWidgets.QSplashScreen(pixmap)
    splash_screen.show()
    message = """
    <p style="width:20px;
              height:20px;
              color:silver;
              font-size:10px;
              font-family:'Ink Free';">
        <b><i>- Aditya Mahapatra</i></b>
    </p>
    """
    splash_screen.showMessage(
        message, alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom,
    )
    time.sleep(4)
    window = ExpenseTracker()
    window.setFocus()
    window.show()
    splash_screen.finish(window)
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
