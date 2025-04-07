import sys
import re
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from form_ui import FormUI  

class FormValidationApp(FormUI):
    def __init__(self):
        super().__init__()
        self.save_button.clicked.connect(self.validate_form)
        self.clear_button.clicked.connect(self.clear_fields)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()

    def validate_form(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.toPlainText().strip()
        gender = self.gender_input.currentText()
        education = self.education_input.currentText()

        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not name:
            self.show_warning("Name is required.")
        elif not re.match(email_regex, email):
            self.show_warning("Invalid email format.")
        elif not age.isdigit():
            self.show_warning("Age must be numeric.")
        elif not (17 <= int(age) <= 60):
            self.show_warning("Age must be between 17 and 60.")
        elif len(phone.replace(" ", "").replace("+", "")) != 13:
            self.show_warning("Phone number must be 13 digits.")
        elif not address:
            self.show_warning("Address is required.")
        elif gender == "-- Select Gender --":
            self.show_warning("Please select a gender.")
        elif education == "-- Select Education --":
            self.show_warning("Please select education level.")
        else:
            self.show_success("Data saved successfully!")
            self.clear_fields()

    def show_warning(self, message):
        QMessageBox.warning(self, "Validation Error", message)

    def show_success(self, message):
        QMessageBox.information(self, "Success", message)

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_input.setCurrentIndex(0)
        self.education_input.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
