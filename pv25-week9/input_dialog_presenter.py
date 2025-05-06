from PyQt5.QtWidgets import QInputDialog

class InputDialogPresenter:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.view.btn_item.clicked.connect(self.getItem)
        self.view.btn_text.clicked.connect(self.getText)
        self.view.btn_int.clicked.connect(self.getInt)

    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(
            self.view, "select input dialog", "list of languages", items, 0, False
        )
        if ok and item:
            self.view.le.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(
            self.view, 'Text Input Dialog', 'Enter your name:'
        )
        if ok:
            self.view.le1.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(
            self.view, "integer input dialog", "enter a number"
        )
        if ok:
            self.view.le2.setText(str(num))
