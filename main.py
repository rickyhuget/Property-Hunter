import json
import pandas as pd

def getCurrentZoningResults():
    fileName = "currentzoningresults.txt"
    f = open(fileName, "r")

    str = f.read()
    #str = str.replace("\'", "\"")

    propertyList = json.loads(str)
    zoneList = []

    #print(propertyList)

    for property in propertyList:
        if property[2] != "None":
            tempList = [property[1], property[2]]
            zoneList.append(tempList)

    print(zoneList)

getCurrentZoningResults()