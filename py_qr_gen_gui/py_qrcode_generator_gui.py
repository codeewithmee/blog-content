from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qrcode
import sys




class Image(qrcode.image.base.BaseImage): 

	
	def __init__(self, border, width, box_size):

		self.border = border 
		self.width = width 
		self.box_size = box_size 
		size = (width + border * 2) * box_size 
		self._image = QImage(size, size, QImage.Format_RGB16) 
		self._image.fill(Qt.white) 


	
	def pixmap(self):

		return QPixmap.fromImage(self._image) 

	
	def drawrect(self, row, col): 

		painter = QPainter(self._image) 
		painter.fillRect( 
			(col + self.border) * self.box_size, 
			(row + self.border) * self.box_size, 
			self.box_size, self.box_size, 
			QtCore.Qt.black) 








class Window(QtWidgets.QWidget): 

	
	def __init__(self): 
		QMainWindow.__init__(self) 

		self.setWindowTitle("QR Code") 
		self.setGeometry(100, 100, 300, 300)  
		self.init_ui()
		self.show()


	
	def handleTextEntered(self,text): 


		self.text = text 
		qr_image = qrcode.make(self.text, image_factory = Image).pixmap() 
		self.label_2.setPixmap(qr_image)



	def saveFunc(self,input_data):
		try:

			name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',"Imagefile Files *.png")
			name = name[0]
			img = qrcode.make(input_data)
			img.save(name)
		except Exception as e:
			return

	def init_ui(self):

		self.label_1 = QLabel("Enter the string to Generate QRCODE")
		self.generate_btn = QPushButton("Generate")
		self.save_btn  = QPushButton("Save")
		self.type_space = QLineEdit()
		self.label_2 = QLabel("")

		v_box = QVBoxLayout()
		v_box.addWidget(self.label_1)
		v_box.addStretch()
		v_box.addWidget(self.label_2)
		v_box.addWidget(self.type_space)
		v_box.addStretch()
		v_box.addWidget(self.generate_btn)
		v_box.addWidget(self.save_btn)
		

		self.generate_btn.clicked.connect(lambda x : self.handleTextEntered(self.type_space.text()))
		self.save_btn.clicked.connect(lambda x : self.saveFunc(self.type_space.text()))
		


		self.setLayout(v_box)

if __name__ == '__main__':
	
	App = QApplication(sys.argv)
	window = Window()
	sys.exit(App.exec())