# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:39:15 2019

@author: satchane
"""

import sys
from PyQt5 import QtGui, QtWidgets

def on_va_voir() :
    global click_count
    click_count = click_count + 1
    print("on a vu", click_count, "fois")
      

def main () :
    
    def create_button(x, y, t, cb) : 
        button = QtWidgets.QPushButton("x" , window)
        button.move( 10 + 100*x , 10+ 100*y )
        button.clicked.connect(on_va_voir)
    
    global click_count 
    click_count = 0
    global window
    global button
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.resize(500, 450)
   
    
            
    create_button( 0, 0, "C",    on_va_voir)
    create_button( 1, 0, "AC",   on_va_voir)
    create_button( 2, 0, "√",    on_va_voir)
    create_button( 3, 0, "=",    on_va_voir)
    create_button( 0, 1, "7",    on_va_voir)
    create_button( 1, 1, "8",    on_va_voir)
    create_button( 2, 1, "9",    on_va_voir)
    create_button( 3, 1, "+",    on_va_voir)
    create_button( 0, 2, "4",    on_va_voir)
    create_button( 1, 2, "5",    on_va_voir)
    create_button( 2, 2, "6",    on_va_voir)
    create_button( 3, 2, "-",    on_va_voir)
    create_button( 0, 3, "1",    on_va_voir)
    create_button( 1, 3, "2",    on_va_voir)
    create_button( 2, 3, "3",    on_va_voir)
    create_button( 3, 3, "*",    on_va_voir)
    create_button( 0, 4, ".",    on_va_voir)
    create_button( 1, 4, "0",    on_va_voir)
    create_button( 2, 4, "+/-",  on_va_voir)
    create_button( 3, 4, "/",    on_va_voir)

    
    window.show()
    sys.exit(app.exec_())
    

main()    