import os
from time import localtime, strftime

lintedConfig={}

def init():
    with open("config.txt", "r") as rawConfig:
        rawConfig=rawConfig.readlines()
    for i in rawConfig:
        if not i.startswith("#"):
            i=i.replace("\n","")
            if len(i)>2 and len(i.split(":"))!=0:
                i=i.split(":",1)
                lintedConfig[i[0]]=i[1]
    if os.path.isfile("keyfile"):
        with open("keyfile","r") as kFile:
            lintedConfig["discordKey"]=kFile.readlines()[0]
    
    logPrint("config init",6)

def logPrint(message:str,logLevel:int):
    if len(lintedConfig)!=0: #sanity check
        if logLevel <= int(lintedConfig["logLevel"]):
            with open("log.txt","r") as logFile:
                logFile.write(f"[{strftime(lintedConfig["timeFormatLogs"], localtime)}]: {message}")
        if lintedConfig["isDaemon"] == 'false':
            print(message)

init()