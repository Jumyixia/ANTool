#!/usr/bin/python
#-*- coding : utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QDir, Qt
from Ui_MainWindow import Ui_ANTool
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap

import os
import sys

import subprocess
import time
import datetime
from PIL import Image
from win32api import GetSystemMetrics


packageName = 'com.fangyanshow.dialectshow'
comman = "adb devices"
dict_device = {}
dict_devicebox = {}
list_apks = []
timefomate = "%Y%m%d%H%M%S"


def exctcmd(command):
    obj = subprocess.Popen(command, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out_error_list = obj.communicate('print "hello"')
    s = obj.stdout.read()
    result = s.decode('ascii')

    obj.terminate()
    # print(result)
    return result


def getdeviceslist():
    global dict_device
    dict_device = {}

    pids = exctcmd('adb devices').split()[4:]

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
                #'shell getprop | grep "ro.product.model"'cat /system/build.prop

                modelinfo = exctcmd(command).replace(
                    "\r", "").replace(" [", "[").strip('\n')[19:]
                # print(modeinfo)
                pid_tag[x] = modelinfo

                dict_device[pid_tag[x]] = pid_s[x]  # 仅考虑连接成功的设备

    return dict_device.keys()


class ImageViewer(QMainWindow):

    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)




        self.scaleFactor = 0.0

        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        # self.scrollArea.setBackgroundRole(QPalette.Dark)
        # self.scrollArea.setWidget(self.imageLabel)
        # self.setCentralWidget(self.scrollArea)
        self.setCentralWidget(self.imageLabel)
        self.setWindowTitle("Image Viewer")

    def showpic(self, filepath, maxSize, minSize):
        # super(ImageViewer, self).showpic(filepath,maxSize,minSize)
        self.resize(minSize, maxSize)

        image = QImage(filepath)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.scaleFactor = 1.0
        self.imageLabel.adjustSize()


