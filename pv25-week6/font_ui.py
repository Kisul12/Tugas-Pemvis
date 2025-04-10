from PyQt5.QtWidgets import (
    QWidget, QLabel, QSlider, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class FontAdjusterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font Size and Color Adjuster")
        self.setGeometry(100, 100, 600, 300)

        # Label utama
        self.label = QLabel("F1B008004")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 30))
        self.label.setAutoFillBackground(True)
        self.label.setFixedHeight(100)  

        # Slider Font Size
        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setRange(20, 60)
        self.font_slider.setValue(30)

        # Slider Background Color
        self.bg_slider = QSlider(Qt.Horizontal)
        self.bg_slider.setRange(0, 255)
        self.bg_slider.setValue(0)

        # Slider Font Color
        self.font_color_slider = QSlider(Qt.Horizontal)
        self.font_color_slider.setRange(0, 255)
        self.font_color_slider.setValue(255)

        # Labels keterangan
        self.font_label = QLabel("Font Size")
        self.bg_label = QLabel("Background Color")
        self.font_color_label = QLabel("Font Color")

        # Watermark
        self.watermark = QLabel("F1B008004 | Muhammad Rizki Assamsuli")
        self.watermark.setAlignment(Qt.AlignRight)
        self.watermark.setStyleSheet("font-size: 10pt; color: gray;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.font_label)
        layout.addWidget(self.font_slider)
        layout.addWidget(self.bg_label)
        layout.addWidget(self.bg_slider)
        layout.addWidget(self.font_color_label)
        layout.addWidget(self.font_color_slider)
        layout.addWidget(self.watermark)

        self.setLayout(layout)
