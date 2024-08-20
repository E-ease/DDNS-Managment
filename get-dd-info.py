#This is just to get the record id but probably could be integrated into ddget as a check for the ip address.
#feel free to modify it to your liking.

import requests
import json

# fill out relevent info here
API_KEY = ""
API_EMAIL = "" 
# zone id goes in the labeled location
API_GET_URL = "https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"

headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": API_EMAIL,
    "X-Auth-Key": API_KEY
}

response = requests.request("GET", API_GET_URL, headers=headers)

# should only be used for Debugging
#print(response.text)

jsonoutput = open('apicalldata.json', 'w')
jsonoutput.write(response.text)
jsonoutput.close()
with open('apicalldata.json', 'r') as file:
    apidata = json.load(file)


result = apidata.get('result')
print(f"Result: {result}")

# use this if you like but the current method looks cleaner.
#fn = apidata.keys()
#print("Names", list(fn))



