from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import sys
import os


class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)
		
		
		self.setGeometry(300,200,500,400)
		self.Menu()
		self.show()



	def Menu(self):

		layout = QVBoxLayout()
		self.editor = QTextEdit()


		fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont) 
		fixedfont.setPointSize(12)
		self.editor.setFont(fixedfont)
		font_style = self.editor.setFont(fixedfont)

		self.path = None
		self.Title()
		layout.addWidget(self.editor)
		container = QWidget()
		container.setLayout(layout)
		self.setCentralWidget(container)

		self.status = QStatusBar()
		self.setStatusBar(self.status)


		file_toolbar = QToolBar("File")
		edit_toolbar = QToolBar("Edit")


		self.addToolBar(file_toolbar)
		self.addToolBar(edit_toolbar)

		file_menu = self.menuBar().addMenu("&File")
		edit_menu = self.menuBar().addMenu("&Edit")
		toolsMenu = self.menuBar().addMenu("&Tools")
		

		open_file_action = QAction("Open", self)
		save_file_action = QAction("Save", self)
		saveas_file_action = QAction("Save As", self)
		saveas_pdf_action = QAction("Save As Pdf", self)
		print_action = QAction("Print", self)
		undo_action = QAction("Undo", self)
		redo_action = QAction("Redo", self)
		cut_action = QAction("Cut", self)
		copy_action = QAction("Copy", self)
		paste_action = QAction("Paste", self)
		select_action = QAction("Select all", self)
		wrap_action = QAction("Wrap text to window", self)
		colorAction = QAction("Color", self)
		fontButton = QAction('Font ', self)
		printPreviewAction = QAction("Print Preview", self)

		save_file_action.setShortcut("Ctrl+S")
		print_action.setShortcut("Ctrl+P")
		undo_action.setShortcut("Ctrl+Z")
		redo_action.setShortcut("Ctrl+R")
		cut_action.setShortcut("Ctrl+X")
		copy_action.setShortcut("Ctrl+C")
		paste_action.setShortcut("Ctrl+V")
		select_action.setShortcut("Ctrl+A")
		open_file_action.setShortcut("Ctrl+O")


		open_file_action.setStatusTip("Open file")
		save_file_action.setStatusTip("Save current page")
		saveas_file_action.setStatusTip("Save current page to specified file")
		fontButton.setStatusTip("change the font size")
		saveas_pdf_action.setStatusTip("Save the file as pdf")
		print_action.setStatusTip("Print current page")
		undo_action.setStatusTip("Undo last change")
		redo_action.setStatusTip("Redo last change")
		cut_action.setStatusTip("Cut selected text")
		copy_action.setStatusTip("Copy selected text")
		paste_action.setStatusTip("Paste from clipboard")
		select_action.setStatusTip("Select all text")
		wrap_action.setStatusTip("Check to wrap text to window")
		printPreviewAction.setStatusTip("Preview the file") 

		file_menu.addAction(open_file_action)
		file_menu.addAction(save_file_action)
		file_menu.addAction(saveas_file_action)
		file_menu.addAction(saveas_pdf_action)
		file_menu.addAction(print_action)
		file_menu.addAction(printPreviewAction)

		file_toolbar.addAction(open_file_action)
		file_toolbar.addAction(save_file_action)
		file_toolbar.addAction(print_action)


		edit_menu.addAction(undo_action)
		edit_menu.addAction(redo_action)
		edit_menu.addAction(cut_action)
		edit_menu.addAction(copy_action)
		edit_menu.addAction(paste_action)
		edit_menu.addAction(select_action)
		edit_menu.addAction(wrap_action)


		toolsMenu.addAction(fontButton)
		toolsMenu.addAction(colorAction)  

		edit_toolbar.addAction(fontButton)
		edit_toolbar.addAction(colorAction)
		edit_toolbar.addAction(printPreviewAction)



		wrap_action.setCheckable(True)
		wrap_action.setChecked(True)
		 
		
		open_file_action.triggered.connect(self.file_open)
		print_action.triggered.connect(self.file_print)
		save_file_action.triggered.connect(self.file_save)
		saveas_file_action.triggered.connect(self.file_saveas)
		saveas_pdf_action.triggered.connect(self.downloadPDF)
		wrap_action.triggered.connect(self.edit_toggle_wrap)
		undo_action.triggered.connect(self.editor.undo) 
		redo_action.triggered.connect(self.editor.redo)
		cut_action.triggered.connect(self.editor.cut) 
		copy_action.triggered.connect(self.editor.copy)
		paste_action.triggered.connect(self.editor.paste)
		select_action.triggered.connect(self.editor.selectAll)
		fontButton.triggered.connect(self.font_set)
		colorAction.triggered.connect(self.colorDialog)
		printPreviewAction.triggered.connect(self.printpreviewDialog)

	def font_set(self):
		font, ok = QFontDialog.getFont(self.editor.font(), self)
		if ok:
			self.editor.setFont(font)

	def colorDialog(self):
		color = QColorDialog.getColor()
		self.editor.setTextColor(color)
		

	def printpreviewDialog(self):
		printer = QPrinter(QPrinter.HighResolution)
		previewDialog = QPrintPreviewDialog(printer, self)
		previewDialog.paintRequested.connect(self.printPreview)
		previewDialog.exec_()


	def downloadPDF(self):
		fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF files (.pdf);;All Files()')
		if fn != '':
			if QFileInfo(fn).suffix() == "" : fn += '.pdf'
			printer = QPrinter(QPrinter.HighResolution)
			printer.setOutputFormat(QPrinter.PdfFormat)
			printer.setOutputFileName(fn)
			self.editor.document().print_(printer)

	def printPreview(self, printer):
		self.editor.print_(printer)


	def Title(self):

		self.setWindowTitle("%s - Python NotePad" %(os.path.basename(self.path) if self.path else "Untitled"))


	def dialog_critical(self, s):

		dlg = QMessageBox(self)
		dlg.setText(s)
		dlg.setIcon(QMessageBox.Critical)
		dlg.show()

	def file_open(self):

		path, _ = QFileDialog.getOpenFileName(self, "Open file", "","Text documents (*.txt);All files (*.*)")
		if path:
			try:
				with open(path,'rU') as f:
					text = f.read()

			except Exception as e:
				
				self.dialog_critical(str(e))

			else:

				self.path = path
				self.editor.setPlainText(text)
				self.Title()


	def file_save(self):

		if self.path is None:
			return self.file_saveas()

		self._save_to_path(self.path)


	def file_saveas(self):

		path, _ = QFileDialog.getSaveFileName(self, "Save file", "","Text documents (*.txt);All files (*.*)")

		if not path:
			return

		self._save_to_path(path)

	def _save_to_path(self,path):

		text = self.editor.toPlainText()
		try:
			with open(path,'w') as f:
				f.write(text)

		except Exception as e:
			
			self.dialog_critical(str(e))

		else:
			self.path = path
			self.Title()


	def file_print(self):

		dlg = QPrintDialog()

		if dlg.exec_():
			self.editor.print_(dlg.printer())

	def edit_toggle_wrap(self):

		self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 )


def main():
	app = QApplication(sys.argv)
	app.setApplicationName("Python NotePad")
	window = Window()
	sys.exit(app.exec())

if __name__ == '__main__':
	main()