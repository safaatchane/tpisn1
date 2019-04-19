# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:08:38 2019

@author: satchane
"""

import datetime
import math
import signal
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

signal.signal(signal.SIGINT, signal.SIG_DFL)

class Animated_window(QtWidgets.QWidget) :

    def __init__(self) :
        super().__init__()
        self.create_game()
        self.create_contents()
        self.show()
        framerate = 60
        self.animation_start = datetime.datetime.now()
        self.animation_timer = QtCore.QTimer()
        self.animation_timer.timeout.connect(self.animation_step)
        self.animation_timer.start(1000 / framerate)

    def create_contents(self) :
        self.time = 0
        self.setWindowTitle("ISN: example")
        self.resize(800, 600)
        
    def create_game(self):
        self.platform = [
         [5,0,0],
         [0,0,1],
         [1,0,0],
        ]
    def animation_step(self) :
        time = datetime.datetime.now() - self.animation_start
        self.time = time.total_seconds()
        self.update()

    def paintEvent(self, event) :
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHints(QtGui.QPainter.Antialiasing, 1)
        path = QtGui.QPainterPath()
        path.addRect(10, 10, 780, 580)
        path.closeSubpath()
        path.closeSubpath()
        qp.fillPath(path, QtGui.QColor(0, 0, 0))
        #qp.drawPath(path)
        print(self.platform[0][0])
        
    if 
        qp.end()

    def keyPressEvent(self, event):
        key = event.key()
        #print(key)
        if key == QtCore.Qt.Key_Q:
            self.close()
        elif key == QtCore.Qt.Key_Plus :
            self.speed = self.speed + 0.01
        elif key == QtCore.Qt.Key_Minus :
            self.speed = self.speed - 0.01

    def keyReleaseEvent(self, event):
        return

def main() :
    app = QtWidgets.QApplication(sys.argv)
    clock = Animated_window()
    sys.exit(app.exec_())

main()