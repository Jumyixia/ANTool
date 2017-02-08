'''
Created on 2017年2月7日

@author: oo
'''


from PyQt5.QtWidgets import QScrollArea,QSizePolicy,QMainWindow,QLabel
from PyQt5.QtGui import QImage, QPalette, QPixmap,QTransform



class ImageViewer(QMainWindow):

    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)

        self.scaleFactor = 0.0

        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        # self.scrollArea.setBackgroundRole(QPalette.Dark)
        # self.scrollArea.setWidget(self.imageLabel)
        # self.setCentralWidget(self.scrollArea)
        self.setCentralWidget(self.imageLabel)
        self.setWindowTitle("Image Viewer")

    def showpic(self, filepath, maxSize, minSize,rotote):
        # super(ImageViewer, self).showpic(filepath,maxSize,minSize)
        self.resize(minSize, maxSize)
        martix = QTransform()  
        martix.rotate(rotote) 
        
        image = QImage(filepath)
        image = image.transformed(martix)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.scaleFactor = 1.0
        self.imageLabel.adjustSize()
