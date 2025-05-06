from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QLabel
)
from PyQt5.QtCore import Qt

class InputDialogView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.resize(500, 200)
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        button_width = 150 

        # Row 1
        self.row1 = QHBoxLayout()
        self.btn_item = QPushButton("Choose from list")
        self.btn_item.setFixedWidth(button_width)
        self.le = QLineEdit()
        self.le.setMinimumWidth(250)
        self.row1.addWidget(self.btn_item)
        self.row1.addWidget(self.le)

        # Row 2
        self.row2 = QHBoxLayout()
        self.btn_text = QPushButton("get name")
        self.btn_text.setFixedWidth(button_width)
        self.le1 = QLineEdit()
        self.le1.setMinimumWidth(250)
        self.row2.addWidget(self.btn_text)
        self.row2.addWidget(self.le1)

        # Row 3
        self.row3 = QHBoxLayout()
        self.btn_int = QPushButton("Enter an integer")
        self.btn_int.setFixedWidth(button_width)
        self.le2 = QLineEdit()
        self.le2.setMinimumWidth(250)
        self.row3.addWidget(self.btn_int)
        self.row3.addWidget(self.le2)

        # Label
        self.name_label = QLabel("Muhammad Rizki Assamsuli | F1D022146")
        self.name_label.setAlignment(Qt.AlignLeft)

        # Add layouts
        self.main_layout.addLayout(self.row1)
        self.main_layout.addLayout(self.row2)
        self.main_layout.addLayout(self.row3)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.name_label)
        self.setLayout(self.main_layout)
