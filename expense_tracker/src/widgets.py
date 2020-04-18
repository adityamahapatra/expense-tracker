from PyQt5 import QtCore, QtGui, QtWidgets

import expense_tracker.src.constants as constants


class MainWidget(QtWidgets.QMainWindow):

    APP_ICON = QtGui.QIcon(constants.CREDIT_CARDS)

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setGeometry(150, 150, 830, 600)
        self.setWindowIcon(self.APP_ICON)
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(self.main_layout)

    def message_box(self, title=None, message=None):
        if message:
            message_box_ = QtWidgets.QMessageBox()
            message_box_.setWindowIcon(self.APP_ICON)
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
