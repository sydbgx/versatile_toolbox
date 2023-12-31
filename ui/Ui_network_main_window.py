# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'network_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(798, 675)
        mainWindow.setMinimumSize(QtCore.QSize(600, 400))
        mainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/logo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_connect = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_connect.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/disconnect"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_connect.setIcon(icon1)
        self.btn_connect.setObjectName("btn_connect")
        self.gridLayout.addWidget(self.btn_connect, 3, 0, 1, 2)
        self.edit_target_ip = QtWidgets.QLineEdit(self.groupBox)
        self.edit_target_ip.setObjectName("edit_target_ip")
        self.gridLayout.addWidget(self.edit_target_ip, 1, 1, 1, 1)
        self.edit_target_port = QtWidgets.QLineEdit(self.groupBox)
        self.edit_target_port.setObjectName("edit_target_port")
        self.gridLayout.addWidget(self.edit_target_port, 2, 1, 1, 1)
        self.edit_client_model = QtWidgets.QComboBox(self.groupBox)
        self.edit_client_model.setMaximumSize(QtCore.QSize(16777215, 25))
        self.edit_client_model.setObjectName("edit_client_model")
        self.edit_client_model.addItem("")
        self.edit_client_model.addItem("")
        self.edit_client_model.addItem("")
        self.gridLayout.addWidget(self.edit_client_model, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.edit_recv = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edit_recv.setObjectName("edit_recv")
        self.verticalLayout_2.addWidget(self.edit_recv)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.edit_local_ip = QtWidgets.QComboBox(self.centralwidget)
        self.edit_local_ip.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edit_local_ip.setObjectName("edit_local_ip")
        self.horizontalLayout_2.addWidget(self.edit_local_ip)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.edit_local_port = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_local_port.setMaximumSize(QtCore.QSize(100, 30))
        self.edit_local_port.setObjectName("edit_local_port")
        self.horizontalLayout_2.addWidget(self.edit_local_port)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_send = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edit_send.setMaximumSize(QtCore.QSize(16777215, 100))
        self.edit_send.setObjectName("edit_send")
        self.horizontalLayout.addWidget(self.edit_send)
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_send.sizePolicy().hasHeightForWidth())
        self.btn_send.setSizePolicy(sizePolicy)
        self.btn_send.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout.addWidget(self.btn_send)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.setStretch(1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "网络调试助手"))
        self.groupBox.setTitle(_translate("mainWindow", "网络设置"))
        self.btn_connect.setText(_translate("mainWindow", "进行连接"))
        self.edit_target_ip.setInputMask(_translate("mainWindow", "000.000.000.000;_"))
        self.edit_target_port.setInputMask(_translate("mainWindow", "99999"))
        self.edit_client_model.setItemText(0, _translate("mainWindow", "TCP客户端"))
        self.edit_client_model.setItemText(1, _translate("mainWindow", "TCP服务器"))
        self.edit_client_model.setItemText(2, _translate("mainWindow", "UDP"))
        self.label_2.setText(_translate("mainWindow", "服务器IP:"))
        self.label_3.setText(_translate("mainWindow", "服务器端口:"))
        self.label.setText(_translate("mainWindow", "设置模式:"))
        self.label_4.setText(_translate("mainWindow", "本地IP"))
        self.label_6.setText(_translate("mainWindow", "本地端口:"))
        self.btn_send.setText(_translate("mainWindow", "发送"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuAbout.setTitle(_translate("mainWindow", "About"))


from ui import resource_rc
