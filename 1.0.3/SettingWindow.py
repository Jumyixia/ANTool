'''
Created on 2017年2月7日

@author: oo
'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Ui_Config import Ui_Form
from config import Config



class SettingWindow(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(SettingWindow, self).__init__(parent)
        self.config = Config()
        self.setupUi(self)
        self.GetProfileInfo()
        
        self.btn_changepath.clicked.connect(self.ChangePath)
        self.btn_changepath_2.clicked.connect(self.ChangePath2)
        
        self.btn_save.clicked.connect(self.SaveToProfile)

    def GetProfileInfo(self):
        global profiledict
        profiledict = self.config.initConfig()
        
        if "tcp_ip" in profiledict and "apk_path" in profiledict and "packagename" in profiledict and "startactivity" in profiledict and "cutpic_path" in profiledict:
            self.connectip.setText(profiledict["tcp_ip"])
            self.packagename.setText(profiledict["packagename"])
            self.startactivity.setText(profiledict["startactivity"])
            self.apkpath.setText(profiledict["apk_path"])
            self.picpath.setText(profiledict["cutpic_path"])

        else:
            QMessageBox.warning(
                self, "警告", "配置文件有错，请删除配置文件后重启应用", QMessageBox.Yes)

    def SaveToProfile(self):
        global profiledict
        
        profiledict["tcp_ip"] = self.connectip.text()
        profiledict["packagename"] = self.packagename.text()
        profiledict["startactivity"] = self.startactivity.text()
        profiledict["apk_path"] = self.apkpath.text()
        profiledict["cutpic_path"] = self.picpath.text()
        
        self.config.changeConfig(**profiledict)


        QMessageBox.warning(
            self, "信息", "保存成功,请在主界面点击重置按钮", QMessageBox.Yes)
        
        self.close()
        
    def ChangePath(self):

        cpath = QFileDialog()
        # path=open.getOpenFileNames()
        # self.path=open.getOpenFileNames()

        path = cpath.getExistingDirectory()
        
        self.apkpath.setText(str(path))
    
    def ChangePath2(self):
        cpath = QFileDialog()
        # path=open.getOpenFileNames()
        # self.path=open.getOpenFileNames()

        path = cpath.getExistingDirectory()
        
        self.picpath.setText(str(path))
