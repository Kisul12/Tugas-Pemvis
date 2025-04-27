import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from mybook_ui import MyBookApp

def tambah_buku(window):
    data = window.get_form_data()
    if not data["judul"] or not data["penulis"]:
        QMessageBox.warning(window, "Peringatan", "Judul dan Penulis wajib diisi!")
        return
    window.books.append(data)
    window.refresh_table()
    window.clear_form()

def update_buku(window):
    row = window.table.currentRow()
    if row == -1:
        QMessageBox.warning(window, "Peringatan", "Pilih data buku yang ingin diperbarui!")
        return
    data = window.get_form_data()
    window.books[row] = data
    window.refresh_table()
    window.clear_form()

def hapus_buku(window):
    row = window.table.currentRow()
    if row == -1:
        QMessageBox.warning(window, "Peringatan", "Pilih data buku yang ingin dihapus!")
        return
    konfirmasi = QMessageBox.question(window, "Konfirmasi", "Apakah kamu yakin ingin menghapus buku ini?")
    if konfirmasi == QMessageBox.Yes:
        del window.books[row]
        window.refresh_table()
        window.clear_form()

def main():
    app = QApplication(sys.argv)
    window = MyBookApp()

    # Event binding
    window.btn_tambah.clicked.connect(lambda: tambah_buku(window))
    window.btn_update.clicked.connect(lambda: update_buku(window))
    window.btn_hapus.clicked.connect(lambda: hapus_buku(window))
    window.table.cellClicked.connect(window.load_data_ke_form)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
