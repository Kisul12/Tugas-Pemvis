import sys
import sqlite3
import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QMessageBox, QFileDialog, QFormLayout, QGroupBox,
    QSpacerItem, QSizePolicy, QStatusBar, QDockWidget, QScrollArea,
    QTextEdit
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon # Digunakan untuk ikon (opsional)

# --- Konfigurasi Awal ---
DB_NAME = 'manajemen_buku.db'
TABLE_NAME = 'buku'
NAMA_MAHASISWA = "Muhammad Rizki Assamsuli"
NIM_MAHASISWA = "F1D022146"

class BookManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_selected_id = None
        self.init_db()
        self.init_ui()
        self.load_data()

    def init_db(self):
        """Inisialisasi database dan tabel jika belum ada."""
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    judul TEXT NOT NULL,
                    pengarang TEXT NOT NULL,
                    tahun INTEGER
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Gagal inisialisasi database: {e}")
        finally:
            if conn:
                conn.close()

    def init_ui(self):
        """Inisialisasi User Interface dengan fitur-fitur baru."""
        self.setWindowTitle("Manajemen Buku - PV25 Week 11 Enhancement")
        self.setGeometry(100, 100, 900, 700)
        # self.setWindowIcon(QIcon('path/to/your/icon.png')) # Opsional: jika Anda punya ikon

        # Central Widget dan Layout Utama
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # --- Implementasi QScrollArea untuk form input ---
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        # Atur agar QScrollArea tidak memakan banyak ruang secara vertikal
        scroll_area.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        main_layout.addWidget(scroll_area)

        # Grup Input Data (dimasukkan ke dalam scroll area)
        self.input_group = QGroupBox("Form Data Buku")
        input_group_layout = QVBoxLayout()
        form_layout = QFormLayout()

        # --- Implementasi QClipboard ---
        self.judul_input = QLineEdit()
        self.judul_input.setPlaceholderText("Masukkan judul buku")
        paste_judul_button = QPushButton("Paste")
        paste_judul_button.setToolTip("Tempel judul dari clipboard")
        paste_judul_button.clicked.connect(self.paste_from_clipboard)
        
        judul_layout = QHBoxLayout()
        judul_layout.addWidget(self.judul_input)
        judul_layout.addWidget(paste_judul_button)
        
        self.pengarang_input = QLineEdit()
        self.pengarang_input.setPlaceholderText("Masukkan nama pengarang")
        self.tahun_input = QLineEdit()
        self.tahun_input.setPlaceholderText("Masukkan tahun terbit (mis: 2024)")

        form_layout.addRow("Judul:", judul_layout)
        form_layout.addRow("Pengarang:", self.pengarang_input)
        form_layout.addRow("Tahun:", self.tahun_input)
        input_group_layout.addLayout(form_layout)

        # Tombol Simpan dan Reset
        button_input_layout = QHBoxLayout()
        self.save_button = QPushButton("Simpan")
        self.save_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.save_button.clicked.connect(self.save_data)
        self.reset_button = QPushButton("Reset Form")
        self.reset_button.clicked.connect(self.clear_inputs)
        button_input_layout.addWidget(self.save_button)
        button_input_layout.addWidget(self.reset_button)
        input_group_layout.addLayout(button_input_layout)

        self.input_group.setLayout(input_group_layout)
        scroll_area.setWidget(self.input_group) # Masukkan groupbox ke dalam scroll area

        # --- Implementasi QDockWidget ---
        self.create_dock_widget()

        # --- Tabel Data (Sudah mendukung scrolling by default) ---
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Judul", "Pengarang", "Tahun"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table_widget.doubleClicked.connect(self.load_data_for_edit)
        main_layout.addWidget(self.table_widget)

        # Tombol Hapus
        self.delete_button = QPushButton("Hapus Data Terpilih")
        self.delete_button.setStyleSheet("background-color: #f44336; color: white;")
        self.delete_button.clicked.connect(self.delete_data)
        main_layout.addWidget(self.delete_button)

        # --- Implementasi QStatusBar ---
        self.setup_status_bar()

    def create_dock_widget(self):
        """Membuat dan mengkonfigurasi QDockWidget."""
        dock_widget = QDockWidget("Panel Bantuan & Operasi Data", self)
        dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.TopDockWidgetArea)

        # Widget konten untuk dock
        dock_content_widget = QWidget()
        dock_layout = QVBoxLayout(dock_content_widget)

        # Grup Pencarian dan Ekspor
        search_export_group = QGroupBox("Pencarian & Ekspor")
        search_export_layout = QHBoxLayout()
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Cari Judul...")
        self.search_input.textChanged.connect(self.search_data)
        search_export_layout.addWidget(QLabel("Cari:"))
        search_export_layout.addWidget(self.search_input)
        
        self.export_button = QPushButton("Ekspor CSV")
        self.export_button.setStyleSheet("background-color: #008CBA; color: white;")
        self.export_button.clicked.connect(self.export_to_csv)
        search_export_layout.addWidget(self.export_button)
        search_export_group.setLayout(search_export_layout)
        dock_layout.addWidget(search_export_group)

        # Panel Bantuan/Info
        help_group = QGroupBox("Info Bantuan")
        help_layout = QVBoxLayout(help_group)
        help_text = QTextEdit()
        help_text.setReadOnly(True)
        help_text.setHtml(
            """
            <b>Panduan Penggunaan:</b>
            <ul>
                <li><b>Tambah Data:</b> Isi form lalu klik 'Simpan'.</li>
                <li><b>Edit Data:</b> Klik dua kali pada baris tabel, ubah data di form, lalu klik 'Update Data'.</li>
                <li><b>Hapus Data:</b> Pilih satu atau lebih baris di tabel, lalu klik 'Hapus Data Terpilih'.</li>
                <li><b>Pencarian:</b> Ketik judul buku di kolom 'Cari' untuk memfilter tabel.</li>
                <li><b>Paste:</b> Gunakan tombol 'Paste' untuk menempelkan judul dari clipboard.</li>
            </ul>
            """
        )
        help_layout.addWidget(help_text)
        dock_layout.addWidget(help_group)

        dock_layout.addStretch() # Menambahkan spacer di akhir
        dock_content_widget.setLayout(dock_layout)
        dock_widget.setWidget(dock_content_widget)

        # Tambahkan dock widget ke main window
        self.addDockWidget(Qt.RightDockWidgetArea, dock_widget)

    def setup_status_bar(self):
        """Mengatur QStatusBar untuk menampilkan nama dan NIM."""
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        
        # Widget untuk nama dan NIM, ditampilkan permanen di sisi kanan
        name_label = QLabel(f"<b>Nama:</b> {NAMA_MAHASISWA}")
        nim_label = QLabel(f"<b>NIM:</b> {NIM_MAHASISWA}")
        
        status_bar.addPermanentWidget(name_label)
        status_bar.addPermanentWidget(QLabel(" | ")) # Pemisah
        status_bar.addPermanentWidget(nim_label)
        
        # Pesan sementara di sisi kiri
        status_bar.showMessage("Aplikasi siap digunakan.", 5000)

    def paste_from_clipboard(self):
        """Mengambil teks dari clipboard dan menempelkannya ke input judul."""
        clipboard = QApplication.clipboard()
        self.judul_input.setText(clipboard.text())
        self.statusBar().showMessage("Teks dari clipboard berhasil ditempel.", 3000)

    def execute_query(self, query, params=()):
        """Eksekusi query SQLite dengan penanganan error."""
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error saat eksekusi query: {e}")
            return None
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    def load_data(self, search_term=None):
        """Memuat atau memfilter data dari database ke QTableWidget."""
        self.table_widget.setRowCount(0)
        query = f"SELECT id, judul, pengarang, tahun FROM {TABLE_NAME}"
        params = []
        if search_term:
            query += " WHERE judul LIKE ?"
            params.append(f"%{search_term}%")
        query += " ORDER BY id ASC"

        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute(query, params)
            records = cursor.fetchall()
            for row_number, row_data in enumerate(records):
                self.table_widget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter if column_number in [0, 3] else Qt.AlignLeft | Qt.AlignVCenter)
                    self.table_widget.setItem(row_number, column_number, item)
        except sqlite3.Error as e:
             QMessageBox.warning(self, "Load Data Error", f"Gagal memuat data: {e}")
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    def save_data(self):
        """Menyimpan data baru atau memperbarui data yang ada."""
        judul = self.judul_input.text().strip()
        pengarang = self.pengarang_input.text().strip()
        tahun_str = self.tahun_input.text().strip()

        if not judul or not pengarang or not tahun_str:
            QMessageBox.warning(self, "Input Tidak Lengkap", "Semua field harus diisi!")
            return

        try:
            tahun = int(tahun_str)
            if not (1000 <= tahun <= 9999):
                raise ValueError("Tahun tidak valid.")
        except ValueError:
            QMessageBox.warning(self, "Input Tidak Valid", "Tahun harus berupa 4 digit angka (contoh: 2024).")
            return

        if self.current_selected_id is None:
            query = f"INSERT INTO {TABLE_NAME} (judul, pengarang, tahun) VALUES (?, ?, ?)"
            params = (judul, pengarang, tahun)
            msg_success = "Data buku berhasil disimpan!"
            status_msg = "Data baru telah ditambahkan."
        else:
            query = f"UPDATE {TABLE_NAME} SET judul=?, pengarang=?, tahun=? WHERE id=?"
            params = (judul, pengarang, tahun, self.current_selected_id)
            msg_success = f"Data buku dengan ID {self.current_selected_id} berhasil diperbarui!"
            status_msg = f"Data ID {self.current_selected_id} telah diperbarui."

        if self.execute_query(query, params):
            QMessageBox.information(self, "Sukses", msg_success)
            self.statusBar().showMessage(status_msg, 5000)
            self.clear_inputs()
            self.load_data()

    def load_data_for_edit(self, row_index):
        """Memuat data dari baris yang di-double-click ke form input."""
        try:
            row = row_index.row()
            self.current_selected_id = int(self.table_widget.item(row, 0).text())
            self.judul_input.setText(self.table_widget.item(row, 1).text())
            self.pengarang_input.setText(self.table_widget.item(row, 2).text())
            self.tahun_input.setText(self.table_widget.item(row, 3).text())
            self.save_button.setText("Update Data")
            self.input_group.setTitle(f"Edit Data Buku (ID: {self.current_selected_id})")
            self.statusBar().showMessage(f"Mode edit untuk ID: {self.current_selected_id}", 5000)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal memuat data untuk diedit: {e}")
            self.clear_inputs()

    def delete_data(self):
        """Menghapus data yang dipilih dari tabel."""
        selected_rows = self.table_widget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Peringatan", "Pilih baris data yang ingin dihapus terlebih dahulu.")
            return

        ids_to_delete = [self.table_widget.item(index.row(), 0).text() for index in selected_rows]
        
        confirm = QMessageBox.question(self, "Konfirmasi Hapus",
                                     f"Apakah Anda yakin ingin menghapus {len(ids_to_delete)} data terpilih?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirm == QMessageBox.Yes:
            try:
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                placeholders = ','.join('?' for _ in ids_to_delete)
                query = f"DELETE FROM {TABLE_NAME} WHERE id IN ({placeholders})"
                cursor.execute(query, ids_to_delete)
                conn.commit()
                QMessageBox.information(self, "Sukses", f"{len(ids_to_delete)} data berhasil dihapus.")
                self.statusBar().showMessage(f"{len(ids_to_delete)} data dihapus.", 5000)
                self.load_data()
                self.clear_inputs()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Database Error", f"Gagal menghapus data: {e}")
            finally:
                if 'conn' in locals() and conn:
                    conn.close()

    def clear_inputs(self):
        """Membersihkan field input dan mereset state ke mode 'Simpan'."""
        self.judul_input.clear()
        self.pengarang_input.clear()
        self.tahun_input.clear()
        self.current_selected_id = None
        self.save_button.setText("Simpan")
        self.input_group.setTitle("Form Data Buku")
        self.judul_input.setFocus()
        self.table_widget.clearSelection()
        self.statusBar().showMessage("Form dibersihkan. Siap untuk input baru.", 3000)

    def search_data(self):
        """Mencari data berdasarkan judul secara real-time."""
        search_term = self.search_input.text().strip()
        self.load_data(search_term)

    def export_to_csv(self):
        """Mengekspor semua data dari tabel ke file CSV."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Simpan sebagai CSV", "", "CSV Files (*.csv);;All Files (*)")
        if not file_path:
            return

        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute(f"SELECT id, judul, pengarang, tahun FROM {TABLE_NAME}")
            records = cursor.fetchall()
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["ID", "Judul", "Pengarang", "Tahun"])
                csv_writer.writerows(records)
            QMessageBox.information(self, "Sukses", f"Data berhasil diekspor ke {file_path}")
            self.statusBar().showMessage(f"Data diekspor ke {file_path}", 5000)
        except (sqlite3.Error, IOError) as e:
            QMessageBox.critical(self, "Error", f"Gagal mengekspor data: {e}")
        finally:
            if 'conn' in locals() and conn:
                conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QMainWindow, QDockWidget {
            background-color: #f0f0f0;
        }
        QWidget {
            font-size: 10pt;
        }
        QGroupBox {
            font-weight: bold;
            margin-top: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 5px 10px;
            background-color: #e0e0e0;
            border-radius: 5px;
        }
        QLineEdit, QTableWidget, QTextEdit {
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
        QPushButton {
            padding: 8px 12px;
            border: 1px solid #bbb;
            border-radius: 4px;
            background-color: #e7e7e7;
        }
        QPushButton:hover {
            background-color: #d7d7d7;
        }
        QHeaderView::section {
            background-color: #e0e0e0;
            padding: 4px;
            border: 1px solid #ccc;
            font-weight: bold;
        }
        QStatusBar {
            background-color: #e0e0e0;
            font-weight: normal;
        }
        QStatusBar QLabel {
            padding: 0 5px;
        }
    """)
    main_window = BookManagerApp()
    main_window.show()
    sys.exit(app.exec_())