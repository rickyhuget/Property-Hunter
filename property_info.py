from api_calls.zillow_api import *
import json
import re

def hasSameZoningCode(code, input):
    match = re.search(code.lower(), input.lower())
    if (match == None):
        return False
    return True

def saveZoningData(fileName, city, state, zoningCode):
    folder_properties = "results_properties\\"
    folder_zoning = "results_zoning\\"

    file_path = folder_properties + fileName
    with open(file_path, 'r') as file:
        resultsDict = json.load(file)

    zoningList = []
    for property in resultsDict["results"]:
        tempList = zillowApi_getZoningData(property['zpid'])  # returns: [parcelNumber, zoning, zoningDescription]
        if ((hasSameZoningCode(zoningCode, tempList[1])) or (hasSameZoningCode(zoningCode, tempList[2]))):
            zpid = property['zpid']
            address = property['address']
            latitude = property['latitude']
            longitude = property['longitude']
            parcelNumber = tempList[0]
            zoning = tempList[1]
            zoningDescription = tempList[2]
            
            tempDict = {
                "zpid" : zpid,
                "address" : address,
                "parcelNumber" : parcelNumber,
                "latitude" : latitude,
                "longitude" : longitude,
                "zoning" : zoning,
                "zoningDescription" : zoningDescription,
            }
            zoningList.append(tempDict)
        
    file_path = folder_zoning + city + "_" + state + "_" + zoningCode + "_zoning.json"
    with open(file_path, 'w') as json_file:
        json.dump(zoningList, json_file, indent=4)
    
def updatePropertyData(city, state, zoningCode):
    zillowApi_getAddressesForSale(city, state)
    saveZoningData(city + "_" + state + "_properties.json", city, state, zoningCode)