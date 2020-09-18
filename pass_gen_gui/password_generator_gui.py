#!/usr/bin/python

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from password_generator import pwd
import sys

class Window(QtWidgets.QWidget):
	"""docstring for Window"""
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle("Password Generator")
		self.setGeometry(300,300,50,40)
		self.init_ui()
		self.show()

	def password(self,length):

		res = pwd(length)
		self.label_2.setText("Your password is: " + res +"\nCopied in clipboard")
		cb = App.clipboard()
		cb.setText(res)



	def init_ui(self):

		self.label_1 = QLabel("Enter the length of the Password")
		self.button = QPushButton("Generate")
		self.type_space = QLineEdit()
		self.label_2 = QLabel("")

		v_box = QVBoxLayout()
		v_box.addWidget(self.label_1)
		v_box.addStretch()
		v_box.addWidget(self.type_space)
		v_box.addWidget(self.label_2)
		v_box.addStretch()
		v_box.addWidget(self.button)

		self.button.clicked.connect(lambda x : self.password(self.type_space.text()))

		self.setLayout(v_box)
		





if __name__ == '__main__':
	
	App = QApplication(sys.argv)
	window = Window()
	sys.exit(App.exec())