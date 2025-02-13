import os
from time import localtime, strftime#, sleep need later but commented so linter doesnt get mad TT

lintedConfig={}
logFile=open("log.txt", "a+")

#logs/backend stuff, generally shouldn't be interacted with on the user end.

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
    
    #format to int as needed
    
    for i in lintedConfig:
        if lintedConfig[i].isnumeric():
            lintedConfig[i] = int(lintedConfig[i])
        
    
    # get up to min if config is below
    if len(lintedConfig["discordKey"]) == 0:
        logPrint("Discord key empty, add a character to silence message if Discord isn't used.", 4)
    
    if lintedConfig["cacheTime"] < 2:
        lintedConfig["cacheTime"] = 2
        logPrint("Cache time below 2 seconds, fixed for runtime", 3)
    
    if lintedConfig["logLevel"] not in range(0,7):
        lintedConfig["logLevel"] = 4
        logPrint("Log level outside of expected range", 3)

def logPrint(message:str,logLevel:int):
    if len(lintedConfig) != 0: #sanity check
        if logLevel <= int(lintedConfig["logLevel"]):
            if len(logFile.readlines()) != 1:
                logFile.write(f"[{strftime(lintedConfig["timeFormatLogs"], localtime())}]: {message} \n")
            else:
                logFile.write(f"[{strftime(lintedConfig["timeFormatLogs"], localtime())}]: {message}")
        if lintedConfig["isDaemon"] == 'false':
            print(message)

def logWrite():
    global logFile
    logFile.close()
    logFile=open("log.txt", "a+")


#gpio interaction

def pullData():
    pass

#output functions

def outputTemp(forceNew: bool, tempFormat: str):
    return("wip")

def outputHydro(forceNew: bool):
    return("wip")

init() #this file won't be directly ran, init() is only for testing
logFile.close() #again, only directly used for the sake of testing