import pandas as pd
import urllib, json

# Declare all variables as strings. Spaces must be replaced with '+', i.e., change 'John Smith' to 'John+Smith'.
# Define the lat, long of the location and the year
lat, lon, year = 33.2164, -97.1292, 2010
# You must request an NSRDB api key from the link above
api_key = 'eSa51PTxM245ppz6gwxMo5NQRVj6OfpPlERGQDRd'

# Declare url string
url = 'http://developer.nrel.gov/api/solar/data_query/v1.json?api_key='+api_key+'&lat='+str(lat)+'&lon='+str(lon)+'&radius=0'
# Return just the first 2 lines to get metadata:
print(url)
# import requests
# r = requests.get(url)
# data = pd.read_json(r.text)
# print(data)
