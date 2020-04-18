from PyQt5 import QtCore, QtGui, QtWidgets

import expense_tracker.src.constants as constants


class MainWidget(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setGeometry(150, 150, 800, 600)
        self.setWindowIcon(QtGui.QIcon(constants.EXPENSES_ICON))
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QtWidgets.QGridLayout()
        central_widget.setLayout(self.main_layout)

    @staticmethod
    def message_box(title=None, message=None):
        if message:
            message_box_ = QtWidgets.QMessageBox()
            message_box_.setWindowIcon(QtGui.QIcon(constants.EXPENSES_ICON))
            message_box_.setIcon(QtWidgets.QMessageBox.Warning)
            if not title:
                message_box_.setWindowTitle('Info')
            else:
                message_box_.setWindowTitle(title)
            message_box_.setText(message)
            message_box_.exec_()

    def confirm_box(self, title=None, msg=None):
        choice = QtWidgets.QMessageBox.question(
            self, title, msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        return True if choice == QtWidgets.QMessageBox.Yes else False

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        confirmation = self.confirm_box(
            title="Exit", msg="Are you sure you wish to exit the app?"
        )
        if not confirmation:
            event.ignore()
        else:
            event.accept()

    def center(self):
        frame_geometry = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(
            QtWidgets.QApplication.desktop().cursor().pos()
        )
        center_point = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())


class TrackerWidget(MainWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.menu = self.menuBar()
        self.status = self.statusBar()
        self.add_expense_action = None
        self.remove_expense_action = None
        self.exit_action = None
        self.rupee_action = None
        self.dollar_action = None
        self.euro_action = None
        self.british_pound_action = None
        self.japanese_yen_action = None
        self.contact_action = None
        self.about_action = None
        self.expense_table_view = None
