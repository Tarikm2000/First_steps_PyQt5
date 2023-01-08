
from CanvasDessin import CanvasDessin
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
import sys
from PyQt5.QtGui import QPainter, QColor


class Dessin(QMainWindow):
		def __init__(self):
			super().__init__() 
			toolbar=self.addToolBar('Toolbar')
			self.slider=QSlider(Qt.Horizontal)
			self.color = self.toolBar()
			toolbar.addWidget(self.slider)
			self.canvasDessin = CanvasDessin(self.color)
			self.setCentralWidget(self.canvasDessin)
			
				
						
		def toolBar(self):
			colorDialog = QColorDialog()
			return colorDialog.getColor()

		

def main(args):
		
		app=QApplication(args)
		win=Dessin()
		win.resize(500,300)
		win.show()
		app.exec_()


if __name__ == "__main__":
		main(sys.argv)