from PyQt5 import QtCore, QtGui, QtWidgets

import expense_tracker.src.constants as constants


class MainWidget(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setGeometry(150, 150, 1000, 600)
        self.setFixedSize(1000, 600)
        self.setWindowIcon(QtGui.QIcon(constants.EXPENSES_ICON))
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QtWidgets.QHBoxLayout()
        central_widget.setLayout(self.main_layout)

    @staticmethod
    def message_box(title=None, message=None, icon=None):
        if message:
            message_box_ = QtWidgets.QMessageBox()
            message_box_.setWindowIcon(QtGui.QIcon(constants.EXPENSES_ICON))
            if not icon:
                message_box_.setIcon(QtWidgets.QMessageBox.Warning)
            else:
                message_box_.setIcon(icon)
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
        self.add_icon = QtGui.QIcon(constants.ADD_ICON)
        self.add_expense_action = None
        self.remove_icon = QtGui.QIcon(constants.REMOVE_ICON)
        self.remove_expense_action = None
        self.exit_action = None
        self.currency_action_group = None
        self.rupee_action = None
        self.dollar_action = None
        self.euro_action = None
        self.british_pound_action = None
        self.japanese_yen_action = None
        self.contact_action = None
        self.about_action = None
        self.left_layout = None
        self.right_layout = None
        self.data_entry_layout = None
        self.expense_table_view = None
        self.selection = None
        self.indices = None
        self.category_label = None
        self.custom_category_label = None
        self.custom_category_field = None
        self.price_label = None
        self.price_field = None
        self.notes_label = None
        self.notes_field = None
        self.calender = None
        self.expense_buttons_layout = None
        self.add_button = None
        self.remove_button = None
        self.graph_toggle_button = None
        self.category_list = None
        self.data_visualization_tabs = None
        self.bar_graph_tab = None
        self.bar_graph_icon = QtGui.QIcon(constants.BAR_GRAPH_ICON)
        self.pie_chart_tab = None
        self.pie_chart_icon = QtGui.QIcon(constants.PIE_CHART_ICON)
        self.line_graph_tab = None
        self.line_graph_icon = QtGui.QIcon(constants.LINE_GRAPH_ICON)
        self.context_menu = None
        self.edit_expense_action = None
        self.expense_editor_window = None
        self.about_window = None
        self.categories = [
            "Groceries",
            "Rent",
            "Movies",
            "Restaurants",
            "Liquor",
            "Utilities",
            "Shopping",
            "Services",
            "Education",
            "Investments",
            "Gifts",
            "Travel",
            "Fuel",
            "Medical Expenses",
            "Miscellaneous",
            "Electronics",
            "Furniture",
            "Household Expenses",
            "Pets",
            "Automobile",
        ]


class ExpenseEditorWidget(MainWidget):

    def __init__(self, rows, parent=None):
        super().__init__(parent=parent)
        self.rows = rows
        self.expense_editor_layout = None
        self.edited_data_layout = None
        self.edit_buttons_layout = None
        self.expense_index_label = None
        self.index_spin_box = None
        self.edit_category_label = None
        self.edit_price_label = None
        self.edit_note_label = None
        self.edit_category_field = None
        self.edit_amount_field = None
        self.edit_note_field = None
        self.edit_expense_button = None
        self.cancel_edit_button = None
        self.calender = None
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle("Edit")
        self.setWindowIcon(QtGui.QIcon(constants.EDIT_EXPENSE_WINDOW_ICON))
        self.setGeometry(150, 150, 600, 325)
        self.setFixedSize(600, 325)
        self.center()

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.expense_editor_layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(self.expense_editor_layout)

        self.edited_data_layout = QtWidgets.QGridLayout()
        self.expense_editor_layout.addLayout(self.edited_data_layout)

        self.expense_index_label = QtWidgets.QLabel("Index")
        self.edited_data_layout.addWidget(self.expense_index_label, 0, 0)

        self.edit_category_label = QtWidgets.QLabel("Category")
        self.edited_data_layout.addWidget(self.edit_category_label, 0, 1)

        self.edit_price_label = QtWidgets.QLabel("Amount")
        self.edited_data_layout.addWidget(self.edit_price_label, 0, 2)

        self.edit_note_label = QtWidgets.QLabel("Note")
        self.edited_data_layout.addWidget(self.edit_note_label, 0, 3)

        self.index_spin_box = QtWidgets.QSpinBox()
        self.index_spin_box.setRange(1, self.rows)
        self.edited_data_layout.addWidget(self.index_spin_box, 1, 0)

        self.edit_category_field = QtWidgets.QLineEdit()
        self.edit_category_field.setPlaceholderText("Enter category here")
        self.edited_data_layout.addWidget(self.edit_category_field, 1, 1)

        self.edit_amount_field = QtWidgets.QLineEdit()
        self.edit_amount_field.setPlaceholderText("Enter amount here")
        self.edited_data_layout.addWidget(self.edit_amount_field, 1, 2)

        self.edit_note_field = QtWidgets.QLineEdit()
        self.edit_note_field.setPlaceholderText("Add note here")
        self.edited_data_layout.addWidget(self.edit_note_field, 1, 3)
        self.expense_editor_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 10))

        self.calender = QtWidgets.QCalendarWidget()
        self.expense_editor_layout.addWidget(self.calender)
        self.expense_editor_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 10))

        self.edit_buttons_layout = QtWidgets.QHBoxLayout()
        self.expense_editor_layout.addLayout(self.edit_buttons_layout)

        self.edit_buttons_layout.addSpacing(150)
        self.edit_expense_button = QtWidgets.QPushButton(" Edit")
        self.edit_expense_button.setIcon(QtGui.QIcon(constants.EDIT_BUTTON_ICON))
        self.edit_buttons_layout.addWidget(self.edit_expense_button)
        self.cancel_edit_button = QtWidgets.QPushButton(" Cancel")
        self.cancel_edit_button.setIcon(QtGui.QIcon(constants.CANCEL_ICON))
        self.edit_buttons_layout.addWidget(self.cancel_edit_button)
        self.edit_buttons_layout.addSpacing(150)
        self.expense_editor_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 10))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.close()


