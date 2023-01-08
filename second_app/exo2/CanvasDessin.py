from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Trace import *

class CanvasDessin(QWidget):
    
    def  __init__(self,color):
         super().__init__()
         self.setMinimumSize(300, 300)
         self.traces = []
         self.trace = []
         self.tracecolor=color
         
    def mouseMoveEvent(self, event):
        point = event.pos()
        self.trace.append((point.x(), point.y()))
        self.update()
        
    def mouseReleaseEvent(self, event):
        point = event.pos()
        self.trace.append((point.x(), point.y()))
        trc = Trace(30, Qt.red)
        for p in self.trace:
            trc.addPoint(p)
        self.traces.append(trc)
        self.update()
        self.trace=[]
            
    def paintEvent(self, event):
            path = QPainterPath() 
            painter = QPainter(self)
            pen = QPen(self.tracecolor)
            pen.setWidth(5)
            painter.setPen(pen)
            for trace in self.traces:
                path.moveTo(self.firstPoint(trace)[0], self.firstPoint(trace)[1])    
                for point in trace.getPoints():
                    path.lineTo(point[0], point[1])
            painter.drawPath(path)


    def firstPoint(self, trace):
        points = trace.getPoints()
        point = points[0]
        return point