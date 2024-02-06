from api_calls.zillow_api import *
    
def updatePropertyData(city, state):
    zillowApi_getAddressesForSale(city, state)