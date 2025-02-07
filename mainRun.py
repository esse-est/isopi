import os
import sys

os.chdir(sys.path[0])

lintedConfig={}

def pullConfig():
    
    with(open("config.txt", "r")) as file:
        noLintConfig = file.readlines()
    
    for item in noLintConfig:
        #prevents comments and empty lines from being added
        if not item.startswith("#") and len(item)!=1:
            #removes newline, spaces, and splits into dict friendly format
            item=item.replace("\n","").replace(" ", "",1).split(":",1)
            
            #this wording means that even if something slips through, it wont be added unless it has proper : formatting
            lintedConfig[item[0]] = item[1]
    
    #keyfile override for dev
    if os.path.exists("keyfile"):
        with(open("keyfile","r")) as kfile:
            lintedConfig["discordKey"] = kfile.readlines()[0]

pullConfig()

print(lintedConfig)