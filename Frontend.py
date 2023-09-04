from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi("dialog.ui", self)
		self.button = self.findChild(QPushButton, "pushButton")
		self.label = self.findChild(QLabel, "label")
		self.button.clicked.connect(self.clicker)
		self.show()

	def clicker(self):
		fname = QFileDialog.getOpenFileName(self, "Open File", "c:\\gui\\images", "All Files (*);; MP4 Files (*.mp4)" )
		if fname:
			self.label.setText(fname[0])


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
    