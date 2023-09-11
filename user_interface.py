from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObjects): #An object wrapping around our ui
    def __init__(self):
        super().__init__()
        self.ui = loader.load("widget.ui", None)
        self.ui.setWindowTitle("Installation")
    