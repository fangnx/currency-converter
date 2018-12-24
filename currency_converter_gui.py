from PyQt5.QtCore import Qt, pyqtSlot, QFile, QIODevice
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton,
                             QLineEdit, QGridLayout,QListWidget, QListWidgetItem)
from PyQt5.QtGui import QDoubleValidator

import sys
from get_rates import get_all_curr_types
from convert_currency import convert_real_time, to_short_name


class MyWindow(QWidget):

    def __init__(self):

        super().__init__()

        try:
            f = open("./style.css")
            self.setStyleSheet(f.read())

        except IOError:
            print("Exception: No stylesheet file found.")

        self.resize(600, 400)
        self.move(200, 150)
        self.setWindowTitle("Currency Converter 💰")
        self.base_currency = None
        self.target_currency = None
        self.amount = 0

        from_label = QLabel("From:")
        to_label = QLabel("To:")
        amount_label = QLabel("Amount")

        self.from_line = QListWidget()
        self.from_line.setSelectionMode(QListWidget.SingleSelection)
        curr_type_list = get_all_curr_types()
        for t in curr_type_list:
            self.from_line.addItem(t[1])

        self.from_line.itemSelectionChanged.connect(self.base_currency_selected)

        self.to_line = QListWidget()
        self.to_line.setSelectionMode(QListWidget.SingleSelection)
        curr_type_list = get_all_curr_types()
        for t in curr_type_list:
            self.to_line.addItem(t[1])

        self.to_line.itemSelectionChanged.connect(self.target_currency_selected)

        self.amount_line = QLineEdit()
        self.amount_line.setValidator(QDoubleValidator())
        self.amount_line.setAlignment(Qt.AlignRight)

        button_enter = QPushButton("Enter", self)
        button_enter.clicked.connect(self.on_click_enter)

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(from_label, 0, 0)
        grid.addWidget(self.from_line, 0, 1)

        grid.addWidget(to_label, 0, 2)
        grid.addWidget(self.to_line, 0, 3)

        grid.addWidget(amount_label, 1, 0)
        grid.addWidget(self.amount_line, 1, 1)

        grid.addWidget(button_enter, 2, 1)

        self.setLayout(grid)
        self.show()


    def base_currency_selected(self):
        self.base_currency = to_short_name(self.from_line.currentItem().text())


    def target_currency_selected(self):
        self.target_currency = to_short_name(self.to_line.currentItem().text())


    @pyqtSlot()
    def on_click_enter(self):
        print(self.base_currency)
        print(self.target_currency)

        out = convert_real_time(self.base_currency, self.target_currency,
                                float(self.amount_line.text()))
        print(out)


    def key_press_handler(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


def show_app():

    app = QApplication(sys.argv)
    w = MyWindow()

    # QLabel(w).setText("<p style='color: blue; margin-left: 20px; margin-right: 20px> </p>")

    sys.exit(app.exec())


if __name__ == "__main__":
    show_app()