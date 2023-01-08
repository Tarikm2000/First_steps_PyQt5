
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
import sys
from ButtonModel import ButtonModel 
from PyQt5.QtGui import QPainter, QColor

class CanvasButton(QWidget):
	hoverCol=QColor()
	pressCol=QColor()

	def __init__(self):
		super().__init__()
		self.bbox=QRect(100,100,200,80)	
		self.defaultCol=QColor(150, 163, 39)
		self.setMouseTracking(True)
		self.cursorPos=None
		self.cursorOver=False
		self.buttonModel=ButtonModel()
		self.pressCol=QColor(189, 13, 39)


	

	def mouseMoveEvent(self,event):
		if self.cursorOnEllipse(event.pos()) :
			self.cursorOver=True
			self.buttonModel.enter()
			self.update()
		else :
			self.cursorOver=False
			self.buttonModel.leave()
			self.update()
		#print("mousemoveevent")
				

	def mousePressEvent(self,event):
		self.buttonModel.press()
		self.update()

	def mouseReleaseEvent(self,event):
		self.buttonModel.release()
		#print("mousereleaseEvent")
		self.update()
	
	def paintEvent(self,event):
		QWidget.paintEvent(self,event)
		painter= QPainter(self)
		if self.buttonModel.state==self.buttonModel.hover:
			painter.setBrush(self.hoverCol)
			painter.drawEllipse(self.bbox)
		elif  self.buttonModel.state==self.buttonModel.pressIn :
			painter.setBrush(self.pressCol)
			painter.drawEllipse(self.bbox)
		else:
			painter.setBrush(self.defaultCol)	
			painter.drawEllipse(self.bbox)

	def cursorOnEllipse(self, point):
		r1 = QRegion(self.bbox,QRegion.Ellipse)
		if r1.contains(point):
			return True 
		else:
			return False





def main(args):
		
		app=QApplication(args)
		win=QMainWindow()
		win.setCentralWidget(CanvasButton())
		win.resize(500,300)
		win.show()
		app.exec_()


if __name__ == "__main__":
		main(sys.argv)
