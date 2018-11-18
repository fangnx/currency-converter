from PyQt5.QtCore import Qt, pyqtSlot, QFile, QIODevice
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QLineEdit, QGridLayout)
from PyQt5.QtGui import QIntValidator, QDoubleValidator

import sys
import get_rates


class MyWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.init_UI()

        try:
            f = open("./style.css")
            self.setStyleSheet(f.read())

        except IOError:
            print("Exception: No stylesheet file found.")


    def init_UI(self):

        self.resize(400, 300)
        self.move(200, 150)
        self.setWindowTitle("Simple Currency Rates 💰")

        label_og_amount = QLabel("Amount of RMB")
        curr_type_label = QLabel("Type of Target Currency")
        target_amount_label = QLabel("Amount of Target Currency")

        line_og_amount = QLineEdit()
        line_og_amount.setValidator(QDoubleValidator())
        line_og_amount.setAlignment(Qt.AlignRight)

        curr_type_edit = QLineEdit()
        target_amount_edit = QLineEdit()

        btn_enter = QPushButton("Enter", self)
        btn_enter.clicked.connect(self.on_click_enter)

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(label_og_amount, 0, 0)
        grid.addWidget(line_og_amount, 0, 1)

        grid.addWidget(curr_type_label, 1, 0)
        grid.addWidget(curr_type_edit, 1, 1)

        grid.addWidget(target_amount_label, 2, 0)
        grid.addWidget(target_amount_edit, 2, 1)

        grid.addWidget(btn_enter, 3, 1)

        self.setLayout(grid)

        self.show()


    @pyqtSlot()
    def on_click_enter(self):
        print("a")


    def key_press_handler(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()






def show_app():
    app = QApplication(sys.argv)
    w = MyWindow()

    QLabel(w).setText("<p style='color: blue; margin-left: 20px; margin-right: 20px>" + get_rates.to_string(get_rates.get_all_rates(), "CAD") + "</p>")

    sys.exit(app.exec())


if __name__ == "__main__":
    show_app()