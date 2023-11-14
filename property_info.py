from api_calls.zillow_api import *
import json
import os

def reviseFile(fileName):
    f = open(fileName, "r")
    results = f.read()
    results = results.replace("True", "true")
    results = results.replace("False", "false")
    results = results.replace("\'", "\"")

    if os.path.exists(fileName):
        f = open(fileName, "w")
        f.write(str(results))
    else:
        f = open(fileName, "x")
        f.write(str(results))

def saveZoningData(fileName):
    f = open(fileName, "r")
    data = f.read()
    propertyList = json.loads(data)

    resultList = []
    tempList = ['zpid', 'address', 'none']
    for property in propertyList:
        zpid = property['zpid']
        address = property['streetAddress']
        zoningCode = zillowApi_getZoningCode(zpid)
        tempList = [zpid, address, zoningCode]
        resultList.append(tempList)

    newFileName = "currentzoningresults.txt"

    if os.path.exists(newFileName):
        f = open(newFileName, "w")
        f.write(json.dumps(resultList))
    else:
        f = open(newFileName, "x")
        f.write(json.dumps(resultList))
        
def saveForSaleData(city, state):
    location = city + ", " + state
    results = zillowApi_getStreetAddressesForSale(location)

    #str = date.today()
    #str = str.replace("-", "_")
    date = "11_07_2023"
    newFileName = "results/results_" + date + ".txt"

    if os.path.exists(newFileName):
        f = open(newFileName, "w")
        f.write(str(results))
    else:
        f = open(newFileName, "x")
        f.write(str(results))

    print("reviseFile:")
    reviseFile(newFileName)

    print("saveZoningData:")
    saveZoningData(newFileName)


saveForSaleData("clallam bay", "wa")
print("End of property results")