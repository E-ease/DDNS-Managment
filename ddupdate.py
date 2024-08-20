import requests
from requests import get

# This script only works with cloudflare so dont try to use it for any other provider.
#feel free to modify it any way you would like though.

#fill out the relevent information here
domain = ""
record_type = ""
zone_id = ""
email = "" 
api_key = ""

getip = get("https://api.ipify.org").content.decode('utf8')
# your zone id and records content id should go here in labeled locations
apiurl = "https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_RECORD_ID}"

payload = {
	"Content": getip,
	"name": domain,
	"proxied": False,
	"type": record_type,
	"id": zone_id
}
headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": email,
    "X-Auth-Key": api_key

}

response = requests.request("PUT", apiurl, json=payload, headers=headers)

# should only be use for debugging
# print(response.text)