# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ANTool(object):
    def setupUi(self, ANTool):
        ANTool.setObjectName("ANTool")
        ANTool.resize(674, 598)
        ANTool.setMaximumSize(QtCore.QSize(8777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ANTool.setWindowIcon(icon)
        ANTool.setWindowOpacity(1.0)
        ANTool.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(ANTool)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 86, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 30, 481, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.devicelist = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.devicelist.setFont(font)
        self.devicelist.setObjectName("devicelist")
        self.verticalLayout_2.addWidget(self.devicelist)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.apkpath = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.apkpath.setEnabled(True)
        self.apkpath.setMaximumSize(QtCore.QSize(8777, 16777215))
        self.apkpath.setBaseSize(QtCore.QSize(133, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.apkpath.setFont(font)
        self.apkpath.setMaxLength(12752)
        self.apkpath.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.apkpath.setObjectName("apkpath")
        self.horizontalLayout.addWidget(self.apkpath)
        self.changepath = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.changepath.setFont(font)
        self.changepath.setObjectName("changepath")
        self.horizontalLayout.addWidget(self.changepath)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.apklist = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.apklist.setMinimumSize(QtCore.QSize(250, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.apklist.setFont(font)
        self.apklist.setObjectName("apklist")
        self.horizontalLayout_8.addWidget(self.apklist)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.overinstall = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.overinstall.setFont(font)
        self.overinstall.setChecked(True)
        self.overinstall.setObjectName("overinstall")
        self.horizontalLayout_2.addWidget(self.overinstall)
        self.reinstall = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reinstall.setFont(font)
        self.reinstall.setObjectName("reinstall")
        self.horizontalLayout_2.addWidget(self.reinstall)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.packagename = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.packagename.setFont(font)
        self.packagename.setObjectName("packagename")
        self.verticalLayout_2.addWidget(self.packagename)
        self.startactivity = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.startactivity.setFont(font)
        self.startactivity.setObjectName("startactivity")
        self.verticalLayout_2.addWidget(self.startactivity)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 230, 611, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 250, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_install = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_install.setFont(font)
        self.btn_install.setObjectName("btn_install")
        self.horizontalLayout_3.addWidget(self.btn_install)
        self.btn_unitstall = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_unitstall.setFont(font)
        self.btn_unitstall.setObjectName("btn_unitstall")
        self.horizontalLayout_3.addWidget(self.btn_unitstall)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 290, 239, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_startapp = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_startapp.setFont(font)
        self.btn_startapp.setObjectName("btn_startapp")
        self.horizontalLayout_4.addWidget(self.btn_startapp)
        self.btn_closeapp = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_closeapp.setFont(font)
        self.btn_closeapp.setObjectName("btn_closeapp")
        self.horizontalLayout_4.addWidget(self.btn_closeapp)
        self.btn_closeapppid = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_closeapppid.setFont(font)
        self.btn_closeapppid.setObjectName("btn_closeapppid")
        self.horizontalLayout_4.addWidget(self.btn_closeapppid)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 330, 118, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_getcuractivity = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_getcuractivity.setFont(font)
        self.btn_getcuractivity.setObjectName("btn_getcuractivity")
        self.horizontalLayout_5.addWidget(self.btn_getcuractivity)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 370, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalLayoutWidget_4.setFont(font)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_screencut = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_screencut.setFont(font)
        self.btn_screencut.setObjectName("btn_screencut")
        self.horizontalLayout_6.addWidget(self.btn_screencut)
        self.btn_clearcache = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_clearcache.setObjectName("btn_clearcache")
        self.horizontalLayout_6.addWidget(self.btn_clearcache)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 420, 601, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 440, 571, 111))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_resultclean = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_resultclean.setObjectName("btn_resultclean")
        self.horizontalLayout_7.addWidget(self.btn_resultclean)
        self.text_result = QtWidgets.QTextEdit(self.horizontalLayoutWidget_5)
        self.text_result.setObjectName("text_result")
        self.horizontalLayout_7.addWidget(self.text_result)
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(490, 210, 111, 23))
        self.btn_reset.setObjectName("btn_reset")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1, 1))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 16, 16))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label_6.raise_()
        self.line.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.line_2.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.btn_reset.raise_()
        ANTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ANTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 23))
        self.menubar.setObjectName("menubar")
        ANTool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ANTool)
        self.statusbar.setObjectName("statusbar")
        ANTool.setStatusBar(self.statusbar)

        self.retranslateUi(ANTool)
        self.btn_resultclean.clicked.connect(self.text_result.clear)
        QtCore.QMetaObject.connectSlotsByName(ANTool)
        ANTool.setTabOrder(self.devicelist, self.apkpath)
        ANTool.setTabOrder(self.apkpath, self.overinstall)
        ANTool.setTabOrder(self.overinstall, self.reinstall)
        ANTool.setTabOrder(self.reinstall, self.packagename)
        ANTool.setTabOrder(self.packagename, self.startactivity)
        ANTool.setTabOrder(self.startactivity, self.btn_reset)
        ANTool.setTabOrder(self.btn_reset, self.btn_install)
        ANTool.setTabOrder(self.btn_install, self.btn_unitstall)
        ANTool.setTabOrder(self.btn_unitstall, self.btn_startapp)
        ANTool.setTabOrder(self.btn_startapp, self.btn_closeapp)
        ANTool.setTabOrder(self.btn_closeapp, self.btn_closeapppid)
        ANTool.setTabOrder(self.btn_closeapppid, self.btn_getcuractivity)
        ANTool.setTabOrder(self.btn_getcuractivity, self.btn_screencut)
        ANTool.setTabOrder(self.btn_screencut, self.btn_resultclean)
        ANTool.setTabOrder(self.btn_resultclean, self.text_result)
        ANTool.setTabOrder(self.text_result, self.scrollArea)

    def retranslateUi(self, ANTool):
        _translate = QtCore.QCoreApplication.translate
        ANTool.setWindowTitle(_translate("ANTool", "ANTool"))
        self.label.setText(_translate("ANTool", "设备列表："))
        self.label_2.setText(_translate("ANTool", "APK列表："))
        self.label_3.setText(_translate("ANTool", "安装方式："))
        self.label_4.setText(_translate("ANTool", "应用包名："))
        self.label_5.setText(_translate("ANTool", "启动Activity："))
        self.apkpath.setText(_translate("ANTool", "./"))
        self.changepath.setText(_translate("ANTool", "切换目录"))
        self.overinstall.setText(_translate("ANTool", "覆盖安装"))
        self.reinstall.setText(_translate("ANTool", "卸载重装"))
        self.packagename.setText(_translate("ANTool", "com.happyteam.dubbingshow"))
        self.startactivity.setText(_translate("ANTool", "com.happyteam.dubbingshow.ui.StartActivity"))
        self.label_6.setText(_translate("ANTool", "基本设置"))
        self.btn_install.setText(_translate("ANTool", "安装"))
        self.btn_unitstall.setText(_translate("ANTool", "卸载"))
        self.btn_startapp.setText(_translate("ANTool", "启动应用"))
        self.btn_closeapp.setText(_translate("ANTool", "关闭应用"))
        self.btn_closeapppid.setText(_translate("ANTool", "关闭进程"))
        self.btn_getcuractivity.setText(_translate("ANTool", "获取当前Activity"))
        self.btn_screencut.setText(_translate("ANTool", "截图"))
        self.btn_clearcache.setText(_translate("ANTool", "清除应用数据"))
        self.btn_resultclean.setText(_translate("ANTool", "清空"))
        self.btn_reset.setText(_translate("ANTool", "重置设备&APK列表"))