class MyWindow(QtWidgets.QMainWindow, Ui_ANTool):

    def __init__(self):
        super(MyWindow, self).__init__()
        global dict_devicebox

        self.setupUi(self)

        self.imageViewer = ImageViewer(self)

        self.apkpath.setText(os.path.abspath('.'))
        # self.devicelist.addItems(dict_device.keys())

        self.setDevices()

        dict_devicebox = dict.fromkeys(dict_device.keys(), 0)

        #self.cutscreen()

        self.apklist.addItems(self.getapklist())
        self.changepath.clicked.connect(self.changePath)  # 会挂，不能用啊,暂时用来测试功能
        self.btn_reset.clicked.connect(self.reset)
        self.btn_install.clicked.connect(self.installapp)
        self.btn_unitstall.clicked.connect(self.unitstallapp)
        self.btn_screencut.clicked.connect(self.cutscreen)
        self.btn_resultclean.clicked.connect(self.cleanresult)
        self.btn_clearcache.clicked.connect(self.clearCache)
        self.btn_deviceinfo.clicked.connect(self.GetDeviceInfo)
        self.btn_closeapp.clicked.connect(self.get_text)

    def setDevices(self):
        global dict_devicebox
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
    def reset(self):
        self.text_result.clear()
        global dict_device, list_apks

        # 将设备以及apk列表/apkpath全部置空/重置
        self.device_1.setText("")
        self.device_2.setText("")
        self.apklist.clear()
        self.apkpath.setText(os.path.abspath('.'))

        getdeviceslist()
        self.setDevices()
        self.apklist.addItems(self.getapklist())

    # 打开文件选择器，选择文件夹
    def changePath(self):
        self.text_result.clear()


        cpath = QFileDialog()
        # path=open.getOpenFileNames()
        # self.path=open.getOpenFileNames()

        path = cpath.getExistingDirectory()
        self.text_result.append(str(path))
        self.apkpath.setText(str(path))

        # 重置apk
        self.apklist.clear()
        self.getapklist()
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

    def get_text(self):
        global dict_devicebox
        self.text_result.clear()
        self.text_result.append('get_text')

        # device = self.devicelist.currentText()  # 获取设备信息当前的选中的String
        # self.text_result.append(device)
        # if device != "":
        #    device_s = dict_device[device]
        #    self.text_result.append(device_s)

        apkpath = self.apkpath.text()
        self.text_result.append(apkpath)

        install_type = '2'
        if self.overinstall.isChecked():
            install_type = '1'
        self.text_result.append(install_type)

        pname = self.packagename.text()
        self.text_result.append(pname)

        sactivity = self.startactivity.text()
        self.text_result.append(sactivity)

        aa = self.device_1.text()
        self.text_result.append(aa)

        # print(self.label_2.toPlainText())

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
            result = (exctcmd(command).replace("[", "").replace(
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
            result = (exctcmd(command).split())

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
                    pids = exctcmd(command)

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
                    pids = exctcmd(command)
                    self.text_result.append(pids)
            else:
                QMessageBox.warning(
                    self, "警告", "请先选择设备", QMessageBox.Yes)
        else:
            QMessageBox.warning(
                self, "警告", "请先填写packagename！", QMessageBox.Yes)

        # self.text_result.setText('取消按钮改变啦')
        # QMessageBox.warning(self,"警告","信息提示！",QMessageBox.Yes)

    def cutscreen(self):
        self.text_result.clear()

        list_devices = self.getCheckedDevices()

        if len(list_devices) == 1:

            if os.path.exists(os.path.abspath('.') + os.sep + "ScreencapFiles") == False:
                os.mkdir(os.path.abspath('.') + os.sep + "ScreencapFiles")

            nowtime = datetime.datetime.now().strftime(timefomate)
            filename = nowtime + ".png"

            text_sname = dict_device[list_devices[0]]
            command = "adb -s " + text_sname + " shell screencap -p /sdcard/" + filename
            self.text_result.append(command)

            pids = exctcmd(command)
            self.text_result.append(pids)

            command = "adb -s " + text_sname + " pull /sdcard/" + filename + \
                    " " + os.path.abspath('.') + os.sep + \
                    "ScreencapFiles" + os.sep + filename
            self.text_result.append(command)
            pids = exctcmd(command)
            self.text_result.append(pids)

            time.sleep(1)
            filepath = os.path.abspath('.') + os.sep + "ScreencapFiles" + os.sep + filename
            
            if os.path.exists(filepath):

                self.text_result.append(filepath)
                img = Image.open(filepath)
                imgSize = img.size  # 图片的长和宽
                maxSize = max(imgSize)  # 图片的长边
                minSize = min(imgSize)  # 图片的短边

                screenminsize = GetSystemMetrics(1) - 80

                if maxSize > screenminsize:
                    minSize = screenminsize * minSize / maxSize
                    maxSize = screenminsize

                self.imageViewer.showpic(filepath, maxSize, minSize)
                self.imageViewer.show()

        elif len(list_devices) > 1:
            QMessageBox.warning(
                self, "警告", "仅支持单个设备截图，请先选择一个设备", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "请先选择设备", QMessageBox.Yes)

    def opencutpic(self):

            # filepath = os.path.abspath('.') + os.sep + filename
        filepath = "C:/Users/Ju/Desktop/shably.jpg"
        self.text_result.append(filepath)
        img = Image.open(filepath)
        imgSize = img.size  # 图片的长和宽
        maxSize = max(imgSize)  # 图片的长边
        minSize = min(imgSize)  # 图片的短边
        if maxSize > 700:
            minSize = 700 * minSize / maxSize
            maxSize = 700

        # time.sleep(10)
        print(maxSize)
        print(minSize)

        self.text_result.append(filepath)
        self.text_result.append(str(maxSize))
        self.text_result.append(str(minSize))

        self.imageViewer.showpic(filepath, maxSize, minSize)
        self.imageViewer.show()

    def clearCache(self):
        self.text_result.clear()
        text_packagename = self.packagename.text()

        if text_packagename != "":
            list_devices = self.getCheckedDevices()

            if len(list_devices) == 1:

                text_sname = dict_device[list_devices[0]]
                command = "adb -s " + text_sname + " shell pm clear " + text_packagename
                self.text_result.append(command)
                pids = exctcmd(command)
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
        # self.text_result.setText("")


if __name__ == "__main__":

    print(getdeviceslist())
    l = []
    l = list(dict_device.keys())
    print(len(l))

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
