# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidnow_petinsert.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1325, 879)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(360, 430, 881, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.acquisition = QtWidgets.QWidget()
        self.acquisition.setObjectName("acquisition")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.acquisition)
        self.doubleSpinBox.setGeometry(QtCore.QRect(20, 30, 181, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label = QtWidgets.QLabel(self.acquisition)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.acquisition)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 171, 16))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.acquisition)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(20, 80, 181, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.acquisition)
        self.checkBox.setGeometry(QtCore.QRect(220, 30, 141, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.acquisition)
        self.checkBox_2.setGeometry(QtCore.QRect(220, 80, 141, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_startAquisition = QtWidgets.QPushButton(self.acquisition)
        self.pushButton_startAquisition.setGeometry(QtCore.QRect(100, 170, 113, 32))
        self.pushButton_startAquisition.setObjectName("pushButton_startAquisition")
        self.lcdNumber_CountRate = QtWidgets.QLCDNumber(self.acquisition)
        self.lcdNumber_CountRate.setGeometry(QtCore.QRect(430, 40, 431, 61))
        self.lcdNumber_CountRate.setObjectName("lcdNumber_CountRate")
        self.label_3 = QtWidgets.QLabel(self.acquisition)
        self.label_3.setGeometry(QtCore.QRect(750, 10, 121, 31))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.acquisition, "")
        self.system = QtWidgets.QWidget()
        self.system.setObjectName("system")
        self.pushButton_ResetBackend = QtWidgets.QPushButton(self.system)
        self.pushButton_ResetBackend.setGeometry(QtCore.QRect(30, 30, 151, 32))
        self.pushButton_ResetBackend.setObjectName("pushButton_ResetBackend")
        self.label_4 = QtWidgets.QLabel(self.system)
        self.label_4.setGeometry(QtCore.QRect(220, 30, 261, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_quary = QtWidgets.QPushButton(self.system)
        self.pushButton_quary.setGeometry(QtCore.QRect(30, 60, 151, 32))
        self.pushButton_quary.setObjectName("pushButton_quary")
        self.pushButton_temperature = QtWidgets.QPushButton(self.system)
        self.pushButton_temperature.setGeometry(QtCore.QRect(30, 90, 151, 32))
        self.pushButton_temperature.setObjectName("pushButton_temperature")
        self.pushButton_current = QtWidgets.QPushButton(self.system)
        self.pushButton_current.setGeometry(QtCore.QRect(30, 120, 151, 32))
        self.pushButton_current.setObjectName("pushButton_current")
        self.pushButton_powerStatus = QtWidgets.QPushButton(self.system)
        self.pushButton_powerStatus.setGeometry(QtCore.QRect(30, 150, 151, 32))
        self.pushButton_powerStatus.setObjectName("pushButton_powerStatus")
        self.pushButton_powerUp = QtWidgets.QPushButton(self.system)
        self.pushButton_powerUp.setGeometry(QtCore.QRect(30, 210, 151, 51))
        self.pushButton_powerUp.setMouseTracking(True)
        self.pushButton_powerUp.setObjectName("pushButton_powerUp")
        self.pushButton_bias = QtWidgets.QPushButton(self.system)
        self.pushButton_bias.setGeometry(QtCore.QRect(210, 211, 151, 51))
        self.pushButton_bias.setObjectName("pushButton_bias")
        self.label_6 = QtWidgets.QLabel(self.system)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 111, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.system)
        self.label_7.setGeometry(QtCore.QRect(210, 190, 151, 16))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.system, "")
        self.setting = QtWidgets.QWidget()
        self.setting.setObjectName("setting")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.setting)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 40, 721, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.lineEdit_directory = QtWidgets.QLineEdit(self.setting)
        self.lineEdit_directory.setGeometry(QtCore.QRect(32, 110, 701, 31))
        self.lineEdit_directory.setObjectName("lineEdit_directory")
        self.pushButton_directory = QtWidgets.QPushButton(self.setting)
        self.pushButton_directory.setGeometry(QtCore.QRect(740, 110, 100, 32))
        self.pushButton_directory.setObjectName("pushButton_directory")
        self.tabWidget.addTab(self.setting, "")
        self.groupBox_ActivityLog = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ActivityLog.setGeometry(QtCore.QRect(10, 420, 351, 331))
        self.groupBox_ActivityLog.setObjectName("groupBox_ActivityLog")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_ActivityLog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 331, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 830, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_Viewer = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Viewer.setGeometry(QtCore.QRect(19, 29, 1221, 381))
        self.groupBox_Viewer.setObjectName("groupBox_Viewer")
        self.label_ucdavisLogo = QtWidgets.QLabel(self.centralwidget)
        self.label_ucdavisLogo.setGeometry(QtCore.QRect(1100, 0, 141, 41))
        self.label_ucdavisLogo.setText("")
        self.label_ucdavisLogo.setPixmap(QtGui.QPixmap(":/ucdlogo/UCDlogo.png"))
        self.label_ucdavisLogo.setObjectName("label_ucdavisLogo")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 771, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.label_statusLed = QtWidgets.QLabel(self.centralwidget)
        self.label_statusLed.setGeometry(QtCore.QRect(1210, 760, 21, 21))
        self.label_statusLed.setAutoFillBackground(False)
        self.label_statusLed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_statusLed.setText("")
        self.label_statusLed.setPixmap(QtGui.QPixmap(":/red/red-light-icon-8.png"))
        self.label_statusLed.setObjectName("label_statusLed")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1110, 760, 111, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1325, 24))
        self.menubar.setObjectName("menubar")
        self.menuPET_Insert = QtWidgets.QMenu(self.menubar)
        self.menuPET_Insert.setObjectName("menuPET_Insert")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setToolTipsVisible(True)
        self.menutest.setObjectName("menutest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPET_Insert.menuAction())
        self.menubar.addAction(self.menutest.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Acquisition time (minutes)"))
        self.label_2.setText(_translate("MainWindow", "Singles to acquire"))
        self.checkBox.setText(_translate("MainWindow", "Timed acquisition"))
        self.checkBox_2.setText(_translate("MainWindow", "Count acquisition"))
        self.pushButton_startAquisition.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Acq.  Count Rate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.acquisition), _translate("MainWindow", "Acquisition"))
        self.pushButton_ResetBackend.setText(_translate("MainWindow", "Reset Backend"))
        self.label_4.setText(_translate("MainWindow", "Reset backend and power down  frontend"))
        self.pushButton_quary.setText(_translate("MainWindow", "Query "))
        self.pushButton_temperature.setText(_translate("MainWindow", "Temperature"))
        self.pushButton_current.setText(_translate("MainWindow", "current"))
        self.pushButton_powerStatus.setText(_translate("MainWindow", "Power Status"))
        self.pushButton_powerUp.setText(_translate("MainWindow", "Power "))
        self.pushButton_bias.setText(_translate("MainWindow", "Bias on/off"))
        self.label_6.setText(_translate("MainWindow", "system power"))
        self.label_7.setText(_translate("MainWindow", "Detector bias voltage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.system), _translate("MainWindow", "System"))
        self.pushButton_directory.setText(_translate("MainWindow", "directory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), _translate("MainWindow", "Settings"))
        self.groupBox_ActivityLog.setTitle(_translate("MainWindow", "Activity Log"))
        self.groupBox_Viewer.setTitle(_translate("MainWindow", "Viewer"))
        self.label_5.setText(_translate("MainWindow", "PET Insert Acquisition Software"))
        self.label_8.setText(_translate("MainWindow", "system power"))
        self.menuPET_Insert.setTitle(_translate("MainWindow", "PET Insert"))
        self.menutest.setTitle(_translate("MainWindow", "test"))
import led_rc
import ucdavis_logo_rc
