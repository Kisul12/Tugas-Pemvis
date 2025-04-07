from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QFormLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt

class FormUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation")
        self.setGeometry(100, 100, 400, 400)
        self.initUI()

    def initUI(self):
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        form_layout.addRow("Name:", self.name_input)

        self.email_input = QLineEdit()
        form_layout.addRow("Email:", self.email_input)

        self.age_input = QLineEdit()
        form_layout.addRow("Age:", self.age_input)

        self.phone_input = QLineEdit()
        self.phone_input.setInputMask("+62000 0000 0000")
        form_layout.addRow("Phone Number:", self.phone_input)

        self.address_input = QTextEdit()
        form_layout.addRow("Address:", self.address_input)

        self.gender_input = QComboBox()
        self.gender_input.addItems(["-- Select Gender --", "Male", "Female", "Other"])
        form_layout.addRow("Gender:", self.gender_input)

        self.education_input = QComboBox()
        self.education_input.addItems(["-- Select Education --", "High School", "Diploma", "Bachelor", "Master"])
        form_layout.addRow("Education:", self.education_input)

        self.save_button = QPushButton("Save")
        self.clear_button = QPushButton("Clear")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)

        self.watermark = QLabel("F1D022146 | Muhammad Rizki Assamsuli")
        self.watermark.setAlignment(Qt.AlignCenter)
        self.watermark.setStyleSheet("color: gray; font-size: 10px;")

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addWidget(self.watermark)

        self.setLayout(main_layout)
