import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QListView, QMessageBox
from PyQt6.QtCore import QStringListModel
from index_ui import Ui_MainWindow  


class POSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Daftar produk dan harga
        self.products = {
            "": 0,
            "Bimoli (Rp. 25,000)": 25000,
            "Sania (Rp. 24,000)": 24000,
            "Tropical (Rp. 23,500)": 23500,
            "Fortune (Rp. 24,500)": 24500,
            "Beras Ramos 5kg (Rp. 65,000)": 65000,
            "Beras Setra 5kg (Rp. 70,000)": 70000,
            "Garam Dapur (Rp. 4,000)": 4000,
            "Gula Pasir 1kg (Rp. 15,000)": 15000,
            "Minyak Wijen 250ml (Rp. 18,000)": 18000,
            "Kecap Manis ABC 600ml (Rp. 17,500)": 17500,
            "Saus Sambal Indofood 335ml (Rp. 11,000)": 11000,
            "Santan Kara 200ml (Rp. 5,000)": 5000,
            "Tepung Terigu Segitiga Biru 1kg (Rp. 13,000)": 13000,
            "Telur Ayam 1kg (Rp. 28,000)": 28000,
            "Mentega Blue Band 250g (Rp. 10,000)": 10000,
            "Bawang Merah 250g (Rp. 12,000)": 12000,
            "Bawang Putih 250g (Rp. 10,000)": 10000,
            "Cabai Merah 250g (Rp. 14,000)": 14000,
        }
        self.ui.productComboBox.clear()
        self.ui.productComboBox.addItems(self.products.keys())

        self.ui.discountSpinBox.setSuffix(" %")
        self.ui.discountSpinBox.setMaximum(100)

        self.cart_model = QStringListModel()
        self.ui.listView.setModel(self.cart_model)
        self.cart_items = []
        self.total_price = 0

        self.ui.pushButton.clicked.connect(self.add_to_cart)
        self.ui.pushButton_2.clicked.connect(self.clear_cart)

    def add_to_cart(self):
        product_name = self.ui.productComboBox.currentText()
        quantity_text = self.ui.quantityLineEdit.text()
        discount = self.ui.discountSpinBox.value()

        # Validasi
        if not product_name or product_name == "":
            QMessageBox.warning(self, "Warning", "Pilih produk terlebih dahulu.")
            return
        if not quantity_text.isdigit():
            QMessageBox.warning(self, "Warning", "Quantity harus berupa angka.")
            return

        quantity = int(quantity_text)
        price = self.products[product_name]
        subtotal = price * quantity
        discount_amount = subtotal * discount // 100
        total = subtotal - discount_amount

        self.total_price += total

        item_text = f"{product_name} - {quantity} x Rp. {price:,} (disc {discount}%)"
        self.cart_items.append(item_text)
        self.cart_model.setStringList(self.cart_items)

        # Update total harga
        self.update_total_label()

    def clear_cart(self):
        self.cart_items = []
        self.cart_model.setStringList(self.cart_items)
        self.total_price = 0
        self.update_total_label()

    def update_total_label(self):
        self.ui.totalLabel.setText(f"Total: Rp. {self.total_price:,}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = POSApp()
    window.setWindowTitle("POS Application - F1D022146 - Muhammad Rizki Assamsuli")
    window.show()
    sys.exit(app.exec())
