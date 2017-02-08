# -*- coding: utf-8 -*-


from __future__ import with_statement
import configparser
import os


config_dict = {}


class Config(object):
    """docstring for Config"""

    filepath = os.path.abspath('.') + os.sep + "ANTool_config.conf"
    
    def __init__(self):
        super(Config, self).__init__()
        self.config_dict = {}
        self.currentpath = os.path.abspath('.')
        print(self.currentpath)
        

    def initConfig(self):
        """启动初始化信息"""
        
        if os.path.exists(self.filepath) == False:
            config = configparser.ConfigParser()
            with open(self.filepath, "w") as cfgfile:
                config.add_section("baseinfo")
                config.set("baseinfo", "symbol", "0")
                config.set("baseinfo", "tcp_ip", "")
                config.set("baseinfo", "apk_path", self.currentpath)
                config.set("baseinfo", "packagename", "")
                config.set("baseinfo", "startactivity", "")
                config.set("baseinfo", "cutpic_path", "")
                config.write(cfgfile)
                self.config_dict = {"symbol": "1", "tcp_ip": "", "apk_path": self.currentpath, "packagename": "", "startactivity": "", "cutpic_path": ""}
        else:
            self.getConfig()
        
        return self.config_dict

    def changeConfig_error(self, **kw):
        config = configparser.ConfigParser()
        with open(self.filepath, "r+") as cfgfile:
            for k, v in kw.items():
                config.set("baseinfo", k, v)

            config.write(cfgfile)
            
            
    def getConfig(self):
        config = configparser.ConfigParser()
        with open(self.filepath, "r") as cfgfile:
            config.readfp(cfgfile)
            self.config_dict["symbol"] = config.get("baseinfo", "symbol")
            self.config_dict["tcp_ip"] = config.get("baseinfo", "tcp_ip")
            self.config_dict["apk_path"] = config.get("baseinfo", "apk_path")
            self.config_dict["packagename"] = config.get("baseinfo", "packagename")
            self.config_dict["startactivity"] = config.get("baseinfo", "startactivity")
            self.config_dict["cutpic_path"] = config.get("baseinfo", "cutpic_path")
        return self.config_dict

   
    def changeConfig(self, **kw):
        config = configparser.ConfigParser()
        
        config.read(self.filepath)
        for k, v in kw.items():
            config.set("baseinfo", k, v)
            
        configfile = open(self.filepath,"w")
        config.write(configfile)
        configfile.close()
