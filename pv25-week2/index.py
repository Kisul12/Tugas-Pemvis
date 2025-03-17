from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QRadioButton, QPushButton, QComboBox, QGroupBox
)
import sys
class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        
        main_layout = QVBoxLayout()
        
        identity_group = QGroupBox("Identitas (vertical box layout)")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Muhammad Rizki Assamsuli"))
        identity_layout.addWidget(QLabel("NIM : F1D022146"))
        identity_layout.addWidget(QLabel("Kelas : C"))
        identity_group.setLayout(identity_layout)
        
        nav_group = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        
        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()
        form_layout.addRow("Full Name:", QLineEdit())
        form_layout.addRow("Email:", QLineEdit())
        form_layout.addRow("Phone:", QLineEdit())
        
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QRadioButton("Male"))
        gender_layout.addWidget(QRadioButton("Female"))
        form_layout.addRow("Gender:", gender_layout)
        
        country_combo = QComboBox()
        country_combo.addItems(["Select", "USA", "UK", "Germany", "Japan"])
        form_layout.addRow("Country:", country_combo)
        
        form_group.setLayout(form_layout)
        
        action_group = QGroupBox("Actions (horizontal box layout)")
        action_layout = QHBoxLayout()
        action_layout.addWidget(QPushButton("Submit"))
        action_layout.addWidget(QPushButton("Cancel"))
        action_group.setLayout(action_layout)
        
        main_layout.addWidget(identity_group)
        main_layout.addWidget(nav_group)
        main_layout.addWidget(form_group)
        main_layout.addWidget(action_group)
        
        self.setLayout(main_layout)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())