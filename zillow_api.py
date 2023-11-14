import requests
from api_keys import RAPIDAPI_KEY_ZILLOW

def zillowApi_getStreetAddressesForSale(location, pageNum=1):
    
    url = "https://zillow56.p.rapidapi.com/search"
    querystring = {"location":location,"page":pageNum,"status":"forSale"}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY_ZILLOW,
        "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    totalPages = response.json()['totalPages']
    propertyList = []
    propertyList = response.json()['results']

    pageNum += 1
    if (pageNum <= totalPages):
        propertyList += zillowApi_getStreetAddressesForSale(location, pageNum)

    return propertyList


def zillowApi_getZoningCode(zpid):
    url = "https://zillow56.p.rapidapi.com/property"
    querystring = {"zpid":zpid}
    headers = {
        "X-RapidAPI-Key": "f51f5f378cmsh90d850ffcf37714p1f4419jsne60010f79e6e",
        "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    results = response.json()
    resoFacts = results['resoFacts']
    zoning = resoFacts['zoning']
    return str(zoning)