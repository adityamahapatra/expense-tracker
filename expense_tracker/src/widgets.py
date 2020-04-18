from PyQt5 import QtCore, QtGui, QtWidgets

import expense_tracker.src.constants as constants


class MainWidget(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setGeometry(150, 150, 800, 600)
        self.setWindowIcon(QtGui.QIcon(constants.CREDIT_CARDS))
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QtWidgets.QGridLayout()
        central_widget.setLayout(self.main_layout)

    @staticmethod
    def message_box(title=None, message=None):
        if message:
            message_box_ = QtWidgets.QMessageBox()
            message_box_.setWindowIcon(QtGui.QIcon(constants.CREDIT_CARDS))
            message_box_.setIcon(QtWidgets.QMessageBox.Warning)
            if not title:
                message_box_.setWindowTitle('Info')
            else:
                message_box_.setWindowTitle(title)
            message_box_.setText(message)
            message_box_.exec_()

    # noinspection PyTypeChecker,PyCallByClass
    def confirm_box(self, title=None, msg=None):
        choice = QtWidgets.QMessageBox.question(
            self, title, msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        return True if choice == QtWidgets.QMessageBox.Yes else False

    # noinspection PyArgumentList
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
