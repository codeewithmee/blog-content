#!/usr/bin/python
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 


class Window(QMainWindow): 

	def __init__(self): 
		super().__init__() 

		self.setWindowTitle("Calender ") 
		self.setGeometry(300,200, 500, 400) 
		self.UiComponents()
		self.showDate() 
		self.show() 

	def UiComponents(self):

		
		calender = QCalendarWidget(self) 
		calender.setGeometry(50, 50, 400, 250)
		layout = QVBoxLayout()
		font = QFont('Arial', 12, QFont.Bold)
		self.label = QLabel("Time")
		self.label.setAlignment(Qt.AlignBottom)
		self.label.setFont(font)
		layout.addWidget(self.label)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
		self.move(100,100)
		timer = QTimer(self)
		timer.timeout.connect(self.showTime)
		timer.start(1000)

	def showTime(self):

		current_time = QTime.currentTime()
		label_time = current_time.toString('hh:mm:ss')
		self.label.setText(label_time)


		
	def showDate(self):

		self.date = QDate.currentDate()
		self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))



if __name__ == '__main__':
	
	App = QApplication(sys.argv) # create pyqt5 app 
	window = Window() # create the instance of our Window 
	sys.exit(App.exec()) # start the app 
	

