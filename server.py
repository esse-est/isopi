import os
from time import localtime, strftime

lintedConfig={}
logFile=open("log.txt", "a+")


def init():
    with open("config.txt", "r") as rawConfig:
        rawConfig=rawConfig.readlines()
    for i in rawConfig:
        if not i.startswith("#"):
            i=i.replace("\n","")
            i=i.replace(" ","")
            if len(i)>2 and len(i.split(":"))!=0:
                i=i.split(":",1)
                lintedConfig[i[0]]=i[1]
    if os.path.isfile("keyfile"):
        with open("keyfile","r") as kFile:
            lintedConfig["discordKey"]=kFile.readlines()[0]
    
    logPrint("Config init",6)

def logPrint(message:str,logLevel:int):
    if len(lintedConfig) != 0: #sanity check
        if logLevel <= int(lintedConfig["logLevel"]):
            if len(logFile.readlines()) != 1:
                logFile.write(f"[{strftime(lintedConfig["timeFormatLogs"], localtime())}]: {message} \n")
            else:
                logFile.write(f"[{strftime(lintedConfig["timeFormatLogs"], localtime())}]: {message}")
        if lintedConfig["isDaemon"] == 'false':
            print(message)

init() #this file won't be directly ran, init() is only for testing