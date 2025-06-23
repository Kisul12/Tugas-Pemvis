# File: main.py

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget, QStatusBar,
    QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QMenuBar, QAction
)
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt

from login_widget import LoginWidget
from dashboard_widget import DashboardWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SadarKulit - Final Project [Pemrograman Visual]")
        self.setGeometry(100, 100, 1000, 700)

        # === Menu Bar ===
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        export_action = QAction("📤 Export CSV", self)
        export_action.setShortcut("Ctrl+E")
        export_action.triggered.connect(lambda: self.dashboard_page.export_to_csv())

        logout_action = QAction("🚪 Logout", self)
        logout_action.setShortcut("Ctrl+L")
        logout_action.triggered.connect(self.logout)

        exit_action = QAction("❌ Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(export_action)
        file_menu.addAction(logout_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        help_menu = menubar.addMenu("Help")
        about_action = QAction("Tentang Aplikasi", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

        # === Central Widget ===
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # --- Sidebar kiri ---
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout()
        self.sidebar.setLayout(self.sidebar_layout)
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("background-color: #f0f0f0;")

        self.export_button = QPushButton("📤 Export CSV")
        self.logout_button = QPushButton("🚪 Logout")
        self.export_button.setEnabled(False)
        self.logout_button.setEnabled(False)

        self.sidebar_layout.addWidget(self.export_button)
        self.sidebar_layout.addWidget(self.logout_button)
        self.sidebar_layout.addStretch()

        # --- Halaman utama ---
        self.pages = QStackedWidget()
        self.login_page = LoginWidget()
        self.dashboard_page = DashboardWidget()
        self.pages.addWidget(self.login_page)
        self.pages.addWidget(self.dashboard_page)

        # Layout utama
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.pages)
        self.central_widget.setLayout(self.main_layout)

        # Status bar
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Selamat datang! Silakan login.")

        # Sinyal
        self.login_page.login_successful.connect(self.show_dashboard)
        self.logout_button.clicked.connect(self.logout)
        self.export_button.clicked.connect(self.dashboard_page.export_to_csv)

        # Sembunyikan sidebar di awal
        self.sidebar.hide()
        self.pages.setCurrentWidget(self.login_page)

        # Style umum
        common_button_style = """
            QPushButton {
                padding: 10px;
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d0e8ff;
                border: 1px solid #66b3ff;
            }
            QPushButton:disabled {
                color: #999999;
                background-color: #f0f0f0;
            }
        """

        logout_button_style = """
            QPushButton {
                padding: 10px;
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 5px;
                font-weight: bold;
                color: #aa0000;
            }
            QPushButton:hover {
                background-color: #ffaaaa;
                border: 1px solid #ff0000;
            }
            QPushButton:disabled {
                color: #999999;
                background-color: #f0f0f0;
            }
        """

        self.export_button.setStyleSheet(common_button_style)
        self.logout_button.setStyleSheet(logout_button_style)

    def show_dashboard(self, token, user_data):
        nama_mahasiswa = "Muhammad Rizki Assamsuli | F1D022146"
        user_name = user_data.get("name", "User")
        self.statusBar().showMessage(f"Project oleh: {nama_mahasiswa} | Login sebagai: {user_name}")

        self.dashboard_page.set_token_and_load_data(token)

        self.export_button.setEnabled(True)
        self.logout_button.setEnabled(True)

        self.sidebar.show()
        self.pages.setCurrentWidget(self.dashboard_page)

    def logout(self):
        confirm = QMessageBox.question(
            self, "Logout", "Apakah Anda yakin ingin logout?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            self.statusBar().showMessage("Silakan login kembali.")
            self.export_button.setEnabled(False)
            self.logout_button.setEnabled(False)
            self.sidebar.hide()
            self.pages.setCurrentWidget(self.login_page)

    def show_about_dialog(self):
        QMessageBox.information(
            self, "Tentang Aplikasi",
            "Aplikasi SadarKulit\n\nDibuat oleh Muhammad Rizki Assamsuli (F1D022146)\n"
            "Final Project Pemrograman Visual - Semester Genap 2024/2025.\n\n"
            "Fitur: Login, Prediksi Gambar Kulit, Riwayat Prediksi, Export CSV."
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)

    font_id = QFontDatabase.addApplicationFont("assets/fonts/Poppins-Regular.ttf")
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        app.setFont(QFont(font_family, 10))
    else:
        print("⚠️ Gagal memuat font Poppins.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
