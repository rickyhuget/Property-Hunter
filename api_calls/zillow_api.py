import requests
import json
import datetime
from api_calls.api_keys import returnZillowKey

def zillowApi_getAddressesForSale(city, state):
    location = city + ", " + state
    pageNum = 1
    totalPages = 1
    propertyDict = {
        'date' : str(datetime.datetime.today()).split()[0]
    }
    propertyList = []

    while (pageNum <= totalPages):
        url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
        querystring = {"location":location,"page":pageNum,"status":"forSale"}
        headers = {
            "X-RapidAPI-Key": returnZillowKey(),
            "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
        }
        try:
            response = requests.get(url, headers=headers, params=querystring)
            status_code = response.status_code
            if status_code == 200:
                totalPages = response.json()['totalPages']
                propertyList += response.json()['props']
            else:
                return {"error": "Failed to fetch data"}
        except requests.RequestException as e:
            return {"error": f"RequestException: {e}"}
        
        pageNum += 1
        
    if response.status_code == 200:
        propertyDict['results'] = propertyList
        folder_properties = "results_properties\\"
        file_path = folder_properties + city + "_" + state + "_properties.json"
        with open(file_path, 'w') as json_file:
            json.dump(propertyDict, json_file, indent=4)
