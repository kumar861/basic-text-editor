#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,QMessageBox
from texteditor import *


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNew.triggered.connect(self.newfile)
        self.ui.actionOpen.triggered.connect(self.openfile)
        self.ui.actionSave.triggered.connect(self.savefile)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionCut.triggered.connect(self.cuttext)
        self.ui.actionCopy.triggered.connect(self.copytext)
        self.ui.actionPaste.triggered.connect(self.pastetext)
        self.ui.actionAbout_Qt.triggered.connect(self.aboutqt)
        self.ui.actionAbout.triggered.connect(self.about)
        #self.show()
        
    def newfile(self):
        self.window1 = window()
        self.window1.show()

    def openfile(self):
        fname = QFileDialog().getOpenFileName(self, "File Dialog")[0]
        # if fname[0]:
        f = open(fname, 'r')
        data = f.read()
        self.ui.textEdit.setText(data)

    def savefile(self):
        fname = QFileDialog.getSaveFileName(self, "Save file")
        if fname[0]:
            f = open(fname[0], 'w')
        data = self.ui.textEdit.toPlainText()
        f.write(data)
        f.close()
    
    def exit(self):
        exit = QMessageBox.question(self,"Exit Message","Do You Want to exit",QMessageBox().Yes | QMessageBox().No ,QMessageBox().No)
        if exit == QMessageBox().Yes:
            sys.exit()
            
    def cuttext(self):
        self.ui.textEdit.cut()
        
    def pastetext(self):
        self.ui.textEdit.paste()
        
    def copytext(self):
        self.ui.textEdit.copy()
    
        
    def aboutqt(self):
        about = QMessageBox().aboutQt(self)

    def about(self):
        about = QMessageBox().about(self,"About","Text Editor\nDeveloped In Python And PyQt5\n By @kumar")

app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec_())