class AboutWindow(MainWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.about_window_layout = None
        self.about_image = None
        self.pixmap = None
        self.version_label = None
        self.dev_label = None
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle("About me")
        self.setWindowIcon(QtGui.QIcon(constants.ABOUT_ICON))
        self.setGeometry(150, 150, 400, 200)
        self.setFixedSize(400, 200)
        self.center()

        about_window_central_widget = QtWidgets.QWidget()
        self.setCentralWidget(about_window_central_widget)

        self.about_window_layout = QtWidgets.QVBoxLayout()
        about_window_central_widget.setLayout(self.about_window_layout)

        self.pixmap = QtGui.QPixmap(constants.SPLASH_SCREEN_IMAGE)
        self.about_image = QtWidgets.QLabel()
        self.about_image.setPixmap(self.pixmap)
        self.about_window_layout.addWidget(self.about_image)

        self.version_label = QtWidgets.QLabel()
        version_text = """
            <p style="width:20px;
                      height:20px;
                      color:#708090;
                      font-size:15px;
                      font-family:'Arial';">
                <b>v1.0.0</b>
            </p>
            """
        self.version_label.setText(version_text)
        self.version_label.setAlignment(QtCore.Qt.AlignHCenter)
        self.about_window_layout.addWidget(self.version_label)

        self.dev_label = QtWidgets.QLabel()
        dev_text = """
            <p style="width:20px;
                      height:20px;
                      color:#708090;
                      font-size:15px;
                      font-family:'Ink Free';">
                <b><i>© Aditya Mahapatra</i></b>
            </p>
            """
        self.dev_label.setText(dev_text)
        self.dev_label.setAlignment(QtCore.Qt.AlignHCenter)
        self.about_window_layout.addWidget(self.dev_label)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.close()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.close()
