from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
    QVBoxLayout, QHBoxLayout, QComboBox, QSpinBox, QCheckBox,
    QTableWidgetItem, QMessageBox, QHeaderView
)

class MyBookApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyBook - Pengelolaan Buku")
        self.setGeometry(100, 100, 800, 500)

        self.books = []  # Data buku: list of dict

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Header Nama & NIM
        identitas_layout = QHBoxLayout()
        self.label_nama = QLabel("Nama: Muhammad Rizki Assamsuli")
        self.label_nim = QLabel("NIM: F1D022146")
        identitas_layout.addWidget(self.label_nama)
        identitas_layout.addStretch()
        identitas_layout.addWidget(self.label_nim)
        main_layout.addLayout(identitas_layout)

        # Form input buku
        form_layout = QHBoxLayout()

        self.input_judul = QLineEdit()
        self.input_judul.setPlaceholderText("Judul Buku")

        self.input_penulis = QLineEdit()
        self.input_penulis.setPlaceholderText("Penulis")

        self.input_tahun = QSpinBox()
        self.input_tahun.setRange(1900, 2100)
        self.input_tahun.setValue(2023)

        self.input_kategori = QComboBox()
        self.input_kategori.addItems(["Fiksi", "Non-Fiksi", "Teknologi", "Biografi"])

        self.check_dibaca = QCheckBox("Sudah Dibaca")
        self.check_arsip = QCheckBox("Arsipkan")

        form_layout.addWidget(self.input_judul)
        form_layout.addWidget(self.input_penulis)
        form_layout.addWidget(self.input_tahun)
        form_layout.addWidget(self.input_kategori)
        form_layout.addWidget(self.check_dibaca)
        form_layout.addWidget(self.check_arsip)

        main_layout.addLayout(form_layout)

        # Tombol aksi
        btn_layout = QHBoxLayout()
        self.btn_tambah = QPushButton("Tambah")
        self.btn_update = QPushButton("Update")
        self.btn_hapus = QPushButton("Hapus")

        self.btn_tambah.setStyleSheet("background-color: #7DCEA0; font-weight: bold;")
        self.btn_hapus.setStyleSheet("background-color: #F1948A;")

        btn_layout.addWidget(self.btn_tambah)
        btn_layout.addWidget(self.btn_update)
        btn_layout.addWidget(self.btn_hapus)
        main_layout.addLayout(btn_layout)

        # Tabel buku
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Judul", "Penulis", "Tahun", "Kategori", "Dibaca", "Arsip"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

    def get_form_data(self):
        return {
            "judul": self.input_judul.text(),
            "penulis": self.input_penulis.text(),
            "tahun": self.input_tahun.value(),
            "kategori": self.input_kategori.currentText(),
            "dibaca": self.check_dibaca.isChecked(),
            "arsip": self.check_arsip.isChecked()
        }

    def clear_form(self):
        self.input_judul.clear()
        self.input_penulis.clear()
        self.input_tahun.setValue(2023)
        self.input_kategori.setCurrentIndex(0)
        self.check_dibaca.setChecked(False)
        self.check_arsip.setChecked(False)
        self.table.clearSelection()

    def refresh_table(self):
        self.table.setRowCount(0)
        for buku in self.books:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(buku["judul"]))
            self.table.setItem(row_position, 1, QTableWidgetItem(buku["penulis"]))
            self.table.setItem(row_position, 2, QTableWidgetItem(str(buku["tahun"])))
            self.table.setItem(row_position, 3, QTableWidgetItem(buku["kategori"]))
            self.table.setItem(row_position, 4, QTableWidgetItem("✓" if buku["dibaca"] else "✗"))
            self.table.setItem(row_position, 5, QTableWidgetItem("✓" if buku["arsip"] else "✗"))

    def load_data_ke_form(self, row, _):
        buku = self.books[row]
        self.input_judul.setText(buku["judul"])
        self.input_penulis.setText(buku["penulis"])
        self.input_tahun.setValue(buku["tahun"])
        self.input_kategori.setCurrentText(buku["kategori"])
        self.check_dibaca.setChecked(buku["dibaca"])
        self.check_arsip.setChecked(buku["arsip"])