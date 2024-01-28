index.html
  initMap(): Asynchronous JavaScript function that imports libraries necessary for the display map and advanced marker elements (or pins) to identify desired properties.
    An addListener event establishes info windows when a marker is clicked by the user that will display information about the marker 
    (this will be the location’s address and any other data to be added that corresponds with the property). 
    Furthermore, with the MarkerClusterer library, groups of markers in the same area will display as one marker displaying the number of markers in the region. 
    This is to ensure a cleaner and more organized display of markers on the map.
  readFile: 
    a JSON file reader gives the user the ability to load a JSON file and use that data to establish the locations of the markers on the map.
  handleFileChange:
    an asynchronous event that parses through the file data that has been imputed through the readFile method. 
    This data is parsed and used to give coordinates to markers on the map and further data that identifies an individual property.
    
property_info.py
  Calls the API requests with the desired data inputs. 
  Once the API calls are made, data is stored in the proper locations.
  updatePropertyData(city, state, zoningCode):
    Initiates the saving of property data from Zillow.com API.
  
