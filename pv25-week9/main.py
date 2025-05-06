import sys
from PyQt5.QtWidgets import QApplication
from input_dialog_view import InputDialogView
from input_dialog_presenter import InputDialogPresenter

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = InputDialogView()
    presenter = InputDialogPresenter(view)
    view.show()
    sys.exit(app.exec_())
