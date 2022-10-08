# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 360)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/1694.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ipv4Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ipv4Edit.setGeometry(QtCore.QRect(10, 30, 220, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ipv4Edit.setFont(font)
        self.ipv4Edit.setText("")
        self.ipv4Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ipv4Edit.setObjectName("ipv4Edit")
        self.btnCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalculate.setGeometry(QtCore.QRect(250, 30, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCalculate.setFont(font)
        self.btnCalculate.setObjectName("btnCalculate")
        self.labelNIps = QtWidgets.QLabel(self.centralwidget)
        self.labelNIps.setGeometry(QtCore.QRect(20, 230, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelNIps.setFont(font)
        self.labelNIps.setObjectName("labelNIps")
        self.labelMask = QtWidgets.QLabel(self.centralwidget)
        self.labelMask.setGeometry(QtCore.QRect(20, 140, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelMask.setFont(font)
        self.labelMask.setObjectName("labelMask")
        self.labelBroadcast = QtWidgets.QLabel(self.centralwidget)
        self.labelBroadcast.setGeometry(QtCore.QRect(20, 200, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBroadcast.setFont(font)
        self.labelBroadcast.setObjectName("labelBroadcast")
        self.labelNetwork = QtWidgets.QLabel(self.centralwidget)
        self.labelNetwork.setGeometry(QtCore.QRect(20, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelNetwork.setFont(font)
        self.labelNetwork.setObjectName("labelNetwork")
        self.networkEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.networkEdit.setGeometry(QtCore.QRect(110, 110, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.networkEdit.setFont(font)
        self.networkEdit.setText("")
        self.networkEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.networkEdit.setObjectName("networkEdit")
        self.maskEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.maskEdit.setGeometry(QtCore.QRect(110, 140, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.maskEdit.setFont(font)
        self.maskEdit.setText("")
        self.maskEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.maskEdit.setObjectName("maskEdit")
        self.broadcastEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.broadcastEdit.setGeometry(QtCore.QRect(110, 200, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.broadcastEdit.setFont(font)
        self.broadcastEdit.setText("")
        self.broadcastEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.broadcastEdit.setObjectName("broadcastEdit")
        self.nIpsEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nIpsEdit.setGeometry(QtCore.QRect(110, 230, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nIpsEdit.setFont(font)
        self.nIpsEdit.setText("")
        self.nIpsEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nIpsEdit.setObjectName("nIpsEdit")
        self.maskOrPrefixEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.maskOrPrefixEdit.setGeometry(QtCore.QRect(10, 60, 220, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.maskOrPrefixEdit.setFont(font)
        self.maskOrPrefixEdit.setText("")
        self.maskOrPrefixEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.maskOrPrefixEdit.setObjectName("maskOrPrefixEdit")
        self.maskOrPrefixComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.maskOrPrefixComboBox.setGeometry(QtCore.QRect(250, 60, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.maskOrPrefixComboBox.setFont(font)
        self.maskOrPrefixComboBox.setObjectName("maskOrPrefixComboBox")
        self.maskOrPrefixComboBox.addItem("")
        self.maskOrPrefixComboBox.addItem("")
        self.labelInvalid = QtWidgets.QLabel(self.centralwidget)
        self.labelInvalid.setGeometry(QtCore.QRect(0, 310, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelInvalid.setFont(font)
        self.labelInvalid.setStyleSheet("color: red;")
        self.labelInvalid.setText("")
        self.labelInvalid.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInvalid.setObjectName("labelInvalid")
        self.labelValid = QtWidgets.QLabel(self.centralwidget)
        self.labelValid.setGeometry(QtCore.QRect(0, 310, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelValid.setFont(font)
        self.labelValid.setStyleSheet("color: green;")
        self.labelValid.setText("")
        self.labelValid.setAlignment(QtCore.Qt.AlignCenter)
        self.labelValid.setObjectName("labelValid")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(20, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.labelPrefix = QtWidgets.QLabel(self.centralwidget)
        self.labelPrefix.setGeometry(QtCore.QRect(20, 170, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelPrefix.setFont(font)
        self.labelPrefix.setObjectName("labelPrefix")
        self.prefixEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.prefixEdit.setGeometry(QtCore.QRect(110, 170, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.prefixEdit.setFont(font)
        self.prefixEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.prefixEdit.setObjectName("prefixEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora IPV4"))
        self.btnCalculate.setText(_translate("MainWindow", "Calcular"))
        self.labelNIps.setText(_translate("MainWindow", "n° de Ips:"))
        self.labelMask.setText(_translate("MainWindow", "Máscara"))
        self.labelBroadcast.setText(_translate("MainWindow", "Broadcast"))
        self.labelNetwork.setText(_translate("MainWindow", "Rede"))
        self.maskOrPrefixComboBox.setItemText(0, _translate("MainWindow", "Prefixo"))
        self.maskOrPrefixComboBox.setItemText(1, _translate("MainWindow", "Máscara"))
        self.btnClear.setText(_translate("MainWindow", "Limpar"))
        self.labelPrefix.setText(_translate("MainWindow", "Prefixo:"))