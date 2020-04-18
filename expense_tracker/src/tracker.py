import sys

from PyQt5 import QtCore, QtWidgets

from expense_tracker.src.widgets import TrackerWidget


class ExpenseTracker(TrackerWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def initUI(self):
        self.setWindowTitle("Expense Tracker")
        self.center()


def main():
    application = QtWidgets.QApplication(sys.argv)
    application.setStyle("Plastique")
    window = ExpenseTracker()
    window.setFocus()
    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
