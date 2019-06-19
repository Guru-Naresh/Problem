import requests
import json

res_ob = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=New+york&key="API_ID"')
x = res_ob.json()
print(x)
