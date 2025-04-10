import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QColor, QPalette
from font_ui import FontAdjusterUI

class FontAdjusterLogic(FontAdjusterUI):
    def __init__(self):
        super().__init__()
        self.font_slider.valueChanged.connect(self.update_font_size)
        self.bg_slider.valueChanged.connect(self.update_colors)
        self.font_color_slider.valueChanged.connect(self.update_colors)
        self.update_colors()

    def update_font_size(self):
        size = self.font_slider.value()
        self.label.setFont(QFont("Arial", size))

    def update_colors(self):
        bg_val = self.bg_slider.value()
        font_val = self.font_color_slider.value()
        palette = self.label.palette()
        palette.setColor(QPalette.Window, QColor(bg_val, bg_val, bg_val))
        palette.setColor(QPalette.WindowText, QColor(font_val, font_val, font_val))
        self.label.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontAdjusterLogic()
    window.show()
    sys.exit(app.exec_())
