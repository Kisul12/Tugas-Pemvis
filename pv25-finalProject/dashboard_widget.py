import requests
import csv
import mimetypes
import os
import re
from datetime import datetime, timezone, timedelta

from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton,
    QVBoxLayout, QHeaderView, QFileDialog, QMessageBox, QLabel
)
from PyQt5.QtCore import Qt

API_URL = "http://localhost:3000"

def bersihkan_nama_penyakit(nama):
    if not nama:
        return "Tidak diketahui"
    nama = re.sub(r'^\d+\.\s*', '', nama)          # Hapus angka & titik di awal
    nama = re.sub(r'\s*[-–]?\s*\d{3,}$', '', nama) # Hapus angka di akhir
    return nama.strip()

class DashboardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.auth_token = None
        self.api_headers = {}
        self.history_data = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("Riwayat Prediksi Penyakit Kulit")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        self.history_table = QTableWidget()
        self.history_table.setMinimumHeight(300)
        self.history_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.history_table.setSortingEnabled(True)

        self.predict_button = QPushButton("🩺 Lakukan Prediksi Baru")
        self.predict_button.setStyleSheet("""
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 5px;
        """)

        layout.addWidget(self.history_table)
        layout.addWidget(self.predict_button)

        self.setLayout(layout)
        self.predict_button.clicked.connect(self.open_predict_dialog)

    def set_token_and_load_data(self, token):
        self.auth_token = token
        self.api_headers = {'Authorization': f'Bearer {self.auth_token}'}
        self.load_history()

    def load_history(self):
        try:
            response = requests.get(f"{API_URL}/history", headers=self.api_headers)
            response.raise_for_status()
            self.history_data = response.json()

            # Debug print
            print("=== DATA YANG DITERIMA DARI BACKEND ===")
            for item in self.history_data:
                print(item)
            print("========================================")

            self.populate_table()
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Error', f"Gagal memuat riwayat:\n{e}")

    def populate_table(self):
        if not self.history_data:
            self.history_table.setRowCount(0)
            self.history_table.setColumnCount(0)
            return

        column_map = {
            "detectedDisease": "Penyakit Terdeteksi",
            "dateChecked": "Tanggal Prediksi"
        }

        headers = list(column_map.keys())
        self.history_table.setColumnCount(len(headers))
        self.history_table.setRowCount(len(self.history_data))
        self.history_table.setHorizontalHeaderLabels([column_map[h] for h in headers])

        for row_idx, row_data in enumerate(self.history_data):
            for col_idx, key in enumerate(headers):
                value = row_data.get(key, '')
                if key == 'detectedDisease':
                    value = bersihkan_nama_penyakit(value)
                elif key == 'dateChecked' and value:
                    try:
                        WIB = timezone(timedelta(hours=8))
                        dt = datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(WIB)
                        value = dt.strftime('%d %B %Y, %H:%M')
                    except Exception:
                        pass
                self.history_table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def open_predict_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Pilih Gambar", "", "Image Files (*.png *.jpg *.jpeg *.webp)"
        )
        if file_path:
            self.perform_prediction(file_path)

    def perform_prediction(self, file_path):
        loading_msg = QMessageBox()
        loading_msg.setWindowTitle("Info")
        loading_msg.setText("Sedang mengirim gambar dan melakukan prediksi...")
        loading_msg.setStandardButtons(QMessageBox.NoButton)
        loading_msg.show()
        QApplication.processEvents()

        try:
            mime_type, _ = mimetypes.guess_type(file_path)
            if not mime_type:
                mime_type = 'application/octet-stream'

            with open(file_path, 'rb') as image_file:
                files = {
                    'image': (os.path.basename(file_path), image_file, mime_type)
                }
                response = requests.post(
                    f"{API_URL}/predict",
                    headers=self.api_headers,
                    files=files
                )
                response.raise_for_status()

                result = response.json()
                loading_msg.close()

                disease_name = (
                    result.get('detectedDisease') or
                    result.get('predicted_disease') or
                    'Tidak diketahui'
                )
                disease_name = bersihkan_nama_penyakit(disease_name)
                confidence = result.get('confidence', 'N/A')

                QMessageBox.information(
                    self, "Hasil Prediksi",
                    f"Penyakit yang terdeteksi:\n\n{disease_name}\n\nTingkat Keyakinan: {confidence}"
                )
                self.load_history()

        except requests.exceptions.RequestException as e:
            loading_msg.close()
            msg = "Terjadi kesalahan saat mengirim data ke server."
            if e.response:
                try:
                    error_info = e.response.json()
                    msg = error_info.get('error', str(e))
                except ValueError:
                    msg = "Respons dari server bukan JSON yang valid."
            QMessageBox.critical(self, "Error Prediksi", f"Gagal melakukan prediksi:\n{msg}")

    def export_to_csv(self):
        if not self.history_data:
            QMessageBox.warning(self, "Tidak Ada Data", "Tidak ada riwayat untuk diekspor.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Simpan sebagai CSV", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_path:
            try:
                headers = list(self.history_data[0].keys())
                with open(file_path, 'w', newline='', encoding='utf-8') as output_file:
                    writer = csv.DictWriter(output_file, fieldnames=headers)
                    writer.writeheader()
                    writer.writerows(self.history_data)
                QMessageBox.information(self, "Berhasil", f"Riwayat berhasil diekspor ke:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal mengekspor file:\n{e}")
