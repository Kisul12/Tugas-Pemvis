import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QPoint

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Task Week 3 - F1D022146_Muhammad Rizki Assamsuli")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Gerakkan Mouse kedalam Area ini", self)
        self.label.setStyleSheet("background-color: lightblue; border-radius: 10px; ")
        self.label.setGeometry(200, 150, 200, 50)
        self.label.setAlignment(Qt.AlignCenter)

        self.setMouseTracking(True)
        self.label.installEventFilter(self)

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        self.label.setText(f"X: {x}, Y: {y}")

    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == event.Enter:
            new_x = random.randint(0, self.width() - self.label.width())
            new_y = random.randint(0, self.height() - self.label.height())
            self.label.move(QPoint(new_x, new_y))
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())
