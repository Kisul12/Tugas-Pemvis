from PyQt6 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("POS Application - F1D022146 - Muhammad Rizki Assamsuli")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(150, 60, 521, 341))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        # Label Produk
        self.productLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.productLabel.setStyleSheet("font: 8pt \"Poppins\";")
        self.productLabel.setObjectName("productLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.productLabel)

        # ComboBox Produk
        self.productComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.productComboBox.setStyleSheet("font: 8pt \"Poppins\";")
        self.productComboBox.setObjectName("productComboBox")
        self.productComboBox.addItems([
            "Silahkan Pilih Produk😊",
            "Bimoli (Rp. 25,000)",
            "Sania (Rp. 24,000)",
            "Tropical (Rp. 23,500)",
            "Fortune (Rp. 24,500)",
            "Beras Ramos 5kg (Rp. 65,000)",
            "Beras Setra 5kg (Rp. 70,000)",
            "Garam Dapur (Rp. 4,000)",
            "Gula Pasir 1kg (Rp. 15,000)",
            "Minyak Wijen 250ml (Rp. 18,000)",
            "Kecap Manis ABC 600ml (Rp. 17,500)",
            "Saus Sambal Indofood 335ml (Rp. 11,000)",
            "Santan Kara 200ml (Rp. 5,000)",
            "Tepung Terigu Segitiga Biru 1kg (Rp. 13,000)",
            "Telur Ayam 1kg (Rp. 28,000)",
            "Mentega Blue Band 250g (Rp. 10,000)",
            "Bawang Merah 250g (Rp. 12,000)",
            "Bawang Putih 250g (Rp. 10,000)",
            "Cabai Merah 250g (Rp. 14,000)"
        ])
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.productComboBox)

        # Label & Input Quantity
        self.quantityLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.quantityLabel.setStyleSheet("font: 8pt \"Poppins\";")
        self.quantityLabel.setObjectName("quantityLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.quantityLabel)

        self.quantityLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.quantityLineEdit.setStyleSheet("font: 8pt \"Poppins\";")
        self.quantityLineEdit.setObjectName("quantityLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.quantityLineEdit)

        # Label & SpinBox Discount
        self.discountLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.discountLabel.setStyleSheet("font: 8pt \"Poppins\";")
        self.discountLabel.setObjectName("discountLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.discountLabel)

        self.discountSpinBox = QtWidgets.QSpinBox(parent=self.formLayoutWidget)
        self.discountSpinBox.setStyleSheet("font: 8pt \"Poppins\";")
        self.discountSpinBox.setObjectName("discountSpinBox")
        self.discountSpinBox.setSuffix(" %")
        self.discountSpinBox.setFixedWidth(70)  
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.discountSpinBox)

        # Tombol Add to Cart & Clear
        self.pushButton = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.pushButton.setStyleSheet("font: 8pt \"Poppins\";")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.pushButton_2.setStyleSheet("font: 8pt \"Poppins\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton_2)

        # ListView Cart
        self.listView = QtWidgets.QListView(parent=self.formLayoutWidget)
        self.listView.setStyleSheet("font: 8pt \"Poppins\";")
        self.listView.setObjectName("listView")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.listView)

        # Label Total
        self.totalLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.totalLabel.setStyleSheet("font: bold 9pt \"Poppins\"; ")
        self.totalLabel.setObjectName("totalLabel")
        self.totalLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.totalLabel.setText("Total: Rp. 0")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.totalLabel)

        # Setup Main Window
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.productLabel.setText(_translate("MainWindow", "Product"))
        self.quantityLabel.setText(_translate("MainWindow", "Quantity"))
        self.discountLabel.setText(_translate("MainWindow", "Discount"))
        self.pushButton.setText(_translate("MainWindow", "Add to Cart"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.totalLabel.setText(_translate("MainWindow", "Total: Rp. 0"))