# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Jul 19 14:52:05 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leftColumn = QtGui.QVBoxLayout()
        self.leftColumn.setObjectName(_fromUtf8("leftColumn"))
        self.mainButtonLayout = QtGui.QHBoxLayout()
        self.mainButtonLayout.setObjectName(_fromUtf8("mainButtonLayout"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setAutoExclusive(False)
        self.startButton.setDefault(True)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.startButton)
        self.mainButtonLayout.addWidget(self.startButton)
        self.leftColumn.addLayout(self.mainButtonLayout)
        self.commandBox = QtGui.QGroupBox(self.centralwidget)
        self.commandBox.setObjectName(_fromUtf8("commandBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.commandBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.commandForm = QtGui.QFormLayout()
        self.commandForm.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.commandForm.setObjectName(_fromUtf8("commandForm"))
        self.tagLabel = QtGui.QLabel(self.commandBox)
        self.tagLabel.setObjectName(_fromUtf8("tagLabel"))
        self.commandForm.setWidget(0, QtGui.QFormLayout.LabelRole, self.tagLabel)
        self.tagLineEdit = QtGui.QLineEdit(self.commandBox)
        self.tagLineEdit.setMaxLength(10)
        self.tagLineEdit.setObjectName(_fromUtf8("tagLineEdit"))
        self.commandForm.setWidget(0, QtGui.QFormLayout.FieldRole, self.tagLineEdit)
        self.bodyLabel = QtGui.QLabel(self.commandBox)
        self.bodyLabel.setObjectName(_fromUtf8("bodyLabel"))
        self.commandForm.setWidget(1, QtGui.QFormLayout.LabelRole, self.bodyLabel)
        self.bodyLineEdit = QtGui.QLineEdit(self.commandBox)
        self.bodyLineEdit.setMaxLength(50)
        self.bodyLineEdit.setObjectName(_fromUtf8("bodyLineEdit"))
        self.commandForm.setWidget(1, QtGui.QFormLayout.FieldRole, self.bodyLineEdit)
        self.verticalLayout.addLayout(self.commandForm)
        self.submitButton = QtGui.QPushButton(self.commandBox)
        self.submitButton.setEnabled(False)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.verticalLayout.addWidget(self.submitButton)
        self.leftColumn.addWidget(self.commandBox)
        self.networkLog = QtGui.QPlainTextEdit(self.centralwidget)
        self.networkLog.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.networkLog.setMaximumBlockCount(50)
        self.networkLog.setCenterOnScroll(False)
        self.networkLog.setObjectName(_fromUtf8("networkLog"))
        self.leftColumn.addWidget(self.networkLog)
        self.leftColumn.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.leftColumn)
        self.rightColumn = QtGui.QVBoxLayout()
        self.rightColumn.setObjectName(_fromUtf8("rightColumn"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.velocityTab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.velocityTab.sizePolicy().hasHeightForWidth())
        self.velocityTab.setSizePolicy(sizePolicy)
        self.velocityTab.setAutoFillBackground(False)
        self.velocityTab.setObjectName(_fromUtf8("velocityTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.velocityTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.velocityPlot = TimePlot(self.velocityTab)
        self.velocityPlot.setObjectName(_fromUtf8("velocityPlot"))
        self.verticalLayout_2.addWidget(self.velocityPlot)
        self.tabWidget.addTab(self.velocityTab, _fromUtf8(""))
        self.heightTab = QtGui.QWidget()
        self.heightTab.setObjectName(_fromUtf8("heightTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.heightTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.heightPlot = TimePlot(self.heightTab)
        self.heightPlot.setObjectName(_fromUtf8("heightPlot"))
        self.verticalLayout_3.addWidget(self.heightPlot)
        self.tabWidget.addTab(self.heightTab, _fromUtf8(""))
        self.distanceTab = QtGui.QWidget()
        self.distanceTab.setObjectName(_fromUtf8("distanceTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.distanceTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.distancePlot = TimePlot(self.distanceTab)
        self.distancePlot.setObjectName(_fromUtf8("distancePlot"))
        self.verticalLayout_4.addWidget(self.distancePlot)
        self.tabWidget.addTab(self.distanceTab, _fromUtf8(""))
        self.uptimeTab = QtGui.QWidget()
        self.uptimeTab.setObjectName(_fromUtf8("uptimeTab"))
        self.tabWidget.addTab(self.uptimeTab, _fromUtf8(""))
        self.rightColumn.addWidget(self.tabWidget)
        self.summaryBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summaryBox.sizePolicy().hasHeightForWidth())
        self.summaryBox.setSizePolicy(sizePolicy)
        self.summaryBox.setObjectName(_fromUtf8("summaryBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.summaryBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.uptimeLCD = QtGui.QLCDNumber(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uptimeLCD.sizePolicy().hasHeightForWidth())
        self.uptimeLCD.setSizePolicy(sizePolicy)
        self.uptimeLCD.setNumDigits(10)
        self.uptimeLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.uptimeLCD.setObjectName(_fromUtf8("uptimeLCD"))
        self.gridLayout_2.addWidget(self.uptimeLCD, 2, 1, 1, 1)
        self.velocityLabel = QtGui.QLabel(self.summaryBox)
        self.velocityLabel.setObjectName(_fromUtf8("velocityLabel"))
        self.gridLayout_2.addWidget(self.velocityLabel, 0, 0, 1, 1)
        self.velocityLCD = QtGui.QLCDNumber(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.velocityLCD.sizePolicy().hasHeightForWidth())
        self.velocityLCD.setSizePolicy(sizePolicy)
        self.velocityLCD.setNumDigits(10)
        self.velocityLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.velocityLCD.setObjectName(_fromUtf8("velocityLCD"))
        self.gridLayout_2.addWidget(self.velocityLCD, 0, 1, 1, 1)
        self.heightLCD = QtGui.QLCDNumber(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightLCD.sizePolicy().hasHeightForWidth())
        self.heightLCD.setSizePolicy(sizePolicy)
        self.heightLCD.setNumDigits(10)
        self.heightLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.heightLCD.setObjectName(_fromUtf8("heightLCD"))
        self.gridLayout_2.addWidget(self.heightLCD, 1, 1, 1, 1)
        self.uptimeLabel = QtGui.QLabel(self.summaryBox)
        self.uptimeLabel.setObjectName(_fromUtf8("uptimeLabel"))
        self.gridLayout_2.addWidget(self.uptimeLabel, 2, 0, 1, 1)
        self.heightLabel = QtGui.QLabel(self.summaryBox)
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))
        self.gridLayout_2.addWidget(self.heightLabel, 1, 0, 1, 1)
        self.distanceLabel = QtGui.QLabel(self.summaryBox)
        self.distanceLabel.setObjectName(_fromUtf8("distanceLabel"))
        self.gridLayout_2.addWidget(self.distanceLabel, 3, 0, 1, 1)
        self.distanceLCD = QtGui.QLCDNumber(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceLCD.sizePolicy().hasHeightForWidth())
        self.distanceLCD.setSizePolicy(sizePolicy)
        self.distanceLCD.setSmallDecimalPoint(False)
        self.distanceLCD.setNumDigits(10)
        self.distanceLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.distanceLCD.setObjectName(_fromUtf8("distanceLCD"))
        self.gridLayout_2.addWidget(self.distanceLCD, 3, 1, 1, 1)
        self.rightColumn.addWidget(self.summaryBox)
        self.horizontalLayout.addLayout(self.rightColumn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuConsole = QtGui.QMenu(self.menubar)
        self.menuConsole.setObjectName(_fromUtf8("menuConsole"))
        self.menuNetwork = QtGui.QMenu(self.menubar)
        self.menuNetwork.setObjectName(_fromUtf8("menuNetwork"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNetwork = QtGui.QAction(MainWindow)
        self.actionNetwork.setObjectName(_fromUtf8("actionNetwork"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionConsoleOpen = QtGui.QAction(MainWindow)
        self.actionConsoleOpen.setObjectName(_fromUtf8("actionConsoleOpen"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionReconnect = QtGui.QAction(MainWindow)
        self.actionReconnect.setObjectName(_fromUtf8("actionReconnect"))
        self.actionTelemetry_Off = QtGui.QAction(MainWindow)
        self.actionTelemetry_Off.setObjectName(_fromUtf8("actionTelemetry_Off"))
        self.actionTelemetry_On = QtGui.QAction(MainWindow)
        self.actionTelemetry_On.setObjectName(_fromUtf8("actionTelemetry_On"))
        self.menuConsole.addAction(self.actionConsoleOpen)
        self.menuNetwork.addAction(self.actionSettings)
        self.menuNetwork.addAction(self.actionReconnect)
        self.menuNetwork.addAction(self.actionTelemetry_Off)
        self.menuNetwork.addAction(self.actionTelemetry_On)
        self.menubar.addAction(self.menuConsole.menuAction())
        self.menubar.addAction(self.menuNetwork.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hyperloop Pod", None))
        self.startButton.setText(_translate("MainWindow", "Begin Interaction", None))
        self.commandBox.setTitle(_translate("MainWindow", "Send a command", None))
        self.tagLabel.setText(_translate("MainWindow", "tag", None))
        self.bodyLabel.setText(_translate("MainWindow", "body", None))
        self.submitButton.setText(_translate("MainWindow", "Submit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.velocityTab), _translate("MainWindow", "Velocity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.heightTab), _translate("MainWindow", "Height", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.distanceTab), _translate("MainWindow", "Distance", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uptimeTab), _translate("MainWindow", "Uptime", None))
        self.summaryBox.setTitle(_translate("MainWindow", "Summary", None))
        self.velocityLabel.setText(_translate("MainWindow", "velocity", None))
        self.uptimeLabel.setText(_translate("MainWindow", "uptime", None))
        self.heightLabel.setText(_translate("MainWindow", "height", None))
        self.distanceLabel.setText(_translate("MainWindow", "distance", None))
        self.menuConsole.setTitle(_translate("MainWindow", "&Console", None))
        self.menuNetwork.setTitle(_translate("MainWindow", "&Network", None))
        self.actionNetwork.setText(_translate("MainWindow", "&Network", None))
        self.actionNew.setText(_translate("MainWindow", "&New", None))
        self.actionConsoleOpen.setText(_translate("MainWindow", "&Open", None))
        self.actionSettings.setText(_translate("MainWindow", "&Settings", None))
        self.actionReconnect.setText(_translate("MainWindow", "&Reconnect", None))
        self.actionTelemetry_Off.setText(_translate("MainWindow", "Telemetry Off", None))
        self.actionTelemetry_On.setText(_translate("MainWindow", "Telemetry On", None))

from hyperloop_app.plot import TimePlot
