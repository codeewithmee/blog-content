#!/usr/bin/python
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui ,QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pytube import YouTube
import sys
import os 

class Window(QtWidgets.QWidget):
	"""docstring for Window"""
	def __init__(self):
		QMainWindow.__init__(self)
		
		self.setWindowTitle("YouTube Video Downloader")
		self.setGeometry(300,200, 500, 200)
		self.UiComponents()
		self.show()


	def UiComponents(self):
		self.label1 = QLabel("Paste the url to download the youtube Video")
		self.browse_btn = QPushButton("Browse")
		self.type_space1 = QLineEdit()
		self.type_space2 = QLineEdit("./")
		self.download_btn = QPushButton("Download")

		v_box = QVBoxLayout()
		v_box.addWidget(self.label1)
		v_box.addWidget(self.type_space1)
		v_box.addStretch()
		v_box.addWidget(self.type_space2)
		v_box.addWidget(self.browse_btn)
		v_box.addWidget(self.download_btn)

		self.browse_btn.clicked.connect(lambda x : self.changeFolder())
		self.download_btn.clicked.connect(lambda x : self.Download(self.type_space1.text()))

		self.setLayout(v_box)



	def changeFolder(self):
		download_path = self.type_space2.text()
		fname = QFileDialog.getExistingDirectory(
            self, 'Select a directory', download_path)
		if fname:
			fname = QDir.toNativeSeparators(fname)

		if os.path.isdir(fname):
			self.type_space2.setText(fname)


	def Download(self,video_link):
		
		Youtube_link = video_link
		download_folder = self.type_space2.text()
		self.download_check(Youtube_link,download_folder)




	def download_check(self,Youtube_link,folder_path):
		try:
			getVideo = YouTube(Youtube_link)
			videoStream = getVideo.streams.first()
			videoStream.download(folder_path)
			self.msgbox(folder_path)
		except:
			self.ERROR_msgbox()




	def msgbox(self,path):
		msg_button = QMessageBox.question(self, 'Message Box', f"This video is Downloaded in {path}", QMessageBox.Ok | QMessageBox.Cancel)
		if msg_button == QMessageBox.Ok:
			return

		if msg_button == QMessageBox.Cancel:
			return

	def ERROR_msgbox(self):
		msg_button = QMessageBox.question(self, 'Message Box', "This video is not Downloaded", QMessageBox.Ok | QMessageBox.Cancel)
		if msg_button == QMessageBox.Ok:
			return

		if msg_button == QMessageBox.Cancel:
			return



if __name__ == '__main__':
	
	App = QApplication(sys.argv) # create pyqt5 app 
	window = Window() # create the instance of our Window 
	sys.exit(App.exec()) # start the app 