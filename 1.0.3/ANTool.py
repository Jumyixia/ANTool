#!/usr/bin/python
# -*- coding : utf-8 -*-

from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox



import os
import sys

import subprocess
import time
import datetime
from PIL import Image
from win32api import GetSystemMetrics


from Ui_MainWindow import Ui_ANTool
from config import Config
from SettingWindow import SettingWindow
from ImageViewer import ImageViewer


packageName = 'com.fangyanshow.dialectshow'
comman = "adb devices"
# 设备列表
dict_device = {}
# 复选框对应的设备
dict_devicebox = {}
# 配置文件信息
dict_config = {}
# apk列表
list_apks = []
timefomate = "%Y%m%d%H%M%S"





class MyWindow(QtWidgets.QMainWindow, Ui_ANTool):

    def __init__(self):
        super(MyWindow, self).__init__()
        
        self.setupUi(self)

        self.imageViewer = ImageViewer(self)        
        self.config = Config()      
               
        
        self.btn_connect.clicked.connect(self.connectIp)
        self.btn_getdevices.clicked.connect(self.setDevices)
        self.changepath.clicked.connect(self.changePath)  # 会挂，不能用啊,暂时用来测试功能
        self.btn_reset.clicked.connect(self.WindowInit)
        self.btn_install.clicked.connect(self.installapp)
        self.btn_unitstall.clicked.connect(self.unitstallapp)
        self.btn_screencut.clicked.connect(self.cutscreen)
        self.btn_screencut_HD.clicked.connect(self.cutscreenHD)
        self.btn_resultclean.clicked.connect(self.cleanresult)
        self.btn_clearcache.clicked.connect(self.clearCache)
        self.btn_deviceinfo.clicked.connect(self.GetDeviceInfo)
        
        
        self.menuOptions.addAction(self.actionSettings)
        self.actionSettings.triggered.connect(self.SettingAction)
        self.menuOptions.addAction(self.actionAbouts)
        self.actionAbouts.triggered.connect(self.AhoutAction)
        
        self.WindowInit()

    def WindowInit(self):
        """初始化主界面"""
        global dict_config
        
        dict_config = self.config.initConfig()        
        
        if dict_config["symbol"] == "1":            
            self.settingWindow = SettingWindow(self)
            self.settingWindow.show()
        
        #读取配置信息         
        self.connectip.setText(dict_config["tcp_ip"])
        self.apkpath.setText(dict_config["apk_path"])
        self.packagename.setText(dict_config["packagename"])
        self.startactivity.setText(dict_config["startactivity"])
        
        #调用函数获取设备和apk
        
        self.setDevices()
        self.apklist.clear()
        self.apklist.addItems(self.getapklist())        
            
    def connectIp(self):
        self.text_result.clear()
        
        ip = self.connectip.text()
        
        if ip != "":
            self.exctcmd("adb tcpip 5555")            
            result = self.exctcmd("adb connect " + ip)
            self.text_result.append(result)
            
            if "connected to " in result:
                # adb 有bug，需要等待一会adb devices 才能给出正确结果
                                
                # 将设备以及apk列表/apkpath全部置空/重置
                self.device_1.setText("")
                self.device_2.setText("")
                self.device_3.setText("")
                self.device_4.setText("")
                self.device_5.setText("")
                self.device_6.setText("")
    
                self.setDevices()
        else:
            QMessageBox.warning(
                self, "警告", "请先填写无线设置的ip", QMessageBox.Yes)
        
    def SettingAction(self):
        self.settingWindow = SettingWindow(self)
        self.settingWindow.show()

    def AhoutAction(self):
        QMessageBox.information(self, "Abouts", "Jumyixia飞走了︿(￣︶￣)︿", QMessageBox.Yes)
        
    def setDevices(self):
        """获取设备列表，并dict_device中的设备添加到CheckBox中"""
        
        global dict_devicebox
        
        self.getdeviceslist()
        
        l = list(dict_device.keys())
        a = len(l)
        if a == 0:
            self.device_1.setText("")
            self.device_1.setChecked(False)
            self.device_2.setText("")
            self.device_2.setChecked(False)
            self.device_3.setText("")
            self.device_3.setChecked(False)
            self.device_4.setText("")
            self.device_4.setChecked(False)
            self.device_5.setText("")
            self.device_5.setChecked(False)
            self.device_6.setText("")
            self.device_6.setChecked(False)

        elif a == 1:
            self.device_1.setChecked(True)
            self.device_1.setText(l[0])
            self.device_2.setText("")
            self.device_2.setChecked(False)
            self.device_3.setText("")
            self.device_3.setChecked(False)
            self.device_4.setText("")
            self.device_4.setChecked(False)
            self.device_5.setText("")
            self.device_5.setChecked(False)
            self.device_6.setText("")
            self.device_6.setChecked(False)

        elif a == 2:
            self.device_1.setText(l[0])
            self.device_2.setText(l[1])           
            
            self.device_3.setText("")
            self.device_4.setText("")
            self.device_5.setText("")
            self.device_6.setText("")
            self.device_1.setChecked(True)
            self.device_2.setChecked(False)
            self.device_3.setChecked(False)            
            self.device_4.setChecked(False)            
            self.device_5.setChecked(False)            
            self.device_6.setChecked(False)

        elif a == 3:

            self.device_1.setText(l[0])
            self.device_2.setText(l[1])
            self.device_3.setText(l[2])
            self.device_4.setText("")
            self.device_5.setText("")
            self.device_6.setText("")
            self.device_1.setChecked(True)
            self.device_2.setChecked(False)
            self.device_3.setChecked(False)            
            self.device_4.setChecked(False)            
            self.device_5.setChecked(False)            
            self.device_6.setChecked(False)
        elif a == 4:
            
            self.device_1.setText(l[0])
            self.device_2.setText(l[1])
            self.device_3.setText(l[2])
            self.device_4.setText(l[3])            
            self.device_5.setText("")            
            self.device_6.setText("")
            self.device_1.setChecked(True)
            self.device_2.setChecked(False)
            self.device_3.setChecked(False)            
            self.device_4.setChecked(False)            
            self.device_5.setChecked(False)            
            self.device_6.setChecked(False)
        elif a == 5:            
            self.device_1.setText(l[0])
            self.device_2.setText(l[1])
            self.device_3.setText(l[2])
            self.device_4.setText(l[3])
            self.device_5.setText(l[4])            
            self.device_6.setText("")
            self.device_1.setChecked(True)
            self.device_2.setChecked(False)
            self.device_3.setChecked(False)            
            self.device_4.setChecked(False)            
            self.device_5.setChecked(False)            
            self.device_6.setChecked(False)
        
        elif a >= 6:
            self.device_1.setChecked(True)
            self.device_1.setText(l[0])
            self.device_2.setText(l[1])
            self.device_3.setText(l[2])
            self.device_4.setText(l[3])
            self.device_5.setText(l[4])
            self.device_6.setText(l[5])
        
        dict_devicebox = dict.fromkeys(dict_device.keys(), 0)
    
    def getCheckedDevices(self):
        global dict_devicebox
        if self.device_1.isChecked():
            dict_devicebox[self.device_1.text()] = 1
        else:
            dict_devicebox[self.device_1.text()] = 0
        if self.device_2.isChecked():
            dict_devicebox[self.device_2.text()] = 1
        else:
            dict_devicebox[self.device_2.text()] = 0
        if self.device_3.isChecked():
            dict_devicebox[self.device_3.text()] = 1
        else:
            dict_devicebox[self.device_3.text()] = 0
        if self.device_4.isChecked():
            dict_devicebox[self.device_4.text()] = 1
        else:
            dict_devicebox[self.device_4.text()] = 0
        if self.device_5.isChecked():
            dict_devicebox[self.device_5.text()] = 1
        else:
            dict_devicebox[self.device_5.text()] = 0
        if self.device_6.isChecked():
            dict_devicebox[self.device_6.text()] = 1
        else:
            dict_devicebox[self.device_6.text()] = 0

        print("dict_devicebox:", dict_devicebox)
        checkeddevice = []
        for (k, v) in dict_devicebox.items():
            if v == 1 and k != '':
                checkeddevice.append(k)
        return checkeddevice

    # 重新设置apkpath并重新获取当前路径下的apklist，重新获取devices
    
    def changePath(self):
        self.text_result.clear()        

        filedialog = QFileDialog()
        #filedialog.setNameFilter("Image Files(*.jpg *.png)")
        #path=open.getOpenFileNames()
        #filedialog.getOpenFileName(self,"选取文件","C:/","APK Files (*.apk);;Text Files (*.txt)")

        path = filedialog.getExistingDirectory(self,"选取文件夹",self.apkpath.text(),)
        if path != "":
            self.text_result.append(str(path))
            self.apkpath.setText(str(path))
    
            # 重置apk
            self.apklist.clear()
            self.apklist.addItems(self.getapklist())

    def getapklist(self):
        global list_apks        
        
        list_apks = []
        mypath = self.apkpath.text()
        if os.path.isdir(mypath):
            for i in os.listdir(mypath):
                if i[-4:] == '.apk':
                    # res.append(mypath + ' > ' + i)
                    list_apks.append(i)
            list_apks.reverse()
        else:
            QMessageBox.warning(
                self, "ERROR", "APK 路径错误，请检查！", QMessageBox.Yes)

        return list_apks

    def GetDeviceInfo(self):
        list_devices = self.getCheckedDevices()
        self.text_result.clear()

        # 遍历勾选的设备
        for devicename in list_devices:

            text_sname = dict_device[devicename]
            print(text_sname, devicename)

            # 初始化设备信息list
            device_info = ["\n品牌：", "\n型号：", "\n分辨率：",
                           "\nAndorid版本：", "\nSDK版本：", "\nCPU版本：", "\n虚拟内存："]

            # 获取出分辨率以外的信息
            command = "adb -s " + text_sname + \
                " shell getprop | grep -E \"ro.product.brand\|ro.product.model\|build.version.sdk\|build.version.release\|product.cpu.abi]\|dalvik.vm.heapsize\""
            self.text_result.append(command)
            result = (self.exctcmd(command).replace("[", "").replace(
                "]", "").replace(" ", "").replace(":", " ").split())
            print(result)
            # 将通过adb 获取到的设备信息插入到list中
            for x in range(len(result)):
                if x % 2 != 0:
                    s = result[x - 1]
                    if "brand" in s:
                        device_info.insert(
                            device_info.index("\n品牌：") + 1, result[x])
                    if "model" in s:
                        device_info.insert(
                            device_info.index("\n型号：") + 1, result[x])
                    if "sdk" in s:
                        device_info.insert(device_info.index(
                            "\nSDK版本：") + 1, result[x])
                    if "release" in s:
                        device_info.insert(device_info.index(
                            "\nAndorid版本：") + 1, result[x])
                    if "cpu" in s:
                        device_info.insert(device_info.index(
                            "\nCPU版本：") + 1, result[x])
                    if "heapsize" in s:
                        device_info.insert(device_info.index(
                            "\n虚拟内存：") + 1, result[x])

            # 获取分别率信息
            command = "adb -s " + text_sname + " shell wm size"
            result = (self.exctcmd(command).split())

            device_info.insert(device_info.index("\n分辨率：") + 1, result[-1])

            self.text_result.append("".join(device_info))

    def installapp(self):
        self.text_result.clear()
        text_appname = self.apklist.currentText()  # 选中的apk
        text_apppath = self.apkpath.text()  # 当前apk路径
        # text_devicesname=self.devicelist.currentText()

        installtype = " "

        if self.overinstall.isChecked():
            installtype = " -r "

        if text_appname != "":
            list_devices = self.getCheckedDevices()

            if len(list_devices) != 0:

                # 遍历勾选的设备
                for devicename in list_devices:

                    text_sname = dict_device[devicename]
                    print(text_sname, devicename)

                    if installtype == " ":
                        self.unitstallapp()
                    text_sname = dict_device[devicename]
                    command = "adb -s " + text_sname + " install" + \
                        installtype + text_apppath + os.sep + text_appname
                    self.text_result.append(command)
                    pids = self.exctcmd(command)

                    self.text_result.append(pids[-50:])
            else:
                QMessageBox.warning(
                    self, "警告", "请先选择设备", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "请先选择apk！", QMessageBox.Yes)

    def unitstallapp(self):
        # self.text_result.clear()
        text_packagename = self.packagename.text()
        text_appname = self.apklist.currentText()  # 选中的apk

        if text_appname != "":
            list_devices = self.getCheckedDevices()

            if len(list_devices) != 0:

                # 遍历勾选的设备
                for devicename in list_devices:

                    text_sname = dict_device[devicename]
                    print(text_sname, devicename)

                    text_sname = dict_device[devicename]
                    command = "adb -s " + text_sname + " uninstall " + text_packagename
                    self.text_result.append(command)
                    pids = self.exctcmd(command)
                    self.text_result.append(pids)
            else:
                QMessageBox.warning(
                    self, "警告", "请先选择设备", QMessageBox.Yes)
        else:
            QMessageBox.warning(
                self, "警告", "请先填写packagename！", QMessageBox.Yes)

    def cutscreen(self):
        global dict_config
        self.text_result.clear()

        list_devices = self.getCheckedDevices()

        if len(list_devices) == 1:
            pc_picpath = dict_config["cutpic_path"]
            if pc_picpath == "":
                pc_picpath = os.path.abspath('.') + os.sep + "ScreencapFiles"

            if os.path.exists(pc_picpath) == False:
                os.mkdir(pc_picpath)

            nowtime = datetime.datetime.now().strftime(timefomate)
            filename = nowtime + ".png"

            text_sname = dict_device[list_devices[0]]
            command = "adb -s " + text_sname + " shell screencap -p /sdcard/" + filename
            self.text_result.append(command)

            pids = self.exctcmd(command)
            self.text_result.append(pids)

            command = "adb -s " + text_sname + " pull /sdcard/" + filename + \
                    " " + pc_picpath + os.sep + filename
            self.text_result.append(command)
            pids = self.exctcmd(command)
            self.text_result.append(pids)

            time.sleep(1)
            filepath = pc_picpath + os.sep + filename
            
            if os.path.exists(filepath):

                self.text_result.append(filepath)
                img = Image.open(filepath)
                imgSize = img.size  # 图片的长和宽
                maxSize = max(imgSize)  # 图片的长边
                minSize = min(imgSize)  # 图片的短边

                screenminsize = GetSystemMetrics(1) - 100

                if maxSize > screenminsize:
                    minSize = screenminsize * minSize / maxSize
                    maxSize = screenminsize

                self.imageViewer.showpic(filepath, maxSize, minSize,0)
                self.imageViewer.show()

        elif len(list_devices) > 1:
            QMessageBox.warning(
                self, "警告", "仅支持单个设备截图，请先选择一个设备", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "请先选择设备", QMessageBox.Yes)
    
    def cutscreenHD(self):
        global dict_config
        self.text_result.clear()

        list_devices = self.getCheckedDevices()

        if len(list_devices) == 1:
            pc_picpath = dict_config["cutpic_path"]
            if pc_picpath == "":
                pc_picpath = os.path.abspath('.') + os.sep + "ScreencapFiles"

            if os.path.exists(pc_picpath) == False:
                os.mkdir(pc_picpath)

            nowtime = datetime.datetime.now().strftime(timefomate)
            filename = nowtime + ".png"

            text_sname = dict_device[list_devices[0]]
            command = "adb -s " + text_sname + " shell screencap -p /sdcard/" + filename
            self.text_result.append(command)

            pids = self.exctcmd(command)
            self.text_result.append(pids)

            command = "adb -s " + text_sname + " pull /sdcard/" + filename + \
                    " " + pc_picpath + os.sep + filename
            self.text_result.append(command)
            pids = self.exctcmd(command)
            self.text_result.append(pids)

            time.sleep(1)
            filepath = pc_picpath + os.sep + filename
            
            if os.path.exists(filepath):

                self.text_result.append(filepath)
                img = Image.open(filepath)
                imgSize = img.size  # 图片的长和宽
                maxSize = max(imgSize)  # 图片的长边
                minSize = min(imgSize)  # 图片的短边

                screenminsize = GetSystemMetrics(1) - 100

                if maxSize > screenminsize:
                    minSize = screenminsize * minSize / maxSize
                    maxSize = screenminsize

                self.imageViewer.showpic(filepath, minSize, maxSize,270)
                self.imageViewer.show()

        elif len(list_devices) > 1:
            QMessageBox.warning(
                self, "警告", "仅支持单个设备截图，请先选择一个设备", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "请先选择设备", QMessageBox.Yes)

    def clearCache(self):
        self.text_result.clear()
        text_packagename = self.packagename.text()

        if text_packagename != "":
            list_devices = self.getCheckedDevices()

            if len(list_devices) == 1:

                text_sname = dict_device[list_devices[0]]
                command = "adb -s " + text_sname + " shell pm clear " + text_packagename
                self.text_result.append(command)
                pids = self.exctcmd(command)
                self.text_result.append(pids)

            elif len(list_devices) > 1:

                QMessageBox.warning(
                    self, "警告", "仅支持单个设备截图，请先选择一个设备", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "请先选择设备", QMessageBox.Yes)
        else:
            QMessageBox.warning(
                self, "警告", "请先填写packagename！", QMessageBox.Yes)

    def cleanresult(self):
        self.text_result.clear()

    def exctcmd(self,command):
        obj = subprocess.Popen(command, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # out_error_list = obj.communicate('print "hello"')
        s = obj.stdout.read()
        # result = s.decode('ascii')
        result = str(s, encoding='utf-8')
        
    
        obj.terminate()
        # print(result)
        return result
    
    
    def getdeviceslist(self):
        """获取设备，并将“device”状态的设备添加到dict_device中"""
        
        global dict_device
        dict_device = {}
    
        pids = self.exctcmd('adb devices').split()[4:]
    
        if pids.count('*') > 0 and pids.count('successfully') > 0:
            pids = pids[16:]
        elif pids.count('*') > 0 and pids.count('successfully') == 0:
            dict_device["Failed to get devices！"] = "Failed to get devices！"
            return 0
    
        pid_s = pids[::2]
        pid_tag = pids[1::2]
        count = len(pid_s)
    
        # 根据device -s 信息获取 设备型号,将设备信息放入device dict中
        if count != 0:
            for x in range(count):
                if pid_tag[x] == 'device':
                    command = "adb -s " + \
                        pid_s[x] + " shell getprop | grep \"ro.product.model\""
                    # 'shell getprop | grep "ro.product.model"'cat /system/build.prop
    
                    modelinfo = self.exctcmd(command).replace(
                        "\r", "").replace(" [", "[").strip('\n')[19:]
                    # print(modeinfo)
                    pid_tag[x] = modelinfo
    
                    dict_device[pid_tag[x]] = pid_s[x]  # 仅考虑连接成功的设备
    
        return dict_device.keys()       

if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
