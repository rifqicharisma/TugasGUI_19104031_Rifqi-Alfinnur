# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datamhs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import *
from datamhs import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.koneksi()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 621, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtJurusan = QtWidgets.QLineEdit(self.tab)
        self.txtJurusan.setGeometry(QtCore.QRect(170, 380, 361, 20))
        self.txtJurusan.setObjectName("txtJurusan")
        self.NAMA = QtWidgets.QLabel(self.tab)
        self.NAMA.setGeometry(QtCore.QRect(64, 340, 39, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NAMA.setFont(font)
        self.NAMA.setObjectName("NAMA")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(190, 250, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.NO_TELP = QtWidgets.QLabel(self.tab)
        self.NO_TELP.setGeometry(QtCore.QRect(64, 420, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NO_TELP.setFont(font)
        self.NO_TELP.setObjectName("NO_TELP")
        self.txtNim = QtWidgets.QLineEdit(self.tab)
        self.txtNim.setGeometry(QtCore.QRect(170, 303, 361, 20))
        self.txtNim.setObjectName("txtNim")
        self.txtNama = QtWidgets.QLineEdit(self.tab)
        self.txtNama.setGeometry(QtCore.QRect(170, 340, 361, 20))
        self.txtNama.setObjectName("txtNama")
        self.JURUSAN = QtWidgets.QLabel(self.tab)
        self.JURUSAN.setGeometry(QtCore.QRect(64, 380, 57, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JURUSAN.setFont(font)
        self.JURUSAN.setObjectName("JURUSAN")
        self.txtNo = QtWidgets.QLineEdit(self.tab)
        self.txtNo.setGeometry(QtCore.QRect(170, 420, 361, 20))
        self.txtNo.setObjectName("txtNo")
        self.btnSubmit = QtWidgets.QPushButton(self.tab)
        self.btnSubmit.setGeometry(QtCore.QRect(440, 450, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setObjectName("btnSubmit")

        self.btnSubmit.clicked.connect(self.submit)

        self.NIM = QtWidgets.QLabel(self.tab)
        self.NIM.setGeometry(QtCore.QRect(64, 304, 24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NIM.setFont(font)
        self.NIM.setObjectName("NIM")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(220, 30, 191, 211))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("E:/Ripki Alfinnur/ITTP/logo ittp.png"))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(200, 220, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(200, 0, 211, 211))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("E:/Ripki Alfinnur/ITTP/logo ittp.png"))
        self.label_3.setObjectName("label_3")
        self.Username = QtWidgets.QLabel(self.tab_2)
        self.Username.setGeometry(QtCore.QRect(71, 291, 64, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.txtUname = QtWidgets.QLineEdit(self.tab_2)
        self.txtUname.setGeometry(QtCore.QRect(141, 291, 361, 20))
        self.txtUname.setObjectName("txtUname")
        self.Login = QtWidgets.QPushButton(self.tab_2)
        self.Login.setGeometry(QtCore.QRect(420, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")
        self.Login.clicked.connect(self.login)
        self.Password = QtWidgets.QLabel(self.tab_2)
        self.Password.setGeometry(QtCore.QRect(71, 331, 63, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.txtPass = QtWidgets.QLineEdit(self.tab_2)
        self.txtPass.setGeometry(QtCore.QRect(140, 331, 361, 20))
        self.txtPass.setObjectName("txtPass")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NAMA.setText(_translate("MainWindow", "NAMA"))
        self.label.setText(_translate("MainWindow", "FORM MAHASISWA"))
        self.NO_TELP.setText(_translate("MainWindow", "NO TELP"))
        self.JURUSAN.setText(_translate("MainWindow", "JURUSAN"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))
        self.NIM.setText(_translate("MainWindow", "NIM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Form"))
        self.label_2.setText(_translate("MainWindow", "LOGIN ADMIN"))
        self.Username.setText(_translate("MainWindow", "Username"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.Password.setText(_translate("MainWindow", "Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Admin"))
    
    def koneksi(self):
        con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        if(cur):
            self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
            self.messagebox("Koneksi", "Koneksi Gagal")
    
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    
    def submit(self):
        nim = self.txtNim.text()
        nama = self.txtNama.text()
        jurusan = self.txtJurusan.text()
        no = self.txtNo.text()
        insert = (nim, nama, jurusan, no)
        print(insert)
        if self.txtNim.text() and self.txtNama.text() and self.txtJurusan.text() and self.txtNo.text():
            con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "INSERT INTO mhs(nim, nama, jurusan, no)" + "VALUES"+ str(insert)
            data = cur.execute(sql)
            self.messagebox("SUKSES", "Data Berhasil di Submit")
        else:
            self.messagebox("GAGAL", "Mohon lengkapi form ")
    
    def login(self):
        uname = self.txtUname.text()
        pw = self.txtPass.text()
        con = pymysql.connect(db='db_mhs',
        user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "SELECT * from admin where uname=%s and pw=%s"
        data = cur.execute(sql, (uname, pw))
        if(len(cur.fetchall())>0):
            self.form = datamhs()
            self.form.show()
        else:
            self.messagebox("GAGAL", "Username atau Password Salah ! ")

    def submit(self):
        nim = self.datamhs.txtNim_2.text()
        nama = self.datamhs.txtNama_2.text()
        jurusan = self.datamhs.txtJurusan_2.text()
        no = self.datamhs.txtNo_2.text()
        insert = (nim, nama, jurusan, no)
        print(insert)
        if self.datamhs.txtNim_2.text() and self.datamhs.txtNama_2.text() and self.datamhs.txtJurusan_2.text() and self.datamhs.txtNo_2.text(): 
            con = pymysql.connect(db='db_mhs', 
            user='root', passwd='', host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "INSERT INTO mhs(nim, nama, jurusan, no)" + "VALUES"+ str(insert)
            data = cur.execute(sql)
            Ui_MainWindow.messagebox(Ui_MainWindow, "SUKSES", "Data Berhasil di Submit")
        else:
            Ui_MainWindow.messagebox(Ui_MainWindow, "GAGAL", "Mohon lengkapi form ")

class datamhs(QWidget):
    def __init__(self):
        super().__init__()
        self.datamhs - Ui_datamhs()
        self.datamhs.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
