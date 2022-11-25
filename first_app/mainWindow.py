import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5 import QtWidgets



class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

			

	def initWindow(self):
		self.resize(500,500)
		bar=self.menuBar()
		fileMenu=bar.addMenu( "Fichier")
		fileToolBar = self.addToolBar("file")

		newAct = QAction(QIcon("open.png"), "Open...", self )
		newAct.setShortcut("Ctrl+O")
		fileToolBar.addAction(newAct)
		newAct.setToolTip(self.tr("Open"))
		newAct.setStatusTip(self.tr("Open"))
		fileMenu.addAction(newAct)
		newAct.triggered.connect(self.openFile)

		newAct1=QAction(QIcon("save.png"),"Save...", self)
		newAct1.setShortcut("Ctrl+S")
		fileToolBar.addAction(newAct1)
		newAct1.setToolTip(self.tr("Save"))
		newAct1.setStatusTip(self.tr("Save"))
		fileMenu.addAction(newAct1)
		newAct1.triggered.connect(self.saveFile)

		newAct2=QAction(QIcon("copy.png"),"Copy...", self)
		newAct2.setShortcut("Ctrl+C")
		fileToolBar.addAction(newAct2)
		newAct2.setToolTip(self.tr("Copy"))
		newAct2.setStatusTip(self.tr("Copy"))
		fileMenu.addAction(newAct2)

		newAct3=QAction(QIcon("quit.png"),"Quit...", self)
		newAct3.setShortcut("Ctrl+Q")
		fileToolBar.addAction(newAct3)
		newAct3.setToolTip(self.tr("Quit"))
		newAct3.setStatusTip(self.tr("Quit"))
		fileMenu.addAction(newAct3)
		newAct3.triggered.connect(self.quitApp)

		self.textEdit=QTextEdit(self)
		self.setCentralWidget(self.textEdit)
		self.statusBar()



	
	def openFile(self):
		fileName =QFileDialog.getOpenFileName(self)	
		fd=QFile(fileName[0])
		fd.open(QFile.ReadOnly)
		data=QTextStream(fd)
		text=data.readAll()
		self.textEdit.setHtml(text)

			
		
	
	def saveFile(self):
		name, _ = QFileDialog.getSaveFileName(self)  # j'ai du mettre name un tuple parce que sinon ça marchait pas ,j'avais un message d'erreur
		file = open(name, 'w')
		text = self.textEdit.toPlainText()
		file.write(text)
		file.close()


		
	def quitApp(self):
		reply = QMessageBox.question(self, 'MessageBox', 'Are you sure ?',QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			print("See you soon")
			sys.exit(0)
		else:
			print(" You have chosen to stay ")
				



	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Window close ', 'Are you sure ?',QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
			print("See you soon")
			self.close()	
		else:
			event.ignore()
			print("You have chosen to stay")
					



def main(args):
		app = QApplication(args)
		#print(args)
		win=MainWindow()
		win.initWindow()
		win.show()
		app.exec_()


if __name__ == "__main__":
	print("execution du programme")
	main(sys.argv)