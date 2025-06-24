import requests
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

API_URL = "http://localhost:3000"

class LoginWidget(QWidget):
    login_successful = pyqtSignal(str, dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/login_widget.ui", self)  

        # logo
        pixmap = QPixmap("assets/images/logo.png")
        self.logoLabel.setPixmap(pixmap.scaled(200, 200, aspectRatioMode=1))  
        self.logoLabel.setStyleSheet("margin-bottom: 10px;")

        # Event binding
        self.loginButton.clicked.connect(self.attempt_login)
        self.passwordInput.returnPressed.connect(self.attempt_login)

    def attempt_login(self):
        email = self.emailInput.text().strip()
        password = self.passwordInput.text().strip()

        if not email or not password:
            QMessageBox.warning(self, 'Input Kosong', 'Email dan password tidak boleh kosong.')
            return

        try:
            response = requests.post(
                f"{API_URL}/auth/login",
                json={'email': email, 'password': password}
            )
            response.raise_for_status()
            data = response.json()

            token = data.get('token')
            user_data = data.get('user')
            if token and user_data:
                self.login_successful.emit(token, user_data)
            else:
                QMessageBox.warning(self, 'Login Gagal', 'Respons dari server tidak valid.')

        except requests.exceptions.RequestException as e:
            error_message = "Email atau password salah."
            if e.response:
                try:
                    backend_error = e.response.json().get('error')
                    if backend_error:
                        error_message = backend_error
                except Exception:
                    pass
            else:
                error_message = f"Gagal terhubung ke server.\n\n{e}"

            QMessageBox.critical(self, 'Login Error', error_message)
