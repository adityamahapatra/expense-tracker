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
        self.setup_help_menu()
        self.setup_expense_table()
        self.setup_data_feed()

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

    def setup_help_menu(self):
        help_menu = self.menu.addMenu("Help")

        contact_icon = QtGui.QIcon(constants.CONTACT_ICON)
        self.contact_action = QtWidgets.QAction("Contact Me", self)
        self.contact_action.setIcon(contact_icon)
        self.contact_action.setStatusTip("Get in touch with the author")
        help_menu.addAction(self.contact_action)

        about_icon = QtGui.QIcon(constants.ABOUT_ICON)
        self.about_action = QtWidgets.QAction("About", self)
        self.about_action.setIcon(about_icon)
        self.about_action.setStatusTip("Display App Information")
        help_menu.addSeparator()
        help_menu.addAction(self.about_action)

    def setup_expense_table(self):
        self.left_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.left_layout)
        self.expense_table_view = QtWidgets.QTableView()
        self.left_layout.addWidget(self.expense_table_view)
        self.expense_table_view.setAlternatingRowColors(True)
        self.display_expense_data()
        self._set_column_width()

    def _set_column_width(self):
        self.expense_table_view.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch
        )
        self.expense_table_view.horizontalHeader().setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch
        )
        self.expense_table_view.horizontalHeader().setSectionResizeMode(
            2, QtWidgets.QHeaderView.Stretch
        )

    def display_expense_data(self):
        model = QtGui.QStandardItemModel()
        headers = ["Category", "Amount", "Date"]
        indices = [str(i) for i in range(1, 51)]
        model.setHorizontalHeaderLabels(headers)
        model.setVerticalHeaderLabels(indices)
        self.expense_table_view.setModel(model)

    def setup_data_feed(self):
        self.right_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.right_layout)

        self.data_entry_layout = QtWidgets.QGridLayout()
        self.right_layout.addLayout(self.data_entry_layout)
        self.category_label = QtWidgets.QLabel("Category")
        self.category_label.setAlignment(QtCore.Qt.AlignHCenter)
        self.data_entry_layout.addWidget(self.category_label, 0, 0)
        self.custom_category_label = QtWidgets.QLabel("Custom")
        self.custom_category_label.setAlignment(QtCore.Qt.AlignHCenter)
        self.data_entry_layout.addWidget(self.custom_category_label, 0, 1)
        self.category_list = QtWidgets.QComboBox()
        self.category_list.setMinimumWidth(195)
        self.category_list.setStatusTip("Choose from a list of category presets")
        self.category_list.addItems(sorted(self.categories))
        self.data_entry_layout.addWidget(self.category_list, 1, 0)
        self.category_field = QtWidgets.QLineEdit()
        self.category_field.setPlaceholderText("Enter custom category")
        self.category_field.setStatusTip(
            "Enter a custom category not available in the list of presets"
        )
        self.data_entry_layout.addWidget(self.category_field, 1, 1)
        self.price_field = QtWidgets.QLineEdit()
        self.price_field.setPlaceholderText("Enter amount")
        self.price_field.setStatusTip("Enter the expense amount")
        self.right_layout.addWidget(self.price_field)

        self.calender = QtWidgets.QCalendarWidget()
        self.calender.setMaximumHeight(175)
        self.right_layout.addWidget(self.calender)

        self.expense_buttons_layout = QtWidgets.QHBoxLayout()
        self.right_layout.addLayout(self.expense_buttons_layout)
        self.add_button = QtWidgets.QPushButton("Add")
        self.add_button.setStatusTip("Add the expense")
        self.expense_buttons_layout.addWidget(self.add_button)
        self.remove_button = QtWidgets.QPushButton("Remove")
        self.remove_button.setStatusTip("Remove the expense")
        self.expense_buttons_layout.addWidget(self.remove_button)

        self.data_visualization_tabs = QtWidgets.QTabWidget()
        self.right_layout.addWidget(self.data_visualization_tabs)
        self.bar_graph_tab = QtWidgets.QWidget()
        self.pie_chart_tab = QtWidgets.QWidget()
        self.line_graph_tab = QtWidgets.QWidget()
        self.data_visualization_tabs.addTab(self.bar_graph_tab, "Bar Graph")
        self.data_visualization_tabs.addTab(self.pie_chart_tab, "Pie Chart")
        self.data_visualization_tabs.addTab(self.line_graph_tab, "Line Graph")


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
    time.sleep(2)
    window = ExpenseTracker()
    window.setFocus()
    window.show()
    splash_screen.finish(window)
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
